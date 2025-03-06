'''
COMP 4401
Homework 4 - Classes & Unit Tests

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


Homework 4 Instructions:
Every class, method and function must have proper DocString documentation of the
following form :

def someFunction(arg1, arg2):
    """
    Function DocString. Indent the DocString.
    One or two lines explaining what the function does

    Args:
        arg1 (type): what is this argument
        arg2 (type): what is this argument

    Return:
        (type): what is being returned by the function ?
    """
    #your code here


class SomeClassIMadeUp:
    """
    Class DocString. Indent the DocString
    One or two lines explaining what the class does

    Attributes:
    ----------------------------------------
        attr1 (type): what is this attribute
        attr2 (type): what is this attribute

    Method:
    ----------------------------------------
        method1: what does this method do
        method2: what does this method do
    """

def method_inside_class(arg1, arg2):
    """
    Method DocString. Indent the DocString
    One or two lines explaining what the method does

    Args: (don't include 'self' in the arguments)
        arg1 (type): what is this argument
        arg2 (type): what is this argument

    Return:
        (type): what is being returned by the method ?
    """


'''
#--------------------------------------------------------------------------#


###---------------------###
###------ Classes ------###
###---------------------###

# 1. Complete the following class, called Car.
# The class must have the following attributes :
# -color (str)
# -year (int)
# -make (str)
# -model (str)
# -num_doors (this includes the hatch/tail gate) (int)
# -engine_type (gas, diesel, electric) (str)
# -top_speed in miles/hour (float)
# -mpg (miles per gallon, float)

class Car:
    """
    This class represents a car.

    Attributes:
        color (str): The color of the car.
        year (int): The year the car was manufactured.
        make (str): The make of the car.
        model (str): The model of the car.
        num_doors (int): The number of doors on the car (this includes the hatch/tail gate).
        engine_type (str): The type of engine in the car (gas, diesel, electric).
        top_speed (float): The top speed of the car in miles per hour.
        mpg (float): The Miles per gallon of the car.
    """

    def __init__(self, color, year, make, model, num_doors, engine_type, top_speed, mpg):
        """
        Initializes a new car.

        Args:
            color (str): The color of the car.
            year (int): The year the car was manufactured.
            make (str): The make of the car.
            model (str): The model of the car.
            num_doors (int): The number of doors on the car (this includes the hatch/tail gate).
            engine_type (str): The type of engine in the car (gas, diesel, electric).
            top_speed (float): The top speed of the car in miles per hour.
            mpg (float): The Miles per gallon of the car.
        """
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.num_doors = num_doors
        self.engine_type = engine_type
        self.top_speed = top_speed
        self.mpg = mpg


# 2. Complete the following methods :
# changeColor: this method should take in a color as an argument (str)
# and change the color attribute of the Car instance

# carInfo: this method should take no arguments and return a string
# with the basic car info in the format : "Make - Model - Color"

def changeColor(self, color):
        """
        Changes the color of the car.

        Args:
            color (str): The new color of the car.
        """
        self.color = color

def carInfo(self):
        """
        Outputs basic car information.

        Returns:
            str: A string containing the basic car info (Make - Model - Color).
        """
        return f"{self.make} - {self.model} - {self.color}"


# 3. Complete the following method :
# betterGasMileage: this method should take two instances of the Car
# class and return the car info, using the carInfo method, of the car
# instance that gets the better gas mileage.

def betterGasMileage(car1, car2):
        """
        Compares the gas mileage of two car instances and returns the car info using the carInfo method, of the car with better gas mileage.

        Args:
            car1 (Car): The first car instance to compare.
            car2 (Car): The second car instance to compare.

        Returns:
            str: The car info of the car with better gas mileage.
        """
        if car1.mpg > car2.mpg:
            return car1.carInfo()
        elif car2.mpg > car1.mpg:
            return car2.carInfo()
        else: #instance when the two cars have equal gas mileages
            return f"Both cars have the same gas mileage."


# 4. Create the following class attribute and class method :
# create a class attribute, called num_cars, which increases every time
# a new Car instance is created.

class Car:

    """
    Tracks the number of car instances created.
    
    """
    num_cars = 0

    def __init__(self, color, year, make, model, num_doors, engine_type, top_speed, mpg):
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.num_doors = num_doors
        self.engine_type = engine_type
        self.top_speed = top_speed
        self.mpg = mpg

        # Increased number of Car instances.
        Car.num_cars += 1

    # using the class method
    def get_num_cars(cls):
        """
        Returns the number of Car instances that have been created.

        Returns:
            int: The number of Car instances.
        """
        return cls.num_cars


# 5. Make a parent class for Car, called Vehicle, which will
# contain an __init__ method for the following attributes :
# -color (str)
# -year (int)
# -make (str)
# -model (str)
# -top_speed in miles/hour (float)
# -mpg (miles per gallon, float)
#
# Don't forget to change the Car class __init__ method to make use of the Vehicle class.

class Vehicle:
    """
    Parent class to represent a vehicle.

    Attributes:
        color (str): The color of the vehicle.
        year (int): The year the vehicle was manufactured.
        make (str): The make of the vehicle.
        model (str): The model of the vehicle.
        top_speed (float): The top speed of the vehicle in miles per hour.
        mpg (float): The Miles per gallon of the vehicle.
    """

    def __init__(self, color, year, make, model, top_speed, mpg):
        """
        Initializes a new vehicle.

        Args:
            color (str): The color of the vehicle.
            year (int): The year the vehicle was manufactured.
            make (str): The make of the vehicle.
            model (str): The model of the vehicle.
            top_speed (float): The top speed of the vehicle in miles per hour.
            mpg (float):The Miles per gallon of the vehicle.
        """
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.mpg = mpg

class Car(Vehicle):
    """
    Represents a car, inheriting from the Vehicle class.

    Attributes:
        num_doors (int): The number of doors on the car, (this includes the hatch/tailgate).
        engine_type (str): The type of engine in the car (gas, diesel, electric).
    """

    def __init__(self, color, year, make, model, num_doors, engine_type, top_speed, mpg):
        """
        Initializes a new car.

        Args:
            color (str): The color of the car.
            year (int): The year the car was manufactured.
            make (str): The make of the car.
            model (str): The model of the car.
            num_doors (int): The number of doors on the car, (this includes the hatch/tailgate).
            engine_type (str): The type of engine (gas, diesel, electric).
            top_speed (float): The top speed of the car in miles per hour.
            mpg (float): The Miles per gallon of the car.
        """
        super().__init__(color, year, make, model, top_speed, mpg)
        self.num_doors = num_doors
        self.engine_type = engine_type































