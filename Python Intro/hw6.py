'''
COMP 4401
Homework 6 - Lists & Tuples

General Homework Guidelines: 
- Do not use built-in functions
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
'''
#--------------------------------------------------------------------------#

# In this assignment we will be working with a Kaggle dataset 
# (https://www.kaggle.com/datasets/bryan2k19/dutch-house-prices-dataset). This is a real estate 
# dataset from the Netherlands. The data contains 16 columns and 5555 entries. 

# Our objective with this data is to import and analyze this data in order to help a family 
# member purchace a home in the Netherlands. They will be letting us sleep on their couch in 
# exchange for this service.



###---------------###
###-----Lists-----###
###---------------###

# 1. Create a function, called importData, that takes the file name as an argument. The function 
# must handle an exception when the file is not found (this occurs when the file does not exist, 
# if it was misspelled or it's in a different directory). If the exception is raised, the function 
# must ask the user to re-enter the file name and check again. 
# Repeat this as many times as needed until the data is read in. If the user enters nothing, the 
# function should terminate. The function should return the data that was read in, it should be of 
# type list, or return an empty list if the user terminated the function. 
# The output list should have length 5556 
# (10 points)

from collections import namedtuple
from hw6_functions import importData, castData, averageValues, filterByValues
from extra_functions import convert_sqm_to_sqft, convert_euros_to_dollars


def importData(file_name):
    """
    Imports data from a file, handles exceptions and returns it the data as a list..

    Args:
        file_name (str): The name of the file to o import data from..

    Returns:
        list: A list of the data imported from the file, or an empty list if the
              user terminates the function.
    """

    data = []

    # Keep trying to read the data until the user terminates or we succeed.
    while True:
        try:
            # Open the file and read the data.
            with open(file_name, "r") as file:
                data = file.readlines()

            # Check if the data has the expected length.
            if len(data) != 5556:
                raise ValueError(
                    f"Invalid data length ({len(data)}), expected 5556."
                )

            # Return the data if it is valid.
            return data
        except FileNotFoundError:
            # The file was not found. Prompt the user to re-enter the file name.
            print(
                f"File '{file_name}' not found. Please re-enter the file name:")
            file_name = input(
                "Enter the file name (or press Enter to terminate): ")

            # If the user enters nothing, terminate the function.
            if not file_name:
                break
        except ValueError:
            # The data is invalid. Print the error message and prompt the user to
            # re-enter the file name.
            print(f"Invalid data length, expected 5556.")
            print("Please re-enter the file name:")
            file_name = input(
                "Enter the file name (or press Enter to terminate): ")

            # If the user enters nothing, terminate the function.
            if not file_name:
                break

    # Return an empty list if the user terminated the function.
    return []

# 2. Create a function, called castData, that takes in the data read in by the previous function, 
# this should be a list of strings. The function should perform the following casts : 
# Price --> float
# Lot size (m2) --> float
# Living space size (m2) --> float
# Build year --> int
# The function should return the data after fixing the data types, this should be of type list.
# Be mindful of errors in the data, you will need to handle exceptions ! 
# Output list should have length 5438. 
# (10 points)


def castData(data):
    """
    Casts data to the specified data types, of a list of strings and handles exceptions.

    This function takes a list of strings as input, casts specific columns to the desired data types,
    and handles exceptions for data conversion errors.

    Args:
        data (list): A list of strings representing the data.

    Returns:
        list: A list containing the data with the specified data types, or an empty list if there are errors.
    """

    # Create an empty list to store the cleaned and casted data.
    cast_data = []

    for line in data:
        try:
            # Split the line into values.
            values = line.split(',')

            # Extract the columns and cast to the desired data types.
            price = float(values[0])
            lot_size_m2 = float(values[1])
            living_space_m2 = float(values[2])
            build_year = int(values[3])

            # Create a new line with the casted data.
            new_line = f"{price},{lot_size_m2},{living_space_m2},{build_year}"

            # Append the new line to the cleaned_data list.
            cast_data.append(new_line)

        except (ValueError, IndexError):
            # Handle data conversion errors or index errors.
            print("Error in data. Skipping this entry.")

    return cast_data


# 3. Create a function, called averageValues, that takes in a list. The list contains the price,
# lot size, living space and build year. The function must deal with missing values, keeping 
# track of the number of data points collected for each field (required for computing the average),
# and realistic data points for the year built column.
# The function should return a tuple containing the average home price, lot size, living space, 
# and build year for all homes. Your output should be :
# (557707.7581831556, 686.6248620816476, 146.34608311879367, 1968.9804836656767)
# (15 points)

