import logging

import requests

from app import constants as const
from app.parsers.html_link_parser import HtmlLinkParser
from app.storage.kv_store import KVStore
from app.storage.run_result import RunResult

logger = logging.getLogger(__name__)


class LinkFetcherStep:
    """
    Fetches HTML from the target URL and extracts initial links.
    """

    def __init__(self, kv_store: KVStore, html_parser: HtmlLinkParser):
        self.kv_store = kv_store
        self.html_parser = html_parser

    def run(self) -> RunResult:
        url = const.TARGET_URL
        logger.info(f"Fetching {url}...")

        try:
            html = self._fetch_html(url)
            links = self.html_parser.extract_links(html)

            self.kv_store.set("raw_links", links)
            self.kv_store.set("stats", {"total_links": len(links)})

            logger.info(f"Found {len(links)} raw links.")
            return RunResult(proceed=True)

        except Exception as e:
            logger.error(f"LinkFetcherStep failed: {e}")
            return RunResult(proceed=False, reason=str(e))

    def _fetch_html(self, url: str) -> str:
        try:
            resp = requests.get(url, timeout=const.DEFAULT_TIMEOUT)
            resp.raise_for_status()
            if not resp.text:
                raise RuntimeError(f"Empty response from {url}")
            return resp.text
        except requests.RequestException as e:
            raise RuntimeError(f"Network error fetching {url}: {e}") from e
