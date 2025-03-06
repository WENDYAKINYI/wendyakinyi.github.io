'''
COMP 4401
Homework 5 - File Input/Output & Exception Handling

General Homework Guidelines: 
- Homework must be submitted in a .py file. Please do not submit .ipynb files.
- Homework should not use packages or functions that have not yet been discussed in class.
- Use comments to explain what your code is doing. 
- Use a consistent coding style. 
- Use descriptive variable names.
- Test your code regularly using a variety of different inputs. 
- Every function must include a docstring for documentation (see: 
   https://realpython.com/documenting-python-code/). This docstring should include:
     - 1 or 2 lines describing what the function does
     - input parameters, their types and what they are for
     - return data type and what it is
- All tests of your functions should be commented out in your final submission or
  encolosed with an if __name__ == '__main__' codeblock.
- All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.



In this assignment we will be working with a Kaggle dataset 
(https://www.kaggle.com/datasets/bryan2k19/dutch-house-prices-dataset)
(https://www.kaggle.com/datasets/mirbektoktogaraev/madrid-real-estate-market). 
This is a real state dataset from the Netherlands and Madrid, Spain. The data 
contains 16 columns with 5555 entries and 58 columns with 21.7k entries respectively.
We will be working with a subset of the data split into multiple files. 

Our objective with this data is to import and analyze this data in order to help a family 
member purchace a home in the Netherlands/Madrid. They will be letting us sleep on their 
couch in exchange for this service. A fair trade.
'''
# --------------------------------------------------------------------------#


# 1. Create a function, called inputData, that takes a file name as an argument.
# The function must handle an exception if the file is not found (this occurs
# when the file does not exist, if it was misspelled or it's in a different
# directory). The function must read in the data from the file and return it
# as a list.
# (15 points)
import os  # Import the os module to check if the file exists
from helper_functions import convert_euros_to_dollars, convert_sqmt_to_sqft
import csv


def inputData(file_name):
    """
    Reads in data from a file and returns it as a list.

    Args:
        file_name (str): The name of the file to read from.

    Returns:
        list: A list of the data in the file.

    Raises:
        FileNotFoundError: If the specified file is not found.
    """
    try:
        with open(file_name, "r") as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        print(f"File {file_name} not found")
        return []


# Example usage:
if __name__ == '__main__':
    file_name = "buyPriceMadrid.csv"  # To be replaced with the actual file name
    data = inputData(file_name)
    if data:
        print(data)


# 2. Create a function, called listOfFloats, that takes a list of values and casts
# each value to a float. The function must be able to handle exceptions dealing with
# missing values and values that cannot be cast to a float, i.e. "fdshjksd". The
# function must return a list of floats. Note: you must create an empty list inside
# the function, and append the casted values to it, then return it.
# (15 points)

def listOfFloats(values):
    """
    Casts a list of values to floats, handling exceptions for missing values
    and values that cannot be cast to a float.

    Args:
        values (list): A list of values to be cast to floats.

    Returns:
        list: A float list

    """
    float_list = []

    for value in values:
        try:
            if value != "missing":  # Handles exceptions dealing with missing values
                float_value = float(value)  # casts the value to a float
                # appends the cast value to the float list
                float_list.append(float_value)
        except (ValueError, TypeError):
            # Handles exceptions dealing with values that cannot be cast to a float
            pass

    return float_list


# Example usage:
if __name__ == '__main__':
    values = ["1.23", "4.56", "7.89", "missing", "fdshjksd"]
    float_values = listOfFloats(values)
    print(float_values)


# 3. Create a function, called computeAverage, that takes in a list of floats as an
# argument. All elements in the list must be floats in order to perform any calculations.
# You cannot use any built-in function to compute the average, instead add up all the
# values and divide by the total number of values you have. Return the average (this
# should be a float).
# (15 points)

def computeAverage(float_values):
    """
    Computes the average of a list of float values, without using any built-in functions.


    Args:
        float_values (list): A list of float values.

    Returns:
        float: The average of the float values.
    """
    if not float_values:
        return 0.0

    sum_of_floats = 0.0
    for value in float_values:
        sum_of_floats += value

    average = sum_of_floats / len(float_values)
    return average


# Example usage:
if __name__ == '__main__':
    float_values = [3.14, 15.63, 1.89]
    average = computeAverage(float_values)
    print(average)


# 4. Create a function, called filteredData, that takes filename and maxPrice as arguments,
# of types string and float respectively. The function should loop over the list and store the
# results that satisfy the maxprice criteria in a new list (amount is <= maxPrice).
# (use :
# filteredResults = []
# filteredResults.append(filteredDataPoint) to add the data to the new list).
# Return the list with the new results. The function must handle the exception of getting an
# incorrect max value, i.e. "bjfdsk".
# (15 points)

