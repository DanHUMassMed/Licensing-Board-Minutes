import logging
import sys
from logging.handlers import RotatingFileHandler

from app import constants as const


import logging
import sys
from logging.handlers import RotatingFileHandler

from app import constants as const


def setup_logging(log_filename: str = "scraper.log") -> logging.Logger:
    """
    Configures the root logger with a RotatingFileHandler and stdout stream.
    All child loggers automatically inherit this configuration.
    """
    const.LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_file_path = const.LOG_DIR / log_filename

    # Get the root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Remove existing handlers to avoid duplicates
    if logger.hasHandlers():
        logger.handlers.clear()

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # Rotating file handler
    file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    # Stream handler
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    # Return root logger for convenience
    return logger

