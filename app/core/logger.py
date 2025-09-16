# app/core/logger.py
import logging
from logging.handlers import RotatingFileHandler
import sys

# Create a logger
logger = logging.getLogger("ronsare_logger")
logger.setLevel(logging.INFO)  # Set default log level

# Formatter for log messages
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Console handler (logs to stdout)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Optional: File handler with rotation (logs to file)
file_handler = RotatingFileHandler(
    "logs/ronsare.log", maxBytes=5*1024*1024, backupCount=3
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Usage example:
# from app.core.logger import logger
# logger.info("This is an info log")
# logger.error("This is an error log")
