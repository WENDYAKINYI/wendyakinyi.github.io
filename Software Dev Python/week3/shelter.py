
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

    Methods:
    --------
    __init__: Constructs all the common attributes for the shelter.

    is_better(other): Determines if the shelter is better than another shelter based on weight, setup time, and season rating.
        Returns: (bool) True if the shelter is better than or equal to the other.

    total_sleeping_spots: Adds up the total number of sleeping spots available from a non-determined number of Shelters.
        Returns: (int) Total number of sleeping spots.

    __str__():  A string representation of the Shelter object.

    __repr__(): Returns the string representation of the Shelter object.

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

    def total_sleeping_spots(*shelters):
        """
        Adds up the total number of sleeping spots available from a non-determined number of Shelters.
        Returns: (int) Total number of sleeping spots.

        """
        total_spots = sum(shelter.num_occupants for shelter in shelters)
        return total_spots

    def __str__(self):
        """
        A string representation of the Shelter object.
        """
        return f"Shelter(num_occupants={self.num_occupants}, material={self.material}, setup_time={self.setup_time}, weight={self.weight}, seasons={self.seasons})"

    def __repr__(self):
        """
        Returns the string representation of the Shelter object.
        """
        return (self.__str__())


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

         Methods:
        --------
         __init__: Constructs all the necessary attributes for the tent object.

         __str__(): A string representation of the Tent object.

        __repr__(): Returns a string representation of the Tent object.

        __lt__(other): Compares two Tent objects based on number of occupants and sqft.
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
        return f"Tent({super().__str__()}, sqft={self.sqft}, vestibule={self.vestibule}, structure_poles={self.structure_poles})"

    def __repr__(self):
        """
        Returns a string representation of the Tent object.
        """
        return ((self.__str__()))

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

        Methods:
        --------
        __init__: Constructs all the necessary attributes for the hammock object.

        __str__(): A string representation of the hammock object.

        __repr__(): Returns a string representation of the hammock object.

        __lt__(other): Compares two hammock objects based on weight and setup_time.
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
        return f"Hammock({super().__str__()}, length={self.length})"

    def __repr__(self):
        """
        Returns a string representation of the hammock object.
        """
        return ((self.__str__()))

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

        Methods:
        --------
        __init__: Constructs all the necessary attributes for the tarp object.

        __str__(): A string representation of the tarp object.

        __repr__(): Returns a string representation of the tarp object.

        __lt__(other): Compares two tarp objects based on number of occupants and sqft.
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
        return f"Tarp({super().__str__()}, sqft={self.sqft})"

    def __repr__(self):
        """
        Returns a string representation of the tarp object.
        """
        return ((self.__str__()))

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
    total_spots = Shelter.total_sleeping_spots(*shelters)
    print(total_spots)