def filteredData(filename, maxPrice):
    """
    Filters the data in a file based on a maximum price.

    Args:
        filename (str): The name of the file to read from.
        maxPrice (float): The maximum price.

    Returns:
        list: A list containing the filtered results.

    Raises:
        ValueError: If maxPrice is not a valid float value.
    """
    filteredResults = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    result = float(line.strip())
                    if result <= maxPrice:
                        filteredResults.append(result)
                except ValueError:
                    # Handle incorrect data points that cannot be cast to float
                    pass
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except ValueError:
        print(f"Invalid maxPrice value: {maxPrice}")

    return filteredResults


# Example usage:
if __name__ == '__main__':
    file_name = "buyPriceNetherlands.csv"  # Replace with the actual file name
    max_price = 7000000.0  # Replace with the desired max price
    results = filteredData(file_name, max_price)
    if results:
        # Process the filtered results here
        print(results)


# 5. Create a function, called realStateAnalysis, that takes a location, type string. The
# function must ask the user for the file names for buy prices, living space and rent prices
# whilst handling the file not found error (there is a clever to do this).

# The function must ask the user to enter a file name until they entered a valid file name.
# Note: the file names must have the extension .csv to work

# The function must then compute the average buy price, average rent price and average living
# space. Perform checks on your data as the data may not be very clean (you should expect
# missing values and negative values. You must deal with them).

# Write the results in a file called : realStateAnalysis.csv using the following format :
# Location, Avg_buy_price, Avg_rent_price, Avg_sqft

# Note 1: the living space is in square meters, rent and buy prices are in euros, so create
# a second file, helper_functions.py and use our previously defined function to convert sqmt
# to sqft and euros to dollars (you may need to modify the function to make it work).
# Note 2: You must also use whichever functions created in this homework to accomplish this task.
# Note 3: You will need to call the function twice, once for the data for Madrid and another for
# the Netherlands
# The output for the function should look like this :
# Madrid, 578091.9661429492, 1434.4682101167316, 883.9385353229587
# Netherlands, 602963.3547672321, 3014.7843377841937, 1576.2050598919893
# (40 points)


def realStateAnalysis(location):
    """Analyzes real estate data for a specific location.

    Args:
        location (str): The location (e.g., "Madrid" or "Netherlands").

    Returns:
        None. The function computes averages and writes the results to realStateAnalysis.csv.
    """
    # Create lists to store data
    buy_prices = []
    rent_prices = []
    living_space = []

    # Ask the user for file names and handle file not found error
    while True:
        try:
            buy_file = input(
                f"Enter the file name for buy prices in {location}: ")
            with open(buy_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                buy_prices = [float(row[0]) for row in reader]
            break
        except FileNotFoundError:
            print(
                f"File '{buy_file}' not found. Please enter a valid .csv file.")

    while True:
        try:
            rent_file = input(
                f"Enter the file name for rent prices in {location}: ")
            with open(rent_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                rent_prices = [float(row[0]) for row in reader]
            break
        except FileNotFoundError:
            print(
                f"File '{rent_file}' not found. Please enter a valid .csv file.")

    while True:
        try:
            space_file = input(
                f"Enter the file name for living space in {location}: ")
            with open(space_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                living_space = [float(row[0]) for row in reader]
            break
        except FileNotFoundError:
            print(
                f"File '{space_file}' not found. Please enter a valid .csv file.")

    # Check data and handle missing/negative values
    buy_prices = [price for price in buy_prices if price > 0]
    rent_prices = [price for price in rent_prices if price > 0]
    living_space = [space for space in living_space if space > 0]

    # Compute averages
    avg_buy_price = sum(buy_prices) / len(buy_prices) if buy_prices else 0
    avg_rent_price = sum(rent_prices) / len(rent_prices) if rent_prices else 0
    avg_living_space = sum(living_space) / \
        len(living_space) if living_space else 0

    # Create or modify the realStateAnalysis.csv file
    filename = 'realStateAnalysis.csv'
    header = ["Location", "Avg_buy_price", "Avg_rent_price", "Avg_sqft"]

    # Check if the file already exists
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='') as result_file:
        writer = csv.writer(result_file)

        # If the file doesn't exist, write the header row
        if not file_exists:
            writer.writerow(header)

        # Write the data for the current location
        writer.writerow(
            [location, avg_buy_price, avg_rent_price, avg_living_space])


if __name__ == "__main__":
    realStateAnalysis("Madrid")
    realStateAnalysis("Netherlands")
