# %% [markdown]
# # Week 6 Assignment - Pandas
#

# %%
import pandas as pd
import numpy as np


# %% [markdown]
# ### 1) Load the data into a pandas dataframe (you may get a warning, you can get rid of it by setting low_memory=False).
#
# ### Print the first 10 rows and print a random sampling of the rows in the dataframe.

# %%

def load_and_sample_data(file_path):
    """
    Loads data from a CSV file into a pandas DataFrame and prints the first 10 rows and a random sample of rows.

    Parameters:
    file_path (str): The path to the CSV file containing the realtor data.

    Returns:
    None
    """
    # Load the data into a pandas dataframe. Setting low_memory=False to avoid dtype warning due to mixed types in columns.
    df = pd.read_csv(file_path, low_memory=False)

    # Print the first 10 rows to get an initial understanding of the data.
    print("First 10 rows of the DataFrame:")
    print(df.head(10))

    # Print a random sampling of 10 rows to see diverse entries across the dataset.
    print("\nRandom sample of 10 rows from the DataFrame:")
    print(df.sample(10))


if __name__ == "__main__":
    # Define the path to the realtor-data.csv file
    data_file_path = 'data/realtor-data.csv'

    # Call the function to load and display data
    load_and_sample_data(data_file_path)

# %% [markdown]
# ### 2) You should always check how many null values there are in your data as well as the data types of the data you're working with. Often you will come across data that looks correct but isn't the right data type.
#
# ### Check the number of null values for every column and check the data types as well

# %%


def load_and_inspect_data(file_path):
    """
    Load the data from a CSV file into a pandas DataFrame, and inspect for null values
    and data types of each column.

    Parameters:
    - file_path: str, the path to the CSV file containing the realtor data.
    """
    # Load the data into a pandas DataFrame
    df = pd.read_csv(file_path, low_memory=False)

    # Null values check in each column
    null_values = df.isnull().sum()
    print("Number of null values in each column:")
    print(null_values)

    # Data types check of each column
    data_types = df.dtypes
    print("\nData types of each column:")
    print(data_types)


if __name__ == "__main__":
    # Function call to load the data and inspect for null values and data types
    load_and_inspect_data(data_file_path)

# %% [markdown]
# ### 3) We have 3 columns that looked right when checking the data but aren't the right data type and we'll correct it.
#
# ### Cast the columns bed, bath and price to float. Values that cannot be casted to float, like "hello" should be turned into NaN.
#
# ### Check the data types again to make sure the conversion was successfull.
#
#
#
# ### Get a count of the number of NaNs in bed, bath and price columns.
#
# ### You should get 216535, 194215 and 110 respectively
#
#

# %%


def clean_and_convert_types(df):
    """
    Clean and convert data types of specific columns in the dataframe.

    Parameters:
    - df: DataFrame, the pandas DataFrame containing the realtor data.
    """
    # Convert 'bed', 'bath', and 'price' to float, coercing errors to NaN
    for column in ['bed', 'bath', 'price']:
        df[column] = pd.to_numeric(df[column], errors='coerce')

    # Check the updated data types
    print("\nUpdated data types of each column:")
    print(df.dtypes)

    return df


def count_nan_values(df, columns):
    """
    Count the number of NaN values in specified columns of the DataFrame.

    Parameters:
    - df: DataFrame, the pandas DataFrame containing the realtor data.
    - columns: list of str, the columns in which to count NaN values.
    """
    nan_counts = df[columns].isnull().sum()
    return nan_counts


if __name__ == "__main__":
    # data_file_path = 'data/realtor-data.csv'
    df = pd.read_csv(data_file_path, low_memory=False)

# # Clean and convert data types for 'bed', 'bath', and 'price'
df = clean_and_convert_types(df)

# Get count of NaN values in 'bed', 'bath', and 'price' columns
nan_counts = count_nan_values(df, ['bed', 'bath', 'price'])
print("\nCount of NaN values in 'bed', 'bath', and 'price' columns:")
print(nan_counts)

# %% [markdown]
# ### 4) Check the number of unique values in the bed, bath and state columns.
#
# ### You should get 49, 42 and 19 respectively
#
# ### Print the uniques values for bed, bath and state. What do you notice about the unique values ?
#
# ### Ans. Further data cleaning steps may be needed to address outliers and anomalies in the bed and bath columns, such as removing or capping extreme values that do not align with typical residential property characteristics.
#

