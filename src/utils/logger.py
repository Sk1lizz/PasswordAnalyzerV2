import logging
import sys

from logging.handlers import RotatingFileHandler
from pathlib import Path

from src.utils.paths import get_logs_path
from src.utils.config import (
    LOG_CONSOLE_LEVEL,
    LOG_FILE_LEVEL,
    LOG_FORMAT,
    LOG_DATE_FORMAT,
    LOG_FILE,
    LOG_BACKUP_COUNT,
    LOG_MAX_BYTES,
)

def setup_logger() -> logging.Logger:
    logger = logging.getLogger("PasswordAnalyzer")
    logger.setLevel(logging.DEBUG)

    if logger.handlers: return logger

    formatter = logging.Formatter(
        LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
    )

    console_handlers = logging.StreamHandler(sys.stdout)
    console_handlers.setLevel(LOG_CONSOLE_LEVEL)
    console_handlers.setFormatter(formatter)
    logger.addHandler(console_handlers)

    log_dir = get_logs_path()
    log_file = log_dir / LOG_FILE

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=LOG_MAX_BYTES,
        backupCount=LOG_BACKUP_COUNT,
        encoding="utf-8",
    )

    file_handler.setLevel(LOG_FILE_LEVEL)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()