def averageValues(data):
    """
    Calculates the average home price, lot size, living space, and build year for all homes in a list of lists.

    Args:
        data (list): A list of lists containing the price, lot size, living space, and build year for each home.

    Returns:
        tuple: A tuple containing the average home price, lot size, living space, and build year for all homes.
    """

    # Initialize variables to store the sums and counts for each field.
    price_sum = 0
    price_count = 0
    lot_size_sum = 0
    lot_size_count = 0
    living_space_sum = 0
    living_space_count = 0
    build_year_sum = 0
    build_year_count = 0

    # Iterate over the data and calculate the sums and counts for each field.
    for home in data:
        # Check if the price is missing.
        if home[0] is not None:
            price_sum += home[0]
            price_count += 1

        # Check if the lot size is missing.
        if home[1] is not None:
            lot_size_sum += home[1]
            lot_size_count += 1

        # Check if the living space is missing.
        if home[2] is not None:
            living_space_sum += home[2]
            living_space_count += 1

        # Check if the build year is missing and is within a realistic range.
        if home[3] is not None and 1900 <= home[3] <= 2023:
            build_year_sum += home[3]
            build_year_count += 1

    # Calculate the averages for each field.
    average_price = price_sum / price_count if price_count > 0 else 0
    average_lot_size = lot_size_sum / lot_size_count if lot_size_count > 0 else 0
    average_living_space = living_space_sum / \
        living_space_count if living_space_count > 0 else 0
    average_build_year = build_year_sum / \
        build_year_count if build_year_count > 0 else 0

    # Return the averages as a tuple.
    return (average_price, average_lot_size, average_living_space, average_build_year)


# 4. Create a function called filterByValues that takes in a list containing real estate 
# information, a minimum price and maximum price, these must be of type list, float and float 
# respectively. The function should return the average home price, lot size, living space, and 
# build year of all homes that fit between the minimum and maximum home values given. 
# Result should be returned as a tuple in the order price, lot size, living space, and build year.

# When function called with minPrice = 100000 and maxPrice = 400000, output should be:
# (324395.9323770492, 216.56045081967213, 110.17930327868852, 1966.869722557298) 
# (15 points)


def filterByValues(real_estate_info, minPrice, maxPrice):
    """
    Filters the given data by price and returns the average home price, lot size, living space, 
    and build year of all homes that fit between the minimum and maximum home values given.
    
    Args:
        real_estate_info (list): A list of real estate information where each entry contains
            price, lot size, living space, and build year.
        minPrice (float): The minimum price for filtering homes.
        maxPrice (float): The maximum price for filtering homes.

    Returns:
        tuple: A tuple containing the average home price, lot size, living space, and build year
            for homes within the specified price range.
    """

    # Create a filtered list with homes within the specified price range.
    filtered_data = [
        (price, lot_size, living_space, build_year)
        for price, lot_size, living_space, build_year in real_estate_info
        if minPrice <= price <= maxPrice
    ]
    # Use the previously implemented averageValues function to calculate average values for each field.
    average_values = averageValues(filtered_data)
    
    return average_values



###----------------###
###-----Tuples-----###
###----------------###


# 5. Write a function, called minMaxTuple, that takes a list of numbers and returns 
# the smallest element and the largest element as a tuple (smallest, largest). Cannot 
# use the built-in functions min()/max().
# For example : lst = [6, 3, 8, 23, -4, 35] should return (-4, 35) 
# (10 points)
import math

def minMaxTuple(lst):
    """
    Finds the smallest and largest elements in a list 
    of numbers without using the built-in min() and max() functions..

    Args:
        lst (list): A list of numbers.

    Returns:
        tuple: A tuple containing the smallest and largest elements in the list.
    """
    if not lst:
        # Handles the case where the list is empty.
        return None

    # Initialize the smallest and largest elements to math.inf and -math.inf, respectively.
    smallest = math.inf
    largest = -math.inf

    # Compares each element to the smallest and largest elements.
    for num in lst:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    # Returns the smallest and largest elements as a tuple.
    
    return (smallest, largest)


if __name__ == '__main__':
    lst = [6, 3, 8, 23, -4, 35]
    result = minMaxTuple(lst)
    print(result)  # Output: (-4, 35)


# 6. Write a function, called allPairs, that takes two lists as paramters, x and y, 
# and returns a new list containing all possible pairs consisting of one element from 
# x and one element from y as long as they are not the same. Cannot use built-in 
# functions or sets.
# For example: If the list x = [1, 4, 6, 8] and y = [5, 2, 6] then the result is the list 
# [(1, 5), (1, 2), (1, 6), (4, 5), (4, 2), (4, 6), (6, 5), (6, 2), (8, 5), (8, 2), (8, 6)]. 
# Note that (6, 6) doesn't appear because they are the same element. 
# (15 points)

