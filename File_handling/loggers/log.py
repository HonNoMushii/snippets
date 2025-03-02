import logging
import os

DEFAULT_LOG_PATH = r"C:\Users\"
DEFAULT_LOG_FILE = "test.log"
DEFAULT_LOG_LEVEL = "DEBUG"


def setup_custom_logger():
    """Set up a custom logger with both console and file handlers."""

    logger = logging.getLogger(
        "osrs_logger"
    )  # Use a unique logger name to avoid conflicts
    if logger.hasHandlers():
        logger.handlers.clear()  # Clear any existing handlers to avoid duplicates

    log_directory = os.path.join(DEFAULT_LOG_PATH)
    log_file_path = os.path.join(log_directory, DEFAULT_LOG_FILE)

    # Ensure log directory exists
    os.makedirs(log_directory, exist_ok=True)

    # Set up logging level
    logger.setLevel(getattr(logging, DEFAULT_LOG_LEVEL.upper(), logging.DEBUG))

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

    # File handler
    file_handler = logging.FileHandler(log_file_path, mode="a", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
    )

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = True  # Ensure messages propagate

    # Add a test log to confirm logger is working
    logger.info(
        f"Logger initialized at level {DEFAULT_LOG_LEVEL}. Logging to: {log_file_path}"
    )

    return logger


# Initialize logger with flexible settings
logger = setup_custom_logger()

# Test the logger immediately after setup
logger.debug("Logger setup is complete and the test log is working.")
