# COMP 4401
# Homework 1 - Variables & Boolean Expressions

# Submit homework 1 responses in a single .py file. Responses to questions 1-4 can be included in Python script files using line comments (# comment) or multiline comments using triple quotes (‘’’comment’’’).

# For questions 1-4 solve without using python to ensure you understand data types and boolean expression, you can then verify your answers using python.

# --------------------------------------------------------------------------#

# 1. For each of the following expression, identify the data type and value (10 points):
# A) 5+3/5*(4-10)
# Using BODMAS
# (4-10)=-6
# 3/5=0.6
# 0.6*-6=-3.6
# 5+(-3.6)=1.4
# A= Float, Since the value 1.4 Which has a fractional component

# B) 17//3**4
# 3**4=81
# 17//81=0
# B=Integer, since the value is 0 having used (//) integer division.

# 2. Evaluate the following boolean expressions (10 points):
# A) 15 % 4 < 20/3
# 15 % 4 = 3
# 20/3 = 6.667 (Floating point-division)
# 3 < 6.667  = True, since 3 is less than 6.667

# B) False or not (False or True) and True
# False or True = True
# not True = False
# False and True = False

# C) 3/4==0or5<6
# 3/4=0.75 (Floating point-division)
# 0.75==0  False
# 5 < 6    True
# False or True gives ' True '

# 3. Let a = True, b = True, c = False. Evaluate the following (15 points):
# A) a and not b
# a=True , b=True
# not b = not True = False
# a and not b = True and False = False

# B) b or c
# b = True
# c = False
# b or c = 'True or False' = True

# C) not b == c
# not b = not True = False
# c = False
# not b == c  = 'False == False' = True

# D) a and not c
# a = True
# not c = 'not False' = True
# a and not c = 'True and True' = True

# E) b or c and not a
# b = True, c = False, a = True
# not a = not True = False
# c and not a = 'False and False'= False
# b or False = 'True or False' = True

# F) a != b or b != c
# a = True, b=True, c= False
# a != b = 'True != True' = False
# b != c = 'True != False' = True
# 'False or True' = True

# 4. Select all invalid variable names below and give reason the variable name is invalid (15 points):
# A) speed Of Light
# Invalid since it contains spaces, otherwsise can be written as 'speed_of_light'

# B) x_2
# Valid

# C) 3Attempts
# Invalid since a variable name should not start with a digit, to correct an underscore can be introduced before the digit '_3Attempts'

# D) vertical-distance
# Invalid since it contains an hyphen instead of underscore, 'vertical_distance'

# E) B5V
# Valid since it starts with a letter and not a digit


# 5. Write code that initializes a variable to store the length of a square in inches, calculates the perimeter and area of the square, and prints the results. Test the program by changing the initial value for length to different integer values (15 points).
# All dimensions are in inches
# Let the length of square be L
L = 4
# Let perimeter of the square be P
P = L * 4
# Let the area of the square be A
A = L**2

print(P)
print(A)

# 6. Write code that will assign a variable to a given number of seconds and then calculate the equivalent number of hours, minutes and seconds. For example, 300 seconds is 0 hours, 5 minutes and 0 seconds while 4503 seconds is 1 hour, 15 minutes and 3 seconds. Assign separate variables to each of these values (i.e., hours, minutes, seconds). Evaluate your program calculations using different starting times (initial seconds). Be mindful of possible rounding errors, use integers only (15 points).
total_seconds = 9432
# hours, minutes, and seconds calculation
seconds = total_seconds % 60
minutes = (total_seconds % 3600) // 60
hours = total_seconds // 3600

print(f"{hours} hours, {minutes} minutes, {seconds} seconds")

# 7. Debug the following code which greets a guest and checks if the guest can get on a ride by checking their age and height (10 points) :

name = "Josh"
height_inches = 62.4
age = 15

# Greeting :
print("Hello, " + name)


# 8. Write code that checks the data types of the following variables and casts them to the proper data type if needed (10 points):

age = 32.4
avgHeight = "73.54"
numOfGuests = 47.0
flightSpeed = "423 miles/hour"
outsideTemp = 73.2

# converting the variables to the correct data types
age = int(age)
avgHeight = float(avgHeight)
numOfGuests = int(numOfGuests)
flightSpeed = str(flightSpeed)
outsideTemp = float(outsideTemp)

# printing the variables and their data types
print("age:", age, ", data type:", type(age))
print("avgHeight:", avgHeight, ", data type:", type(avgHeight))
print("numOfGuests:", numOfGuests, ", data type:", type(numOfGuests))
print("flightSpeed:", flightSpeed, ", data type:", type(flightSpeed))
print("outsideTemp:", outsideTemp, ", data type:", type(outsideTemp))
