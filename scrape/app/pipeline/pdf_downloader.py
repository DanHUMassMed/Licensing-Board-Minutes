import logging
import shutil
from io import BytesIO
from pathlib import Path
from urllib.parse import urljoin

import pikepdf
import requests

from app import constants as const
from app.link_filters.exclude_list_filter import ExcludeListFilter
from app.storage.kv_store import KVStore
from app.storage.pdf_store import PdfStore
from app.storage.run_result import RunResult

logger = logging.getLogger(__name__)


class DownloaderStep:
    """
    Downloads voting minute PDFs from the links in KVStore.
    """

    def __init__(
        self, kv_store: KVStore, pdf_store: PdfStore, exclude_filter: ExcludeListFilter
    ):
        self.kv_store = kv_store
        self.pdf_store = pdf_store
        self.exclude_filter = exclude_filter

    def run(self) -> RunResult:
        links = self.kv_store.get("minutes_links", [])
        if not links:
            logger.warning("No links found for downloading.")
            return RunResult(proceed=True)

        logger.info("Starting download process...")
        for item in links:
            href = item.get("href")
            date_str = item.get("date")

            if not href or not date_str:
                logger.warning(f"Skipping malformed item: {item}")
                continue

            if href in self.exclude_filter.exclude_items:
                continue

            content = self._download_pdf(href)
            if content:
                self.pdf_store.save_pdf(content, date_str)

        self._copy_exception_pdfs(const.EXCEPTION_PDFS, self.pdf_store.download_dir)
        return RunResult(proceed=True)

    def _download_pdf(self, href: str) -> bytes | None:
        url = self._prepare_url(href)
        try:
            resp = requests.get(url, timeout=const.DEFAULT_TIMEOUT)
            resp.raise_for_status()
            content = resp.content

            if self._is_valid_pdf(content):
                return content
            else:
                logger.warning(f"Invalid PDF at {url}. Adding to exclude list.")
                self.exclude_filter.add_url(href)
                return None

        except requests.RequestException as e:
            logger.error(f"Failed to download {url}: {e}")
            return None

    def _prepare_url(self, href: str) -> str:
        if "drive.google.com" in href and "/file/d/" in href:
            file_id = href.split("/file/d/", 1)[1].split("/", 1)[0]
            return f"https://drive.google.com/uc?export=download&id={file_id}"
        return urljoin(const.BASE_URL, href)

    def _is_valid_pdf(self, content: bytes) -> bool:
        try:
            with pikepdf.open(BytesIO(content)):
                return True
        except pikepdf.PdfError:
            return False

    def _copy_exception_pdfs(
        self,
        source_dir: str | Path,
        destination_dir: str | Path,
    ) -> int:
        src = Path(source_dir)
        dst = Path(destination_dir)

        if not src.exists() or not src.is_dir():
            logger.warning(f"Source directory for exception PDFs does not exist: {src}")
            return 0

        dst.mkdir(parents=True, exist_ok=True)
        pdf_files = list(src.glob("*.pdf"))

        for pdf in pdf_files:
            shutil.copy2(pdf, dst / pdf.name)

        return len(pdf_files)
