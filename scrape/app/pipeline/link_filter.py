import logging
from typing import Any

from app.storage.kv_store import KVStore
from app.storage.run_result import RunResult

logger = logging.getLogger(__name__)


class LinkFilterStep:
    """
    Applies a sequence of filters to the links in KVStore.
    """

    def __init__(self, kv_store: KVStore, filters: list[Any]):
        self.kv_store = kv_store
        self.filters = filters

    def run(self) -> RunResult:
        links = self.kv_store.get("raw_links", [])
        stats = self.kv_store.get("stats", {})

        filtered_links = links
        for filter in self.filters:
            prev_len = len(filtered_links)
            filtered_links = filter.process(filtered_links)

            filter_name = filter.__class__.__name__
            removed_count = prev_len - len(filtered_links)

            # Attribute stats for compatibility
            if "ClientSide" in filter_name:
                stats["client_side_links"] = removed_count
            elif "Exclude" in filter_name:
                stats["excluded_links"] = removed_count
            elif "Video" in filter_name:
                stats["video_links"] = removed_count

        self.kv_store.set("filtered_links", filtered_links)
        self.kv_store.set("stats", stats)

        logger.info(f"Filtering complete. {len(filtered_links)} links remaining.")
        return RunResult(proceed=True)
