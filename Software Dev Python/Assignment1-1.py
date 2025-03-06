'''
COMP 3006
Homework 1 - Functional programming and OOP intro

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
     - Args: input parameters, their types and what they are for
     - Returns: return data type and what it is
- All tests of your functions should be commented out in your final submission or
  encolosed with an if __name__ == '__main__' codeblock.
- All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.
'''

# Question 1:
# Create a function, called student_id_numbers, that takes a list of student names
# and generates an automatic student id number. The function must be able to handle
# collisions using dictionaries. A collision will happen when students have the same
# last name. The function must return the dictionary or dictionaries containing the
# students and their student id numbers.
# Note: using defaultdict might be helpful but not required. Having some good music
# while you code this might be helpful but also not required.

# You will also need to write a second function, called retrieve student_number that
# will take a student's name and will return their student id number. This function
# will need to handle misspelled names.


def student_id_numbers(student_names):
    """
    This function generates automatic student id numbers from a list of student names.

    Args:
    student_names (list): List of student names

    Returns:
    dict: Dictionary containing the students and their student id numbers
    """
    student_id_dict = {}
    for name in student_names:
        # Split the student's name into first and last name
        first_name, last_name = name.split()

        # Check if last name already exists in the dictionary
        if last_name in student_id_dict:
            # If collision occurs, append a number to the last name
            count = 1
            while f"{last_name}{count}" in student_id_dict:
                count += 1
            last_name = f"{last_name}{count}"

        # Generate student id number
        student_id = f"{first_name}{last_name}"

        # Add student and id number to the dictionary
        student_id_dict[last_name] = student_id

    return student_id_dict


# Test
if __name__ == '__main__':
    student_names = ["Akinyi Odero", "Odero Akinyi",
                     "Akinyi Odero", "Ode Aki", "Odero Akinyi", "Akinyi Odero"]
    student_id_dict = student_id_numbers(student_names)
    print(student_id_dict)


def retrieve_student_number(student_name, student_id_dict):
    """
    This function retrieves a student's id number from the dictionary of student ids 
    and also handles misspelled names by searching for a close match.

    Args:
    student_name (str): The name of the student to retrieve the id for
    student_ids (dict): A dictionary with student names and their id numbers 

    Returns: 
    The student id number if found or a message indicating the name was not found
    """
    # If the name exists exactly in the dictionary, return the id
    if student_name in student_id_dict:
        return student_id_dict[student_name]

    # Handling misspelled names by finding a match of the first four letters
    for name in student_id_dict.keys():
        if name.lower().startswith(student_name.lower()[:4]):
            return student_id_dict[name]

    # If no match is found, return student name not found
    return "Student name not found."


# Test
if __name__ == '__main__':
    student_names = ["Akinyi Odero", "Odero Akinyi",
                     "Akinyi Odero", "Ode Aki", "Odero Akinyi", "Akinyi Odero"]
    student_id_dict = student_id_numbers(student_names)

    student_name_search = "Akit Odero"
    retrieved_student_number = retrieve_student_number(
        student_name_search, student_id_dict)

    if retrieved_student_number is not None:
        print(
            f"The student id number for {student_name_search} is: {retrieved_student_number}")
    else:
        print(f"{student_name_search} not found.")


# Question 2:
# In France there is a child's marching song called "Un Kilometre a Pied" which
# translates to One Kilometer On Foot. The lyrics are:

# One kilometer on foot wears out, wears out,
# One kilometer on foot wears out your shoes for good.

# Two kilometers on foot wears out, wears out,
# Two kilometers on foot wears out your shoes for good.

# ...

# The lyrics repeat to infinity (or rather until the kids get tired of singing).
# Create a function, called un_kilometre_a_pied, which takes no parameters and prints
# the lyrics of the song to the console. The function must make use of a generator to
# write the lyrics of the song until the user decides to stop. The generator you use must
# be able to produce a value that increses to infinity. You must make sure that your code
# doesn't get caught in an infinite loop that is difficult to exit, I recommend having
# the necessary logic to allow the user to exit whenever they get tired of the song.