def allPairs(x, y):
    """
    Generates all possible pairs from two lists, avoiding same-element pairs.

    Args:
        x (list): The first list.
        y (list): The second list.

    Returns:
        list: A list containing all possible pairs, excluding same-element pairs.
    """
    pairs = []   # Create a new list to store the pairs.

    for element_x in x:   # Iterate over the first list.
        for element_y in y:  # Iterate over the second list.
            # If the two elements are not the same, add them to the list of pairs.
            if element_x != element_y:
                pairs.append((element_x, element_y))

    # Return the list of pairs.
    return pairs


if __name__ == '__main__':
    # Example usage:
    x = [1, 4, 6, 8]
    y = [5, 2, 6]
    # Generate all possible pairs of elements from the two lists.
    pairs = allPairs(x, y)
    print(pairs) # Output: [(1, 5), (1, 2), (1, 6), (4, 5), (4, 2), (4, 6), (6, 5), (6, 2), (8, 5), (8, 2), (8, 6)]


# 7. Write a function, called removeDups, that takes a list of tuples and removes any 
# duplicate tuples and returns the modified list. Cannot use built-in functions nor 
# sets.
# For example if the list contains [(1, 2), (1, 4, 5), (1, 2), (3, 5)] then the list 
# will become [(1, 2), (1, 4, 5), (3, 5)]. 
# (10 points)

def removeDups(list_of_tuples):
    """
    Removes duplicate tuples from a list of tuples without using built-in functions or sets..

    Args:
        tuple_list (list): A list of tuples.

    Returns:
        list: The modified list with duplicate tuples removed.
    """
    # Create a new list to store the tuples with no duplicates.
    variable_tuples = []

    for tuple in list_of_tuples:
        # Check if the tuple is already in the list of variable tuples.
        if tuple not in variable_tuples:
            # If the tuple is not in the list of variable tuples, add it to the list.
            variable_tuples.append(tuple)
    # Return the list of variable tuples.
    return variable_tuples


if __name__ == '__main':
    list_of_tuples = [(1, 2), (1, 4, 5), (1, 2), (3, 5)]
    variable_tuples = removeDups(list_of_tuples)
    print(variable_tuples)  # Output: [(1, 2), (1, 4, 5), (3, 5)]


# 8. Create a function, called resultTuples, which takes a location as an argument, this
# should be of type str. The function will create namedtuples named realEstate. Each 
# namedtuple should have the fields : 
# Location, CheapestBuyPrice, AvgBuyPrice and MostExpBuy. 
# To create each tuple you will need to make function calls to our previously defined
# functions in this homework. Also keep in mind that  The function must return the namedtuple created.

# Note1: You will also need to convert the units from sqmt to sqft and euros to 
# dollars using the functions from previous homeworks.
# Note2: You will need to place those functions in the extra_functions.py file and
# import them to use them as we've done in the past.
# Note3: You may need to modify our previously used functions so they work with our
# data.

# Output should look like this :
# (the location can change, I used Madrid as an example, numerical values are correct) :
# realEstate(Location='Madrid', CheapestPrice=149000.0, AvgPrice=557707.7581831556, MostExp=4700000.0)
# (15 points)


def resultTuples(location):
    """
    Creates a namedtuple named realEstate with the fields Location, CheapestBuyPrice, AvgBuyPrice, and MostExpBuy for the given location.

    Args:
        location (str): The location for the named tuple.

    Returns:
        namedTuple: A named tuple with the specified fields.
    """
    # Import from hw6 data file and process the data.
    file_name = f"{location}_hw6_data.csv"
    data = importData(file_name)
    if not data:
        return None  # Return None if data is empty or not found.

    # Cast data and convert units.
    casted_data = castData(data)
    converted_data = [convert_sqm_to_sqft(
        casted_data[0]), casted_data[1], casted_data[2], casted_data[3]]

    # Calculate cheapest, average, and most expensive buy prices.
    minPrice = 70000  # Both min and max prices can be adjusted as needed.
    maxPrice = 200000
    filtered_data = filterByValues([converted_data], minPrice, maxPrice)
    cheapest_price, _, _, most_expensive_price = averageValues(filtered_data)

    # Convert the prices from euros to dollars
    cheapest_price = convert_euros_to_dollars(cheapest_price)
    filtered_data[0][0] = convert_euros_to_dollars(filtered_data[0][0])
    most_expensive_price = convert_euros_to_dollars(most_expensive_price)

    # Create a named tuple.
    realEstate = namedtuple(
        "realEstate", ["Location", "CheapestBuyPrice", "AvgBuyPrice", "MostExpBuy"])

    # Return the named tuple.
    return realEstate(Location=location, CheapestBuyPrice=cheapest_price, AvgBuyPrice=filtered_data[0][0], MostExpBuy=most_expensive_price)

if __name__ == '__main__':  
    location = "Madrid"  # Replace with the desired location.
    real_estate_madrid = resultTuples(location)
    print(real_estate_madrid)

