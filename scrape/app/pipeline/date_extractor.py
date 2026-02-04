import logging

from app.parsers.date_parser import DateParser
from app.storage.kv_store import KVStore
from app.storage.run_result import RunResult

logger = logging.getLogger(__name__)


class DateExtractorStep:
    """
    Extracts dates from the filtered links.
    """

    def __init__(self, kv_store: KVStore, date_parser: DateParser):
        self.kv_store = kv_store
        self.date_parser = date_parser

    def run(self) -> RunResult:
        links = self.kv_store.get("filtered_links", [])
        if not links:
            logger.warning("No links to extract dates from.")
            return RunResult(proceed=True)

        logger.info(f"Extracting dates from {len(links)} links...")
        processed_minutes = []
        for link in links:
            # We clone the link to avoid side effects if needed,
            # though here we just add the date.
            link_data = dict(link)
            link_data["date"] = self.date_parser.parse(link["body"], link["href"])
            processed_minutes.append(link_data)

        self.kv_store.set("minutes_links", processed_minutes)

        stats = self.kv_store.get("stats", {})
        stats["minutes_links"] = len(processed_minutes)
        self.kv_store.set("stats", stats)

        return RunResult(proceed=True)