def un_kilometre_a_pied():
    """
    The function prints the lyrics of the song "Un Kilometre a Pied" using a generator.

    The lyrics repeat until the user decides to stop.

    """
    # kilometre counter starting from 1
    kilometre = 1

    while True:
        # lyrics generator
        lyrics = f"{kilometre} kilometer{'s' if kilometre > 1 else ''} on foot wears out, wears out,\n" \
                 f"{kilometre} kilometer{'s' if kilometre > 1 else ''} on foot wears out your shoes for good."

        # Print the lyrics
        print(lyrics)

        # Ask the user if they want to continue or stop
        user_input = input(
            "Press Enter to continue or type 'stop' to end the song: ").strip().lower()

        if user_input in ['stop']:
            break

        # kilometer counter increment
        kilometre += 1


# Test
if __name__ == '__main__':
    un_kilometre_a_pied()


### ----------------------------------------------------------------------------------------- ###
### We wish to compare and store data on various types of shelters for when we go backpacking ###
### ----------------------------------------------------------------------------------------- ###

# Question 3:
# Create a class, called Tent, that contains the following attributes (in the order given):
# num_occupants (int)
# material (str)
# setup_time (int, number of minutes)
# sqft (float)
# vestibule (bool, True if tent has a vestibule)
# weight (float)
# structure_poles (bool, True if tent has structural poles. Should have a default value of True)
# seasons (int, 3 or 4. Should have a default value of 3)

# The class should also have the following methods:
# __str__
# __repr__
# __lt__ (this should use the num_occupants and sqft attributes to determine if one tent is
# less than another tent)
# is_better (a tent is considered better if and only if its weight and setup_time is less than
# another tent whilst having equal or better season rating)

class Tent:
    """
    A class to represent a tent with various attributes.

    Attributes:
    -----------
    num_occupants (int): The number of occupants the tent can contain.
    material (str): The material the tent is made of.
    setup_time (int): The time it takes to set up the tent, in minutes.
    sqft (float): The square footage of the tent.
    vestibule (bool): True if the tent has a vestibule, False otherwise.
    weight (float): The weight of the tent.
    structure_poles (bool): True if the tent has structural poles, defaults to True.
    seasons (int): The season the tent is suitable for, either 3 or 4, defaults to 3.
    """

    def __init__(self, num_occupants, material, setup_time, sqft, vestibule, weight, structure_poles=True, seasons=3):
        """
        Constructs all the necessary attributes for the tent object.
        """
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.sqft = sqft
        self.vestibule = vestibule
        self.weight = weight
        self.structure_poles = structure_poles
        self.seasons = seasons

    def __str__(self):
        """
        A string representation of the Tent object.
        """
        return f"Tent for {self.num_occupants} occupants, {self.material} material, {self.sqft} sqft, weighing {self.weight}."

    def __repr__(self):
        """
        A detailed string representation of the Tent object.
        """
        return (f"Tent(num_occupants={self.num_occupants}, material='{self.material}', setup_time={self.setup_time}, "
                f"sqft={self.sqft}, vestibule={self.vestibule}, weight={self.weight}, "
                f"structure_poles={self.structure_poles}, seasons={self.seasons})")

    def __lt__(self, other):
        """
        A comparison based on the number of occupants and square footage.

        Returns: (bool) True if the tent is less than the other, False otherwise
        """
        if self.num_occupants == other.num_occupants:
            return self.sqft < other.sqft
        return self.num_occupants < other.num_occupants

    def is_better(self, other):
        """
        Determines if the tent is better than another tent based on weight, setup time, and season rating.

        Returns: (bool) True if the tent is better than or equal to the other.


        """
        return (self.weight < other.weight and
                self.setup_time < other.setup_time and
                self.seasons >= other.seasons)


# Test
if __name__ == "__main__":
    tent1 = Tent(num_occupants=4, material="Nylon", setup_time=15,
                 sqft=65.0, vestibule=True, weight=5.5)
    tent2 = Tent(num_occupants=2, material="Polyester",
                 setup_time=10, sqft=60.0, vestibule=False, weight=2.5)

    print(tent1)
    print(tent2)
    print(tent1 < tent2)
    print(tent1.is_better(tent2))


