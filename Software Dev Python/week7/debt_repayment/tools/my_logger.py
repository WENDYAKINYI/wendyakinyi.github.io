import logging
import os


def custom_logger(name):
    """
    Creates and configures a custom logger with a specified name.

    Parameters
    - name (str):The name of the logger. 

    Returns
    -logger : logging.Logger
        The configured logger object ready for logging messages.
    """
    log_directory = "debt_repayment/files/logs"
    # Checks if the logs directory exists, if not, creates it
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(name)s - %(lineno)d: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    log_file_path = os.path.join(log_directory, 'getting_out_of_debt.log')

    logger = logging.getLogger(name)
    if not logger.handlers:  # For checking if the logger already has handlers to avoid duplicates
        handler = logging.FileHandler(filename=log_file_path, mode='a')
        handler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)

    return logger
