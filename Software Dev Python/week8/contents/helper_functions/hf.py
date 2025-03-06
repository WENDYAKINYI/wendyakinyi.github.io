import os
import re


def retrieve_files(file_extension):
    """
    Traverses the directories starting from the current working directory and
    retrieves all files matching the given extension.

    Parameters:
    -extension: The file extension to search for (e.g., ".txt").
    Returns: A list of paths to files matching the extension.
    """
    matching_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(file_extension):
                matching_files.append(os.path.join(root, file))
    return matching_files


def record_loader_gen(file_paths):
    """
    A generator that yields records from the given list of file paths. Each record
    consists of the name, gender, births, and year extracted from the file name and contents.

    Parameters:
    - file_paths: A list of file paths to process.
    """
    year_pattern = re.compile(r'yob(\d{4})\.txt$')
    for file_path in file_paths:
        match = year_pattern.search(file_path)
        if match:
            year = int(match.group(1))
            with open(file_path, 'r') as file:
                for line in file:
                    name, gender, births = line.strip().split(',')
                    yield name, gender, int(births), year