# Question 4:
# We wish to compare and store data on various types of shelters for when we go backpacking.
# Create a class, called Hammock, that contains the following attributes (in the order given):
# num_occupants (int)
# material (str)
# setup_time (int, number of minutes)
# weight (float)
# length (int, length of hammock in feet. Should have a default value of 11)
# seasons (int, 3 or 4. Should have a default value of 3)

# The class should also have the following methods:
# __str__
# __repr__
# __lt__ (this should use the weight and setup_time attributes to determine if one hammock is
# less than another hammock)
# is_better (a tent is considered better if and only if its weight and setup_time is less than
# another tent whilst having equal or better season rating)


class Hammock:
    """
    A class to represent a hammock with various attributes.

    Attributes:
    -----------
    num_occupants (int): The number of occupants the hammcok can hold.
    material (str): The material the hammock is made of.
    setup_time (int): The time it takes to set up the hammock, in minutes.
    weight (float): The weight of the hammock.
    length (int): The length of the hammock in feet, should have a default value of 11.
    seasons (int): The season the tent is suitable for, either 3 or 4, defaults to 3.
    """

    def __init__(self, num_occupants, material, setup_time, weight, length=11, seasons=3):
        """
        Constructs all the necessary attributes for the hammock object.
        """
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.weight = weight
        self.length = length
        self.seasons = seasons

    def __str__(self):
        """
        A string representation of the hammock object.
        """
        return f"Hammock for {self.num_occupants} occupants, {self.material} material, weighing {self.weight}."

    def __repr__(self):
        """
        A detailed string representation of the Tent object.
        """
        return (f"Hammock(num_occupants={self.num_occupants}, material='{self.material}', setup_time={self.setup_time}, "
                f"weight={self.weight}, "
                f"length={self.length}, seasons={self.seasons})")

    def __lt__(self, other):
        """
        A comparison based on the weight and set up time of the hammocks.

        Returns: (bool) True if the hammock is less than the other, False otherwise
        """
        if self.weight == other.weight:
            return self.weight < other.weight
        return self.setup_time < other.setup_time

    def is_better(self, other):
        """
        Determines if the tent is better than another tent based on weight, setup time, and season rating.

        Returns: (bool) True if the tent is better than or equal to the other.


        """
        return (self.weight < other.weight and
                self.setup_time < other.setup_time and
                self.seasons >= other.seasons)


# Test
if __name__ == "__main__":
    hammock1 = Hammock(num_occupants=1, material="canvas",
                       setup_time=5, weight=2.5)
    hammock2 = Hammock(num_occupants=2, material="rope mesh",
                       setup_time=8, weight=3.0)

    print(hammock1)
    print(hammock2)
    print(hammock1 < hammock2)
    print(hammock1.is_better(hammock2))


# Question 5:
# Create a class, called Tarp, that contains the following attributes (in the order given):
# num_occupants (int)
# material (str)
# setup_time (int, number of minutes)
# sqft (float)
# weight (float)
# seasons (int, 3 or 4. Should have a default value of 3)

# The class should also have the following methods:
# __str__
# __repr__
# __lt__ (this should use the num_occupants and sqft attributes to determine if one tent is
# less than another tent)
# is_better (a tent is considered better if and only if its weight and setup_time is less than
# another tent whilst having equal or better season rating)


