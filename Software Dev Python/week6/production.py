import pandas as pd
import numpy as np


class RealEstate2:
    """
    A class to contain the entire real estate data set.

    Attributes:
    -----------
    properties_df : pandas.DataFrame
        A DataFrame to store real estate properties data.

    Methods:
    --------
    __init__(file_name, location):
        Initializes the RealEstate2 object with properties_df as an empty DataFrame and calls load_data method.

    load_data(file_name, file_path):
        Loads data from a CSV file into properties_df and preprocesses it.

    _col_2_numeric():
        Converts specified columns to numeric, replacing unconvertible values with NaN.

    _check_type(s):
        Returns the data types of the columns of the DataFrame.

    _num_nulls(col_name):
        Returns the number of null values in the specified column.

    _get_unique_vals(col_name):
        Returns the number of unique values and the unique values themselves for the specified column.

    _filth_be_gone(col_name, value):
        Removes all rows containing the specified value from the given column.

    _col_val_count(col_name):
        Returns the count of each value present in the given column.

    _summary_table(index_cols, summary_cols, operations)::
        Generates a summary table based on user-defined columns and operations.

    """

    def __init__(self, file_name, location):
        """
        Constructs all the necessary attributes for the RealEstate2 object.

        Parameters:
        -----------
        file_name : str
            The name of the file containing real estate data.
        location : str
            The location or path where the file is stored.
        """
        self.properties_df = pd.DataFrame()
        self.load_data(file_name, location)

    def load_data(self, file_name, file_path):
        """
        Loads data from a CSV file into the properties_df DataFrame and preprocesses it.

        Parameters:
        -----------
        file_name : str
            The name of the file containing real estate data.
        file_path : str
            The path where the file is located.
        """
        try:
            full_path = f"{file_path}/{file_name}"
            self.properties_df = pd.read_csv(full_path, low_memory=False)
            self._col_2_numeric()
            self.properties_df.drop_duplicates(inplace=True)
        except FileNotFoundError:
            print("File not found. Please check the file name and path.")
            user_input = input("Enter a valid file name or 'q' to quit: ")
            if user_input.lower() != 'q':
                self.load_data(user_input, file_path)
            else:
                print("Exiting program.")

    def _col_2_numeric(self):
        """
        Converts specified columns to numeric, replacing unconvertible values with NaN.
        """

        # SpecifIc columns known to be numeric
        cols_to_convert = ['bed', 'bath', 'price']
        for col_name in cols_to_convert:
            if col_name in self.properties_df.columns:
                self.properties_df[col_name] = pd.to_numeric(
                    self.properties_df[col_name], errors='coerce')
        else:
            print(f"Column '{col_name}' not found in the DataFrame.")

    def _check_column_exists(self, *cols):
        """
        Helper method to check if  multiple columns exist in the DataFrame.

        Parameters:
        -----------
        *cols  : str
            The name of the columns to check.

        Returns:
        --------
        bool
            True if all columns exist, False otherwise.
        """
        missing_columns = [
            col for col in cols if col not in self.properties_df.columns]
        if missing_columns:
            print(f"Columns not found in the DataFrame: {
                ', '.join(missing_columns)}")
            return False
        return True

    def _percentage_above_mode(self, col):
        """
        Custom summary operation to calculate the percentage of values above the mode value in a column.

        Parameters:
        -----------
        col : pandas.Series
            The column for which to calculate the percentage.

        Returns:
        --------
        float
            The percentage of values above the mode value in the column.
        """
        mode_val = col.mode().iloc[0]
        above_mode_count = (col > mode_val).sum()
        total_count = len(col)
        percentage_above_mode = (above_mode_count / total_count) * 100
        return percentage_above_mode

    def check_type(self):
        """
        Returns the data types of the columns of the DataFrame.

        Returns:
        --------
        pandas.Series
            The data types of the DataFrame's columns.
        """
        return self.properties_df.dtypes

    def num_nulls(self, col_name):
        """
        Returns the number of null values in the specified column.

        Parameters:
        -----------
        col_name : str
            The name of the column.

        Returns:
        --------
        int
            The number of null values in the column, or None if the column doesn't exist.
        """
        if self._check_column_exists(col_name):
            return self.properties_df[col_name].isnull().sum()
        return None

    def get_unique_vals(self, col_name):
        """
        Returns the number of unique values and the unique values themselves for the specified column.

        Parameters:
        -----------
        col_name : str
            The name of the column.

        Returns:
        --------
        tuple
            A tuple containing the number of unique values and the unique values themselves, or None if the column doesn't exist.
        """
        if self._check_column_exists(col_name):
            unique_vals = self.properties_df[col_name].unique()
            return len(unique_vals), unique_vals
        return None

    def filth_be_gone(self, col_name, value):
        """
        Removes all rows containing the specified value from the given column.

        Parameters:
        -----------
        col_name : str
            The name of the column.
        value : any
            The value to remove from the column.

        Returns:
        --------
        None
        """
        if self._check_column_exists(col_name):
            self.properties_df = self.properties_df[self.properties_df[col_name] != value]

    def col_val_count(self, col_name):
        """
        Returns the count of each value present in the given column.

        Parameters:
        -----------
        col_name : str
            The name of the column.

        Returns:
        --------
        pandas.Series
            A Series containing the count of each unique value in the column, or None if the column doesn't exist.
        """
        if self._check_column_exists(col_name):
            return self.properties_df[col_name].value_counts()
        return None

    def summary_table(self, index_cols, summary_cols, operations):
        """
        Generates a summary table based on user-defined columns and operations.

        Parameters:
        -----------
        index_cols : list
            List of column names to create a multi-index.
        summary_cols : list
            List of column names to summarize.
        operations : list
            List of operations to perform on the summary columns (e.g., 'mean', 'mode', 'min').

        Returns:
        --------
        pandas.DataFrame
            The resulting summary DataFrame.
        """
        if self._check_column_exists(*index_cols, *summary_cols):
            summary_df = self.properties_df.groupby(
                index_cols)[summary_cols].agg(operations)
            return summary_df


if __name__ == "__main__":
    file_name = "realtor-data.csv"
    location = "./data"
    real_estate = RealEstate2(file_name, location)
    print(real_estate.properties_df.head())
    print("Data Types:\n", real_estate.check_type())
    # Number of null values in the specified column
    print("\nNumber of Nulls in 'bath':", real_estate.num_nulls('bath'))
    # Number of unique values and the unique values themselves for the specified column
    num_unique, unique_vals = real_estate.get_unique_vals('bath')
    print(f"\nNumber of Unique baths: {
          num_unique}\n {unique_vals}")
    # Filth_be_gone
    real_estate.filth_be_gone('city', 'Unknown')
    # Verify removal
    num_unique_after, _ = real_estate.get_unique_vals('city')
    print(f"Number of Unique Cities after removal: {num_unique_after}")
    # Get count of each value in 'city' column
    city_value_counts = real_estate.col_val_count('city')
    print("Count of each value in 'city' column:\n", city_value_counts)
    # Generate summary table
    index_columns = ['city', 'bed']
    summary_columns = ['house_size', 'price']
    operations = ['mean', 'min']
    summary_result = real_estate.summary_table(
        index_columns, summary_columns, operations)
    print("Summary Table:\n", summary_result)
    # Custom helper functions
    test_column = 'bed'
    if test_column not in real_estate.properties_df.columns:
        real_estate._handle_missing_column(test_column)
    else:
        percentage_above_mode_result = real_estate._percentage_above_mode(
            real_estate.properties_df[test_column])
        print(f"Percentage of values above mode in '{
              test_column}': {percentage_above_mode_result:.2f}%")
