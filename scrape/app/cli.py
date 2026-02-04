import argparse
import sys
import time
from pathlib import Path

from app import constants as const
from app.link_filters.client_side_filter import ClientSideFilter
from app.link_filters.exclude_list_filter import ExcludeListFilter
from app.link_filters.video_link_filter import VideoLinkFilter
from app.parsers.date_parser import DateParser
from app.parsers.html_link_parser import HtmlLinkParser
from app.pipeline.date_extractor import DateExtractorStep
from app.pipeline.link_fetcher import LinkFetcherStep
from app.pipeline.link_filter import LinkFilterStep
from app.pipeline.pdf_downloader import DownloaderStep
from app.pipeline.pdf_text_extractor import PDFTextExtractorStep
from app.storage.json_store import JsonStore
from app.storage.kv_store import KVStore
from app.storage.pdf_store import PdfStore
from app.pipeline.pipeline import Pipeline
from app.utils.logger import setup_logging

logger = setup_logging()

def main():
    logger.info("Starting Licensing Board Scraper Application (CLI Mode)")

    parser = argparse.ArgumentParser(description="Licensing Board Scrapper CLI")
    parser.add_argument(
        "--pdf-dir",
        type=str,
        default=str(const.DOWNLOAD_DIR),
        help=f"Directory to save downloaded PDFs (default: {const.DOWNLOAD_DIR})",
    )
    parser.add_argument(
        "--txt-dir",
        type=str,
        help="Directory to save extracted text (skips extraction if not provided)",
    )
    args = parser.parse_args()
    pdf_dir = Path(args.pdf_dir)
    txt_dir = Path(args.txt_dir) if args.txt_dir else None
    run_pipeline(pdf_dir, txt_dir)


def run_pipeline(pdf_dir: Path, txt_dir: Path | None):
    start_time = time.perf_counter()
    try:
        # Initialize Shared Context
        store = KVStore()

        # Initialize Dependencies
        json_store = JsonStore()

        pdf_store = PdfStore(pdf_dir)
        exclude_filter = ExcludeListFilter(const.URL_EXCLUDE_LIST_FILE)

        # Build Pipeline Steps
        steps = [
            # 1. Scrape all links from the website
            LinkFetcherStep(store, HtmlLinkParser()),
            # 2. Filter out unwanted (non-pdf) links
            LinkFilterStep(
                store,
                [
                    ClientSideFilter(),
                    VideoLinkFilter(json_store, const.VIDEO_LINKS_FILE),
                    exclude_filter
                ],
            ),
            # 3. Extract dates from links
            DateExtractorStep(store, DateParser()),
            # 4. Download PDFs
            DownloaderStep(store, pdf_store, exclude_filter),
        ]

        # 3. Extract Text (Optional)
        if txt_dir:
            logger.info(f"Text extraction enabled. Output dir: {txt_dir}")
            # Add PDFTextExtractorStep to pipeline steps
            steps.append(PDFTextExtractorStep(store, pdf_dir, txt_dir))
        else:
            logger.info("Text extraction skipped (no --txt-dir provided).")

        # Build and Execute Pipeline
        pipeline = Pipeline(store, steps)
        result = pipeline.run()

        if result.proceed:
            # Log summary stats
            stats = store.get("stats", {})
            logger.info("Link Statistics Summary:")
            for k, v in stats.items():
                logger.info(f"  {k}: {v}")
            logger.info("Application finished successfully.")
        else:
            logger.error(f"Application failed: {result.reason}")
            sys.exit(1)

    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
    finally:
        elapsed = time.perf_counter() - start_time
        minutes, seconds = divmod(elapsed, 60)
        logger.info("Total runtime: %d minutes %.2f seconds", int(minutes), seconds)


if __name__ == "__main__":
    main()