class Tarp:
    """
    A class to represent a tarp with various attributes.

    Attributes:
    -----------
    num_occupants (int): The number of occupants the tarp can cover.
    material (str): The material the tarp is made of.
    setup_time (int): The time it takes to set up the tarp, in minutes.
    sqft (float): The square footage of the tarp.
    weight (float): The weight of the tarp.
    seasons (int): The season the tent is suitable for, either 3 or 4, defaults to 3.
    """

    def __init__(self, num_occupants, material, setup_time, sqft, weight, seasons=3):
        """
        Constructs all the necessary attributes for the tarp object.
        """
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.sqft = sqft
        self.weight = weight
        self.seasons = seasons

    def __str__(self):
        """
        A string representation of the Tarp object.
        """
        return f"Tarp for {self.num_occupants} occupants, {self.material} material, {self.sqft} sqft, weighing {self.weight}."

    def __repr__(self):
        """
        A detailed string representation of the tarp object.
        """
        return (f"Tarp(num_occupants={self.num_occupants}, material='{self.material}', setup_time={self.setup_time}, "
                f"sqft={self.sqft}, weight={self.weight}, "
                f"seasons={self.seasons})")

    def __lt__(self, other):
        """
        A comparison based on the number of occupants and square footage.

        Returns: (bool) True if the tarp is less than the other, False otherwise
        """
        if self.num_occupants == other.num_occupants:
            return self.sqft < other.sqft
        return self.num_occupants < other.num_occupants

    def is_better(self, other):
        """
        Determines if the tarp is better than another tarp based on weight, setup time, and season rating.

        Returns: (bool) True if the tarp is better than or equal to the other.


        """
        return (self.weight < other.weight and
                self.setup_time < other.setup_time and
                self.seasons >= other.seasons)


# Test
if __name__ == "__main__":
    tarp1 = Tarp(num_occupants=4, material="Nylon",
                 setup_time=15, sqft=65.0, weight=5.5)
    tarp2 = Tarp(num_occupants=2, material="Polyethylener",
                 setup_time=10, sqft=60.0, weight=2.5)

    print(tarp1)
    print(tarp2)
    print(tarp1 < tarp2)
    print(tarp1.is_better(tarp2))


# Question 6:
# There is lots of repeated code above, let's create a parent class for Tent, Hammock and Tarp
# called Shelter. The Shelter class should have a constructor that takes over all of the
# attributes that are common for Tent, Hammock and Tarp. The Shelter class should also include
# the is_better method. You will also need to create a new method called total_sleeping_spots
# which will add up the total number of sleeping spots available from a non-determined number
# of Shelters being passed into the method.
# Rewrite the Tent, Hammock and Tarp classes taking into account the changes brought on by using
# the Shelter parent class.

class Shelter:
    """
    A parent class for Tent, Hammock and Tarp with common attributes.

    Attributes:
    -----------
    num_occupants (int): The number of occupants the shelter can accomodate.
    material (str): The material the shelter is made of.
    setup_time (int): The time it takes to set up the shelter, in minutes.
    weight (float): The weight of the shelter.
    seasons (int): The seasons the shelter is suitable for, either 3 or 4, defaults to 3.

    """

    def __init__(self, num_occupants, material, setup_time, weight, seasons=3):
        """
        Constructs all the common attributes for the shelter.
        """
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.weight = weight
        self.seasons = seasons

    def is_better(self, other):
        """
        Determines if the shelter is better than another shelter based on weight, setup time, and season rating.
        Returns: (bool) True if the shelter is better than or equal to the other.

        """
        return (self.weight < other.weight and
                self.setup_time < other.setup_time and
                self.seasons >= other.seasons)

    def total_sleeping_spots(shelters):
        """
        Adds up the total number of sleeping spots available from a non-determined number of Shelters.
        Returns: (int) Total number of sleeping spots.

        """
        return sum(shelter.num_occupants for shelter in shelters)

    def __str__(self):
        """
        A string representation of the Shelter object.
        """
        return f"Shelter for {self.num_occupants} occupants, {self.material} material, weighing {self.weight}kg."

    def __repr__(self):
        """
        A detailed string representation of the Shelter object.
        """
        return (f"Shelter({self.num_occupants}, {self.material}, {self.setup_time}, {self.weight}, {self.seasons})")


