import csv
from real_estate.helper_functions.context_manager import custom_context_manager
from ..helper_functions import calculate_stats
from collections import namedtuple
from collections import defaultdict


class RealEstate:
    """
    A class containing the entire real estate dataset.

    Attributes:
        properties_dict (defaultdict): A nested defaultdict to store real estate data.
    """
    Property = namedtuple(
        'Property', ['status', 'bed', 'bath', 'acre_lot', 'city', 'state', 'zip_code', 'house_size', 'prev_sold_date', 'price'])

    def __init__(self, file_name, location):
        """
        Constructs all the necessary at=ributes for the RealEstate object and makes a call to the load data method.

        Parameters:
            file_name (str): The name of the file containing real estate data.
            location (str): The location of the file.
        """
        self.file_name = file_name
        self.location = location
        self.properties_dict = defaultdict(lambda: defaultdict(list))
        self.load_data()
        return

    def load_data(self):
        """
        Load data from the specified file using a custom context manager.

        Parameters:
        - file_name (str): The name of the file containing real estate data.
        - location (str): The location to categorize the data (e.g., "US States" or "Territories").
        """
        valid_file = False
        while not valid_file:
            try:
                with custom_context_manager(self.file_name, 'r', self.location) as file:
                    reader = csv.reader(file)
                    header = next(reader)
                    Property = self._create_container(header)
                    for row in reader:
                        property_entry = Property(*row)
                        # Categorize the entry as 'US States' or 'Territories'
                        category = 'Territories' if property_entry.state in [
                            'Puerto Rico', 'Virgin Islands'] else 'US States'
                        if property_entry.state not in self.properties_dict[category]:
                            self.properties_dict[category][property_entry.state] = [
                            ]
                        self.properties_dict[category][property_entry.state].append(
                            property_entry)
                    valid_file = True
            except FileNotFoundError:
                print("File not found.")
                user_input = input(
                    "Please enter a valid file name or 'q' to quit: ")
                if user_input.lower() == 'q':
                    return  # Exit the method if the user decides to quit
                else:
                    self.file_name = user_input  # Update the file name and retry
                    return

    def _create_container(self, header):
        """
        Create a namedtuple 'Property' with attributes based on the column names in the header.

        Parameters:
            header (list): List of column names from the file.

        Returns:
            namedtuple: A namedtuple with attributes based on the column names.
        """
        self.Property = namedtuple('Property', header)
        return self.Property

    def compute_stats(self, func_name, *args, **kwargs):
        """
        Compute statistics using a function from the calculate_stats module.

        Parameters:
            func_name (str): The name of the function from the calculate_stats module.
            *args: Variable number of positional arguments for the function.
            **kwargs: Variable number of keyword arguments for the function.

        Returns:
            float: The value returned by the function.
        """
        try:
            # Get the function from calculate_stats module
            func = getattr(calculate_stats, func_name)
            # Call the function with provided arguments
            result = func(*args, **kwargs)
            return result
        except AttributeError:
            print(
                f"Function '{func_name}' not found in calculate_stats module.")
            return None
