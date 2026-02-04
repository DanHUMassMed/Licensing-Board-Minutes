import logging
from pathlib import Path

import fitz  # PyMuPDF

from app.storage.kv_store import KVStore
from app.storage.run_result import RunResult

logger = logging.getLogger(__name__)


class PDFTextExtractorStep:
    """
    Extracts text from downloaded PDFs.
    """

    def __init__(self, kv_store: KVStore, pdf_dir: Path, output_dir: Path):
        self.kv_store = kv_store
        self.pdf_dir = pdf_dir
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def run(self) -> RunResult:
        logger.info("Starting text extraction process...")
        if not self.pdf_dir.exists():
            logger.error(f"PDF directory not found: {self.pdf_dir}")
            return RunResult(proceed=False, reason="PDF directory not found")

        pdf_files = sorted(self.pdf_dir.glob("*.pdf"))
        if not pdf_files:
            logger.warning(f"No PDF files found in {self.pdf_dir}")
            return RunResult(proceed=True)

        logger.info(f"Found {len(pdf_files)} PDF files to process.")
        for pdf_file in pdf_files:
            self._process_file(pdf_file)

        return RunResult(proceed=True)

    def _process_file(self, pdf_file):
        output_file = self.output_dir / f"{pdf_file.stem}.txt"
        text = self._extract_text(pdf_file)
        text = self._strip_non_ascii(text)
        if text:
            try:
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(text)
                logger.info(f"Extracted {pdf_file.name} -> {output_file.name}")
            except OSError as e:
                logger.error(f"Failed to write text file {output_file}: {e}")
        else:
            logger.warning(f"No text extracted from {pdf_file.name}")

    def _extract_text(self, pdf_path) -> str:
        try:
            doc = fitz.open(pdf_path)
            all_text = []
            for page in doc:
                text = page.get_text()
                if text.strip():
                    all_text.append(text.strip())
            doc.close()
            return "\n".join(all_text)
        except Exception as e:
            logger.error(f"Error extracting text from {pdf_path}: {e}")
            return ""

    def _strip_non_ascii(self, text: str) -> str:
        return text.encode("ascii", errors="ignore").decode("ascii")
