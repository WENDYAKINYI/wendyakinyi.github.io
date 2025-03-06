'''
COMP 4401
Homework 3 - Control Flow Statements

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
'''
#--------------------------------------------------------------------------#

# 1. Create a function distanceConversion that takes in two parameters, distance and unit, 
# of types float and string respectively. Based on the unit type, "metric" or "imperial", it 
# will convert distance into miles or kilometers. This is creating a single function from 
# milesToKm and kmToMiles in the last homework. (10 points)

def distanceConversion(distance, unit):
    '''
    -Converts distance based on unit type, metric or imperial.

    -Parameters:
    distanceI (float): Distance value to be converted.
    unit (str): specifies the input distance either in "metric" or "imperial".

    -Returns:
    float: Converted distance value. In "miles" or "kilometers"
    '''
    # if distance is in "imperial" (miles to kilometers) conversion
    if unit == "imperial":
        kilometers = distance * 1.60934
        return kilometers
    # if distance is in "metric" (kilometers to miles) conversion
    elif unit == "metric":
        miles = distance * 0.621371
        return miles
    else:
        return "Not applicable. Please input 'imperial' or 'metric'."

# Example
distanceInKm = 10
distanceInMiles = 62.08
distanceConverted = distanceConversion(distanceInMiles, "imperial")
print(f"{distanceInMiles} miles is equal to {distanceConverted} kilometers")

distanceConverted = distanceConversion(distanceInKm, "metric")
print(f"{distanceInKm} kilometers is equal to {distanceConverted} miles")

# 2. Create a function called brickPath that takes three parameters: wallLength, smallBricks, and largeBricks.
# You want to make a row of bricks that is wallLength inches long with the given length of the small and large 
# bricks. Return 'Possible' if it is possible to make the goal by choosing from the given bricks. Otherwise 
# return 'Not Possible'. Small bricks are 1 unit long and large bricks are 5 units long.

# For example: 
# If wallLength = 8, smallGBricks = 2, largeGBricks = 3 then it’s not possible because there is no way 
# to get 8 inches using the given bricks. 
# On the other hand, wallLength = 7 with smallBricks = 2 and largeBricks = 3 is possible (1 large and 2 small 
# gives you 7). (15 points)

