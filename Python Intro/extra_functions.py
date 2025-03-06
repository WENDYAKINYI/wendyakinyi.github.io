# 6. We're going to practice importing functions from another file. Complete the following steps:
#  - Create a new .py file called extra_functions.py
#  - In extra_functions.py, write a function called midpoint which takes an integer as input and returns
#    the midpoint between that integer and 0.
#  - Include an if __name__ == '__main__' codeblock in extra_functions.py to test your midpoint function.
#  - Import extra_functions.py into this file.
#  - Run this line of code: midpoint_of_10 = midpoint(10)
# (20 points)


# extra_functions.py

def midpoint(number):
    '''
    function calculates midpoint by taking an integer as input and returns
    the midpoint between that integer and 0

    Parameters:
    number (int): An integer

    Returns:
    float: Midpoint between the integer and 0
    '''
    return number / 2


if __name__ == '__main__':
    # Test the midpoint function when running extra_functions.py directly
    test_number = 10
    result = midpoint(test_number)
    print(f"The midpoint of {test_number} is {result}")