# %%


def check_unique_values(df, columns):
    """
    Check and print the number of unique values for specified columns in the DataFrame.

    Parameters:
    - df: pandas DataFrame, the DataFrame to analyze.
    - columns: list of str, the column names to check for unique values.

    Returns:
    - None
    """
    for column in columns:
        unique_values = df[column].unique()
        print(f"Number of unique values in {column}: {len(unique_values)}")
        print(f"Unique values in {column}: {unique_values}\n")


def handle_missing_values(df, columns):
    """
    Handle missing values in specified columns by dropping rows with NaN values.

    Parameters:
    - df: pandas DataFrame, the DataFrame to handle missing values.
    - columns: list of str, the column names to check for missing values.

    Returns:
    - df_cleaned: pandas DataFrame with missing values handled.
    """
    for column in columns:
        most_common_value = df[column].mode()[0]
        df[column].fillna(most_common_value, inplace=True)

    return df


if __name__ == "__main__":
    # Columns to check for unique values
    columns_to_check = ['bed', 'bath', 'state']
    columns_to_clean = ['bed', 'bath']

    # Handle missing values
    df_cleaned = handle_missing_values(df, columns_to_clean)

    # Check and print unique values
    check_unique_values(df_cleaned, columns_to_check)

# %% [markdown]
# ### 5) We want to see which state has the largest number of properties for sale.
#
# ### Print a count of the number of properties in each state/territory.
#
# ### We want to make sure that we're getting unique listings, so drop any duplicate rows and print the count of the number of properties. What do you notice about the number of properties in each state ?
#
# ### Ans.The stark differences in property counts between states, especially those with very few listings, raise questions about the dataset's quality and completeness. It might be necessary to investigate whether the dataset accurately reflects the real estate market or if there are gaps in the data collection process.

# %%


def count_properties_by_state(df):
    """
    Drop duplicate rows and count the number of properties in each state.

    Parameters:
    - df: DataFrame, the pandas DataFrame containing the realtor data.
    """
    # Drop duplicate rows to ensure unique listings
    unique_df = df.drop_duplicates()

    # Count the number of properties in each state
    properties_count = unique_df['state'].value_counts()
    print("Count of properties in each state/territory:")
    print(properties_count)


if __name__ == "__main__":
    # Count properties by state
    count_properties_by_state(df)

# %% [markdown]
# ### 6) We now want to look for patterns in our data, find the 5 dates when the most houses were sold. What do you notice ?
#
# ### Ans.The dates with the highest number of houses sold are relatively close together, all within a span of a few months. This could indicate a particularly active period in the real estate market.

# %%


def top_dates_most_houses_sold(df, num_dates=5):
    """
    Find the top dates when the most houses were sold.

    Parameters:
    - df: DataFrame, the pandas DataFrame containing the realtor data.
    - num_dates: int, the number of top dates to identify (default is 5).
    """
    # Convert 'prev_sold_date' to datetime format
    df['prev_sold_date'] = pd.to_datetime(df['prev_sold_date'])

    # Count the number of houses sold on each date
    top_dates = df['prev_sold_date'].value_counts().nlargest(num_dates)

    print(f"Top {num_dates} dates when the most houses were sold:")
    print(top_dates)


if __name__ == "__main__":
    # Find the top dates when the most houses were sold
    top_dates_most_houses_sold(df, num_dates=5)

# %% [markdown]
# ### 7) Now we want to create a simple but effective summary of the properties that are for sale.
#
# ### Let's create a summary table that contains the average home size and price, every state and each city within a state.
#
#

# %%


def create_summary_table(df):
    """
    Create a summary table with the average home size and price for each city within a state.

    Parameters:
    - df: DataFrame, the pandas DataFrame containing the realtor data.
    """
    # Ensure numeric columns are treated as such
    df['house_size'] = pd.to_numeric(df['house_size'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # Group by state and city, then calculate the mean of house_size and price
    summary_table = df.groupby(['state', 'city'])[
        ['house_size', 'price']].mean()

    print("Summary table of average home size and price for each city within a state:")
    print(summary_table)


if __name__ == "__main__":
   # Create the summary table
    create_summary_table(df)
