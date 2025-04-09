import logging
import os
from datetime import datetime
from pathlib import Path


class Logger:

    def __init__(self, log_file_path=None, log_level=logging.INFO):

        # Create logs directory if it doesn't exist
        log_dir = Path(__file__).parent.parent / 'logs'
        log_dir.mkdir(exist_ok=True)

        # Set default log file path if not provided
        if log_file_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file_path = log_dir / f"test_run_{timestamp}.log"

        # Configure logger
        self.logger = logging.getLogger('playwright_tests')
        self.logger.setLevel(log_level)
        self.logger.handlers = []  # Clear existing handlers to avoid duplicates

        # Create file handler
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(log_level)

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        self.info(f"Logger initialized. Log file: {log_file_path}")

    def debug(self, message):
        """Log a debug message."""
        self.logger.debug(message)

    def info(self, message):
        """Log an info message."""
        self.logger.info(message)

    def warning(self, message):
        """Log a warning message."""
        self.logger.warning(message)

    def error(self, message):
        """Log an error message."""
        self.logger.error(message)

    def critical(self, message):
        """Log a critical message."""
        self.logger.critical(message)

    def exception(self, message):
        """Log an exception message with traceback."""
        self.logger.exception(message)


# Create a singleton instance for global use
def get_logger(log_file_path=None, log_level=logging.INFO):

    return Logger(log_file_path, log_level)

