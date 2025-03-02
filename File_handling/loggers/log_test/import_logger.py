import os
import logging

# Default values (can be overwritten by config.py if it exists)
try:
    from config import DEFAULT_LOG_PATH, DEFAULT_LOG_FILE, DEFAULT_LOG_LEVEL
except ImportError:
    DEFAULT_LOG_PATH = r"C:\Users\stout\Documents\GitHub\logging-snippets"  # location of saved .log file
    DEFAULT_LOG_FILE = "test.log"  # naming of the file
    DEFAULT_LOG_LEVEL = "DEBUG"  # assigns level of the console handler


def setup_custom_logger(
    log_path=DEFAULT_LOG_PATH, log_file=DEFAULT_LOG_FILE, log_level=DEFAULT_LOG_LEVEL
):
    """Set up a custom logger with both console and file handlers."""
    log_directory = os.path.join(log_path)
    log_file_path = os.path.join(log_directory, log_file)

    # Ensure log directory exists
    os.makedirs(log_directory, exist_ok=True)

    # Create and configure the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(getattr(logging, log_level.upper(), logging.DEBUG))

    # **Prevent duplicate handlers**
    if logger.hasHandlers():
        logger.handlers.clear()

    # Console handler with simple formatting
    console_handler = logging.StreamHandler()
    console_handler.setLevel(
        getattr(logging, log_level.upper(), logging.DEBUG)
    )  # Console follows DEFAULT_LOG_LEVEL
    console_handler.setFormatter(
        logging.Formatter("%(levelname)s - %(message)s")
    )  # Simple format for console

    # File handler with detailed formatting
    file_handler = logging.FileHandler(log_file_path, mode="a", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)  # Always logs everything to the file
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )  # Detailed format for file

    # Add both handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Log initialization message
    logger.info(f"Logger initialized at level {log_level}. Logging to: {log_file_path}")

    return logger


# Initialize logger with flexible settings
logger = setup_custom_logger()


def main():
    logger.info(f"Starting up main function: {__name__}.")


if __name__ == "__main__":
    main()
    logger.info("Script finished.")
