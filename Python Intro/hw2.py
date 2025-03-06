'''
COMP 4401
Homework 2 - Functions & Variable Scope

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
  enclosed with an if __name__ == '__main__' codeblock.
- All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.

Homework 2 Instructions:
You should submit two .py files, this file and a new file you create for problem 6 called : extra_functions.py.

'''
# --------------------------------------------------------------------------#
from extra_functions import midpoint

# 1. Create a function called secondsToHMS that takes an argument `seconds`,
# an integer number of seconds, and returns a string in the format "xx h, xx m, xx s",
# where xx is the number of hours, minutes and seconds. This is turning the question
# from last week's homework into a function. (15 points)


def secondsToHMS(seconds):
    '''
    -Function that converts seconds into a string in the format "xx h, xx m, xx s".

    -Parameters:
    seconds (int): Number of seconds

    -Returns:
    str: Formatted time string
    '''

    # number of hours, minutes, and remaining seconds calculation
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    # formatted time string
    time_str = f"{hours} h, {minutes} m, {seconds} s"

    return time_str


# Example
seconds = 9432  # use any number (int) of seconds for testing
formatted_time = secondsToHMS(seconds)
print("Formatted time:", formatted_time)

# 2. Create two functions milesToKm and kmToMiles, each function will take in one
# parameter, distance, of type float. Each function will convert the distance into
# either miles or kilometers based on the function used and return that value.
# (15 points)
# 1 mile = 1.6 kilometers
# 1 kilometer = 0.62 miles


def milesToKm(distanceInMiles):
    '''
    -Converting miles to kilometers.
    1 mile = 1.6 kilometers

    -Parameters:
    distanceInMiles (float): Distance in miles

    -Returns:
    float: Equivalent distance in kilometers
    '''
    return distanceInMiles * 1.6


def kmToMiles(distanceInKm):
    '''
    -Converting kilometers to miles
    1 kilometer = 0.62 miles

    -Parameters:
    distanceInKm (float): Distance in kilometers

    -Returns:
    float: Equivalent distance in miles
    '''
    return distanceInKm * 0.62


# Example
miles = 40  # use any number of miles(float) for testing
kilometers = 86  # use any number of kilometers(float) for conversion

# Convert miles to kilometers
converted_kilometers = milesToKm(miles)
print(f"{miles} miles is equivalent to {converted_kilometers} kilometers")

# Convert kilometers to miles
converted_miles = kmToMiles(kilometers)
print(f"{kilometers} kilometers is equivalent to {converted_miles} miles")

# 3. Create a function called europeUS that takes 2 parameters, sqmToSqft and euroToDollars,
# both of type float. The function must return the coverted values as a tuple: sqft, dollars.
# This will allow us to convert real state listings in Europe, which are in metric, to imperial
# units so we can shop for our next vacation home. (10 points)
# 1 sqm = 10.7639 sqft
# 1 euro = 1.08 dollars

# def function(....):
# ...
# ...
# return val1, val2
#
# result1, result2 = function(...)


def europeUS(sqmToSqft, euroToDollars):
    '''
    -Converting square meters to square feet and Euros to Dollars.

    -Parameters:
    sqm (float): square meters
    sqft (float): square feet
    dollar (float): dollars
    euro (float): Euros

    -Returns:
    tuple: sqft, dollars
    '''
    # Conversion
    sqft = sqmToSqft * 10.7639
    dollars = euroToDollars * 1.08

    return sqft, dollars


# Example
sqm_area = 1000.0  # use the actual square meter area
euro_price = 22345.0  # use with the actual price in euros

sqft_area, usd_price = europeUS(sqm_area, euro_price)
print(f"{sqm_area} sqm is equal to {sqft_area:.2f} sqft.")
print(f"{euro_price} euros is equal to ${usd_price:.2f}.")


# 4. Create a function called roadTrip that takes 1 parameter, mpg (miles per gallon), of type float.
# The function should ask for user input on how far they intend to drive on their road trip. Once
# you have the distance, calculate the number of gallons they will need to complete the road trip.
# Use $3.07 as the average cost of a gallon of gas. Return the total cost of gas for the road trip.
# (15 points)


def roadTrip(mpg):
    '''
    -Calculates the total cost of gas for a road trip.

    -Parameters:
    mpg (float): Miles per gallon

    -Returns:
    float: Total cost of gas for the road trip
    '''
    # Drive distance
    distance = float(input("Enter the distance of your road trip in miles: "))

    # gallons required
    gallons_required = float(distance / mpg)

    # Average cost of a gallon of gas
    cost_per_gallon = 3.07

    # Calculate the total cost of gas
    total_cost = gallons_required * cost_per_gallon

    return total_cost


# Example usage:
mpg = 80.0  # change miles per gallon depending on customers vehicle model

total_gas_cost = roadTrip(mpg)
print(f"Total cost of gas for the road trip: ${total_gas_cost:.2f}")


# 5. Create a function called insulateHomeCost that takes no parameters and asks the user to input
# the length, width and height of the the basement of their house. Once you have these values,
# calculate the surface area (sq ft) of each side of the basement and use $2.75 as the average cost
# of spray foam insulation per sq ft. Once you have that value multiply. Return the total insulation
# cost. (15 points)

def insulateHomeCost():
    '''
    Total insulation cost of a basement.

    Returns:
    float: Total insulation cost
    '''
    # basement dimensions
    length = float(input("Enter the length in (feet): "))
    width = float(input("Enter the width in (feet): "))
    height = float(input("Enter the height in (feet): "))

    # surface area of the sides
    surface_area = 2 * (length * height + width * height)

    # Average cost of spray foam insulation per sq ft
    insulation_cost_per_sqft = 2.75

    # total insulation cost
    total_cost = surface_area * insulation_cost_per_sqft

    return total_cost


# Example usage:
total_insulation_cost = insulateHomeCost()
print(
    f"The total insulation cost for the basement will be: ${total_insulation_cost:.2f}")

# 6. We're going to practice importing functions from another file. Complete the following steps:
#  - Create a new .py file called extra_functions.py
#  - In extra_functions.py, write a function called midpoint which takes an integer as input and returns
#    the midpoint between that integer and 0.
#  - Include an if __name__ == '__main__' codeblock in extra_functions.py to test your midpoint function.
#  - Import extra_functions.py into this file.
#  - Run this line of code: midpoint_of_10 = midpoint(10)
# (20 points)


# Import extra_functions.py into this file.
# Calculate the midpoint of 10
midpoint_of_10 = midpoint(10)

# Line of code
print(f"The midpoint of 10 is {midpoint_of_10}")


# 7. Fix the following code (10 points)

def calc_bmi(height, weight, age):
    '''
    This function calculates the Body Mass Index (BMI).

    Parameters:
    height (float): Height in feet
    weight (float): Weight in pounds
    age (int): Age in years

    Returns:
    float: BMI value
    '''

    # BMI calculation formula
    bmi = weight / (height**2) * 703

    return bmi


# Example usage:
height = 5.8  # use any number value in feet
weight = 160  # use any number value in pounds
age = 30  # use any number value in years

bmi_outcome = calc_bmi(height, weight, age)
print("Your BMI is:", bmi_outcome)