def brickPath(wallLength, smallBricks, largeBricks):
    '''
    -Determines if it is possible to make a row of bricks that is wallLength inches long with the given length of the small and large bricks
    
    -Parameters:
    wallLength (int): Length of wall in inches
    largeBricks (int): available number of large bricks(5 units long)
    smallBricks (int): available number of small bricks (1 unit long)

    -Returns:
    str: 'possible' to create a wall with provided number of bricks, otherwise 'not possible'
       
    '''
    # Calculating the total number of large bricks that can be used, including the parameter largeBricks
    usable_large_bricks = min(wallLength // 5, largeBricks)
    
    # Trying out different combinations of large and small bricks
    for num_large_bricks in range(usable_large_bricks + 1):
        # Remaining length after using large bricks
        remaining_length = wallLength - (num_large_bricks * 5)
        
        # Looking to get enough small bricks to complete the wall
        # If the remaining length is less than or equal to the number of small bricks available, then return 'Possible'
        if remaining_length <= smallBricks:
            return 'Possible'
    
    # If the available bricks cannot complete the wall, return 'Not Possible'
    return 'Not Possible'

# Example 
wallLength = 8
smallBricks = 2
largeBricks = 3
output = brickPath(wallLength, smallBricks, largeBricks)
print(output)  # Output: 'Not Possible'

wallLength = 7
smallBricks = 2
largeBricks = 3
output = brickPath(wallLength, smallBricks, largeBricks)
print(output)  # Output: 'Possible'

# 3. Write a function, called calcSum, that takes 3 integer values as arguments: a, b and c. The function 
# must return their sum. However, if one of the values is a duplicate, the duplicate value does not count 
# towards the sum. You cannot use the built-in method sum().
# For example 2, 4, 5 returns 11. The inputs 2, 2, 5 returns 7 and the inputs 1, 1, 1 returns 1. (10 points)

def calcSum(a, b, c):
    '''
    -Calculates the sum of three integer values, excluding duplicates

    -Parameters:
    a (int): first integer value
    b (int): second integer value
    c (int): third integer value

    -Returns:
    int: the sum of the three integer values excluding repeated values

    '''
    # checking for duplicates and removing them
    if a == b == c:
        return a
    elif a == b:
        return a + c
    elif b == c:
        return a + b
    elif a == c:
        return b + c
    else:    #if there are no duplicates, return the sum of all three values
        return a + b + c

# Example
print(calcSum(2, 4, 5))  # Output: 11
print(calcSum(2, 2, 5))  # Output: 7
print(calcSum(1, 1, 1))  # Output: 1

# 4. Create a function that takes in 4 parameters, intVal, strVal, floatVal, and floatVal2. Check that each 
# parameter is of the corresponding type, int, string, float and float respectively. If their data type does 
# not match these types, cast them to the right data type. Then return all 4 values as a tuple. (10 points)

def check_types(intVal, strVal, floatVal, floatVal2):
  '''
    -Check the data types of input parameters and cast them to the correct types if required.

    -Parameters:
    intVal: The input value expected to be an integer or castable to an integer.
    strVal: The input value expected to be a string.
    floatVal: The input value expected to be a float or castable to a float.
    floatVal2: The input value expected to be a float or castable to a float.

    -Returns:
    tuple: A tuple containing the four values after data type checks and casting.
    
    '''
  # Check the data type of intVal and convert to an integer if necessary.
  if not isinstance(intVal, int):
    intVal = int(intVal)

  # Check the data type of strVal and convert to a string if necessary.
  if not isinstance(strVal, str):
    strVal = str(strVal)

  # Check the data type of floatVal and convert to a float if necessary.
  if not isinstance(floatVal, float):
    floatVal = float(floatVal)

  # Check the data type of floatVal2 and convert it to a float if necessary.
  if not isinstance(floatVal2, float):
    floatVal2 = float(floatVal2)
    
  # Return all values as a tuple
  return intVal, strVal, floatVal, floatVal2

#Example
# here is a tuple of values, can be changed
values = (20, "Hello", 2.2, 3.142)

# Checking the data types of the values and cast them to the correct type if necessary.
checked_values = check_types(*values)

# Print the checked values.
print(checked_values) # output is a tuple with values(20, 'Hello', 2.2, 3.142)

# 5. Create a function, called change, that takes an input, cash (a float), and determines 
# the least number of dollar bills and coins needed for change. Note that bills are: 1, 5, 10, 20, 50, and 100.
# Coins can be: 1 cent, 5 cents, 10 cents and 25 cents (penny, nickel, dime, quarter). (15 points)
# Example:
# If the dollar amount is 35.63, then your function should return the string:
# "1 x $20 bill, 1 x $10 bill, 1 x $5 bill, 2 quarters, 1 dime, 3 pennies"

def change(cash):
    '''
    -Determines the least number of dollar bills and coins needed for change.

    -Parameters:
    cash (float): The amount of cash for which change needs to be calculated.

    -Returns:
    str: A string describing the least number of dollar bills and coins needed for change.
     
    '''
    # bills and coins denominations
    denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
    # bills and coins names
    names = ["$100 bill", "$50 bill", "$20 bill", "$10 bill", "$5 bill", "$1 bill",
             "quarters", "dimes", "nickels", "pennies"]
    # counts of each denomination
    counts = [0] * len(denominations)
    
    # trying out each denomination to calculate the number of bills/coins needed
    for k in range(len(denominations)):
        if cash >= denominations[k]:
            counts[k] = int(cash // denominations[k])
            cash -= counts[k] * denominations[k]
    
    # Create a list of formatted strings for each denomination with its count
    result_strings = [f"{counts[k]} x {names[k]}" for k in range(len(counts)) if counts[k] > 0]
    
    # Join the result strings with commas and return the result
    return ", ".join(result_strings)

# Example usage:
cash_amount = 35.63   #amount can be changed
result = change(cash_amount)
print(result)  # Output: "1 x $20 bill, 1 x $10 bill, 1 x $5 bill, 2 x quarters, 1 x dime, 3 x pennies"

# 6. Create a function, called bottlesOfBeer, that accurately prints the “99 bottles of beer on the wall” song: 
# http://www.99-bottles-of-beer.net/lyrics.html
# Your program should account for changes in plural vs. singular nouns and should count down from 99 to 0. 
# (10 points)

def bottlesofBeer(numberOfBottles):
  '''
    -Prints the "99 bottles of beer on the wall" song, counting down from the given number of bottles.

    -Parameters:
    numberOfBottles: The initial number of bottles of beer.

    -This function takes an initial number of bottles as input and prints the lyrics of the song,
    counting down from the initial number of bottles until there are no more bottles left on the wall.
    -It correctly handles the singular and plural forms of "bottle" based on the number of bottles.
    
  '''
  while numberOfBottles > 0:
    # Determine the plural form of "bottle" based on the number of bottles.
    bottlePlural = "bottles" if numberOfBottles > 1 else "bottle"

    # Print the first verse of the song.
    print(f"{numberOfBottles} {bottlePlural} of beer on the wall, {numberOfBottles} {bottlePlural} of beer.")
    print("Take one down and pass it around,")

    # Decrease the number of bottles by one.
    numberOfBottles -= 1

    # Determine the new plural form of "bottle" based on the new number of bottles.
    bottlePlural = "bottles" if numberOfBottles > 1 else "bottle"

    # when there are no more bottles, print the following line.
    if numberOfBottles == 0:
      print("No more bottles of beer on the wall, no more bottles of beer.")
      print("Go to the store and buy some more, 99 bottles of beer on the wall.")
    else:
            # Print the next line of the song.
            print(f"{numberOfBottles} {bottlePlural} of beer on the wall.")


# Example usage:
bottlesofBeer(99) #output; 99 bottles of beer on the wall, 99 bottles of beer.
                  #Take one down and pass it around, 98 bottles of beer on the wall.


# 7. Check age and height (15 points)

def checkAgeHeight(age, height):
    '''
    -Checks if a person is old enough and tall enough to get on a ride.

    -Parameters:
        age (int):  the age of the ride customer.
        height (int): the actual height of the customer in inches.

    -Prints:
        - "You're old enough to get on the ride" if age is greater than 12.
        - "You can get on the ride. Enjoy!" if age is greater than 12 and height is greater than 54.
        - "You're a bit too short, sorry." if age is greater than 12 but height is not greater than 54.
        - "Too young" if age is not greater than 12.
    
    '''
    if age > 12:
        print("You're old enough to get on the ride")
        if height > 54:
            print("You can get on the ride. Enjoy!")
        else:
            print("You're a bit too short, sorry.")
    else:
        print("Too young")

# Example
age = 15  # to be replaced with the actual age of the ride customer
height = 60  # to be replaced with the actual height of the ride customer
checkAgeHeight(age, height)
#output: #You're old enough to get on the ride, 
         # You can get on the ride. Enjoy!

# 8. Debug the following code (15 points):
def changeNumber(myNum, myType):
  '''
  -This function will change a number from int to float or float to int
  
  -Parameters:
  myNum (int/float): input number
  myType (int/float): the type we want to get back
  
  -Returns:
      myNum but with correct type, "int" else "float"
  
  '''
  if myType == int:
    return int(myNum)
  else:
    return float(myNum)













