import os
from contextlib import contextmanager


@contextmanager
def custom_context_manager(file_name, mode, destination):
    """
    A context manager function to temporarily change the current working directory
    to a specified destination for file operations, and revert it back
    after the operations are done.

    Parameters:
        file_name (str): The name of the file to be opened.
        mode (str): The mode in which the file should be opened.
        destination (str): The destination directory to temporarily change to.

    Yields:
        file object: The file opened in the specified mode.
    """
    original_path = os.getcwd()
    file = None
    try:
        print("Loading data")
        os.chdir(destination)
        file = open(file_name, mode)
        yield file
    finally:
        file.close()
        os.chdir(original_path)
        print("Data loaded")