class Tent(Shelter):
    """
        A class to represent a tent with various attributes.
        Attributes:
        -----------

        num_occupants (int): The number of occupants the tent can contain.
        material (str): The material the tent is made of.
        setup_time (int): The time it takes to set up the tent, in minutes.
        sqft (float): The square footage of the tent.
        vestibule (bool): True if the tent has a vestibule, False otherwise.
        weight (float): The weight of the tent.
        structure_poles (bool): True if the tent has structural poles, defaults to True.
        seasons (int): The season the tent is suitable for, either 3 or 4, defaults to 3.

    """

    def __init__(self, num_occupants, material, setup_time, sqft, vestibule, weight, structure_poles=True, seasons=3):
        """
        Constructs all the necessary attributes for the tent object.
        """
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.sqft = sqft
        self.vestibule = vestibule
        self.structure_poles = structure_poles

    def __str__(self):
        """
        A string representation of the Tent object.
        """
        return f"Tent for {self.num_occupants} occupants, {self.material} material, {self.sqft} sqft, weighing {self.weight}."

    def __repr__(self):
        """
        A detailed string representation of the Tent object.
        """
        return (f"Tent({super().__repr__()}, {self.sqft}, {self.vestibule}, {self.structure_poles})")

    def __lt__(self, other):
        """
        Compares two Tent objects based on  on number of occupants and sqft.
        """
        if self.num_occupants == other.num_occupants:
            return self.sqft < other.sqft
        return self.num_occupants < other.num_occupants


class Hammock(Shelter):
    """
        A class to represent a hammock with various attributes.
        Attributes:
        -----------
        num_occupants (int): The number of occupants the hammcok can hold.
        material (str): The material the hammock is made of.
        setup_time (int): The time it takes to set up the hammock, in minutes.
        weight (float): The weight of the hammock.
        length (int): The length of the hammock in feet, should have a default value of 11.
        seasons (int): The season the tent is suitable for, either 3 or 4, defaults to 3.
    """

    def __init__(self, num_occupants, material, setup_time, weight, length=11, seasons=3):
        """
        Constructs all the necessary attributes for the hammock object.
        """
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.length = length

    def __str__(self):
        """
        A string representation of the hammock object.
        """
        return f"Hammock for {self.num_occupants} occupants, {self.material} material, weighing {self.weight}"

    def __repr__(self):
        """
        A detailed string representation of the hammock object.
        """
        return (f"Hammock({super().__repr__()}, {self.length})")

    def __lt__(self, other):
        """
        Compares two hammock objects based on weight and setup_time.
        """
        if self.weight == other.weight:
            return self.weight < other.weight
        return self.setup_time < other.setup_time


class Tarp(Shelter):
    """
        A class to represent a tarp with various attributes.
        Attributes:
        -----------
        num_occupants (int): The number of occupants the tarp can cover.
        material (str): The material the tarp is made of.
        setup_time (int): The time it takes to set up the tarp, in minutes.
        sqft (float): The square footage of the tarp.
        weight (float): The weight of the tarp.
        seasons (int): The season the tent is suitable for, either 3 or 4, defaults to 3.
    """

    def __init__(self, num_occupants, material, setup_time, sqft, weight, seasons=3):
        """
        Constructs all the necessary attributes for the tarp object.
        """
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.sqft = sqft

    def __str__(self):
        """
        A string representation of the tarp object.
        """
        return f"Tarp for {self.num_occupants} occupants, {self.material} material, {self.sqft} sqft, weighing {self.weight}"

    def __repr__(self):
        """
        A detailed string representation of the tarp object.
        """
        return (f"Tarp({super().__repr__()}, {self.sqft})")

    def __lt__(self, other):
        """
        Compares two Tarp objects based on number of occupants and sqft.
        """
        if self.num_occupants == other.num_occupants:
            return self.sqft < other.sqft
        return self.num_occupants < other.num_occupants


# Test
if __name__ == "__main__":
    tent1 = Tent(num_occupants=4, material='nylon', setup_time=2,
                 sqft=100, vestibule=True, weight=2.5)
    hammock1 = Hammock(num_occupants=3, material='canvas',
                       setup_time=5, weight=3.2)
    tarp1 = Tarp(num_occupants=2, material='polyester',
                 setup_time=10, sqft=80, weight=2.5)
    print(tent1.is_better(hammock1))

# Total sleeping spots
    shelters = [tent1, hammock1, tarp1]
    total_spots = Shelter.total_sleeping_spots(shelters)
    print(total_spots)
