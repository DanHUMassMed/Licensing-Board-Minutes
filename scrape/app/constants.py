from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
STATE_DIR = BASE_DIR / "scraper_state"
LOG_DIR = BASE_DIR / "log"

# Files
VIDEO_LINKS_FILE = STATE_DIR / "hearing_video_links.json"
URL_EXCLUDE_LIST_FILE = STATE_DIR / "url_exclude_list.json"
DOWNLOAD_DIR = BASE_DIR / "../voting_minutes_pdfs"
EXCEPTION_PDFS = STATE_DIR / "exception_pdfs"

# Scraping
TARGET_URL = "https://www.boston.gov/departments/licensing-board/licensing-board-information-and-members"
BASE_URL = "https://www.boston.gov"

# Defaults
DEFAULT_TIMEOUT = 30
