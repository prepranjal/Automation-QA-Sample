# in/wrapstore/automation/utils/logger_util.py

import logging
import os
import sys


class LoggerUtil:
    """Unified logger utility replicating Log4j2 (console + file appenders)."""

    _configured = False

    @staticmethod
    def _configure_logger():
        """Configures both console and file logging with the same pattern as log4j2.xml."""
        if LoggerUtil._configured:
            return

        # Ensure logs directory exists
        logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
        os.makedirs(logs_dir, exist_ok=True)

        log_file = os.path.join(logs_dir, "wrapstore.log")

        # Log format — same as your log4j.xml patterns
        formatter_console = logging.Formatter(
            fmt="%(asctime)s [%(threadName)s] %(levelname)-5s %(name)s - %(message)s",
            datefmt="%H:%M:%S",
        )
        formatter_file = logging.Formatter(
            fmt="%(asctime)s %(levelname)-5s %(filename)s:%(lineno)d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter_console)

        # File handler (append mode)
        file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        file_handler.setFormatter(formatter_file)

        # Configure root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)
        root_logger.addHandler(console_handler)
        root_logger.addHandler(file_handler)

        LoggerUtil._configured = True

    @staticmethod
    def info(message: str):
        LoggerUtil._configure_logger()
        logging.info(message)

    @staticmethod
    def warn(message: str):
        LoggerUtil._configure_logger()
        logging.warning(message)

    @staticmethod
    def error(message: str):
        LoggerUtil._configure_logger()
        logging.error(message)
