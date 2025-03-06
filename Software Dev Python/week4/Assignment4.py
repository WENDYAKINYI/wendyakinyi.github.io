from collections import defaultdict, namedtuple, Counter
from typing import List
import csv

# Step 1


class Records:
    """
    A class to represent the entire record dataset files.

    Attributes:
        record_dict (defaultdict): A nested defaultdict to store records and statistics.
    """

    def __init__(self, file_name: str, file_title: str):
        """
        Initializes the Records class by loading data from a specified file.

        Parameters:
            file_name (str): The name of the file to load data from.
            file_title (str): The title to use as a key in the record_dict.
        """
        self.record_dict = defaultdict(lambda: defaultdict(list))
        self.load_data(file_name, file_title)

    def load_data(self, file_name: str, file_title: str):
        """
        Loads data from the file and stores it in the record_dict.

        Parameters:
            file_name (str): The name of the file to load data from.
            file_title (str): The title to use as a key in the record_dict.
        """
        while True:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    # Extract the first line of the file for column names
                    header = next(reader)
                    # Create the Entry namedtuple using column names
                    Entry = self._create_container(header)
                    for row in reader:
                        entry = Entry(*row)
                        self.record_dict[file_title]['data'].append(entry)
            except FileNotFoundError:
                print(
                    f"File {file_name} not found. Please enter a valid file name.")
                file_name_input = input(
                    "Enter a valid file name or 'q' to quit: ")
                if file_name_input.lower() == 'q':
                    return
                file_name = file_name_input
            else:
                print(
                    f"File {file_name} loaded successfully into '{file_title}'.")
                break  # Exit the loop if file is loaded successfully

    def _create_container(self, columns: List[str]):
        """
        Creates a namedtuple container for data entries based on column names.

        Parameters:
            columns (List[str]): A list of column names from the dataset.

        Returns:
            namedtuple: A namedtuple class with standardized column names as fields.
        """
        standardized_columns = self._standardize_col_names(columns)
        Entry = namedtuple('Entry', standardized_columns)
        return Entry

    def _standardize_col_names(self, columns: List[str]) -> List[str]:
        """
        Standardizes column names by removing special characters and ensuring alpha-numeric names.

        Parameters:
            columns (List[str]): A list of column names to be standardized.

        Returns:
            List[str]: A list of standardized, alpha-numeric column names.

        Raises:
            InvalidColumnNames: If any column name is not alpha-numeric after standardization.
        """
        # Replace "_" and "-" with an empty string, and remove blank spaces
        standardized_columns = [
            ''.join(filter(str.isalnum, col)) for col in columns]

        # Check if all column names are alpha-numeric after standardization
        if not all(col.isalnum() for col in standardized_columns):
            invalid_columns = [col for col in columns if not ''.join(
                filter(str.isalnum, col)).isalnum()]
            raise InvalidColumnNames(invalid_columns)

        return standardized_columns

    def record_stats(self, file_title: str, column_name: str, extract_value_lambda):
        """
        Record statistics for a specific column using a lambda function.

        Parameters:
            file_title (str): The title of the file in record_dict.
            column_name (str): The column name to process.
            extract_value_lambda (lambda): The lambda function to extract values from the column.
        """
        # Retrieve the list of data entries (namedtuples) for the given file_title
        data_entries = self.record_dict[file_title]['data']
        column_values = map(extract_value_lambda, data_entries)
        # Summarize the number of instances for each unique value
        column_stats = Counter(column_values)
        stats_key = f'stats_{column_name}'
        self.record_dict[file_title][stats_key] = column_stats

    def extract_top_n(self, n: int, file_title: str, stats_column_name: str):
        """
        Returns the top n most frequent values for the Counter object created by the record_stats method.

        Parameters:
            n (int): Number of top values to extract.
            file_title (str): The title of the file in record_dict.
            stats_column_name (str): The column name for statistics.

        Returns:
            List: Top n most frequent values with counts.

        Raises:
            NoRecordStatsFound: If the stats_column_name doesn't exist.
        """
        try:
            stats_counter = self.record_dict[file_title][stats_column_name]
            # Return the top n most common values
            return stats_counter.most_common(n)
        except KeyError:
            # If the stats_column_name doesn't exist, raise NoRecordStatsFound exception
            raise NoRecordStatsFound(stats_column_name)

# Step 2


class InvalidColumnNames(Exception):
    """Exception raised for invalid column names in the dataset."""

    def __init__(self, column_names: list):
        """
        Initializes the InvalidColumnNames exception.

        Parameters:
            column_names (list): A list of invalid column names.
        """
        self.column_names = column_names
        self.msg = "The names of the columns are invalid. Column names can only be letters and numbers: {}".format(
            ", ".join(column_names))
        super().__init__(self.msg)
        print(self.msg)


class NoRecordStatsFound(Exception):
    """Exception raised when no statistics are found for a requested column."""

    def __init__(self, column_name: str):
        """
        Initializes the NoRecordStatsFound exception.

        Parameters:
            column_name (str): The name of the column for which statistics are not found.
        """
        self.column_name = column_name
        self.msg = "The column stats you’re trying to access doesn’t exist. You entered {}.".format(
            column_name)
        super().__init__(self.msg)
        print(self.msg)


if __name__ == "__main__":
    try:
        # Test loading credit card records
        credit_card_records = Records('credit_card.csv', 'Credit Card')

        # Test loading customer complaints records
        complaints_records = Records('customer_complaints.csv', 'Complaints')

        # Example for most common values in the customer complaints file
        complaints_records.record_stats(
            'Complaints', 'Product', lambda entry: entry.Product)
        print(
            complaints_records.record_dict['Complaints']['stats_Product'].most_common(5))

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except InvalidColumnNames as e:
        print(f"Invalid column names: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
