import logging
import datetime


def my_logger(log_file):
    """
    Custom logger function that logs messages to the specified log file with timestamp.

    Args:
        log_file (str): The file path where the log messages will be saved.
    """
    # Create a logger
    logger = logging.getLogger('custom_logger')
    logger.setLevel(logging.DEBUG)

    # Create a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter(
        '%(asctime)s::%(lineno)d::%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger


if __name__ == "__main__":
    logger = my_logger("my_log.log")
    logger.debug("This is a debug message.")
