import unittest
from shelter import Hammock, Tent, Tarp


class TestShelter(unittest.TestCase):
    """Unit tests for the Shelter, Hammock, Tent, and Tarp classes.

     Methods:
    --------
    - setUpClass: Print 'setUpClass' to the console.
    - tearDownClass: Print 'tearDownClass' to the console.
    - setUp: Create instances of Tent, Tarp, and Hammock classes for testing.
    - tearDown: Delete each instance of Tent, Tarp, and Hammock created in setUp.
    - test_str: Check that the string returned by the str method matches the expected format.
    - test_lt: Check if the __lt__ method is working as intended for each class.
    - test_is_better: Check if the is_better method is working as intended.

    """

    @classmethod
    def setUpClass(cls):
        """
        Print 'setUpClass' to the console.
        """
        print("Executing setUpClass")

    @classmethod
    def tearDownClass(cls):
        """
        Print 'tearDownClass' to the console.
        """
        print("Executing tearDown")

    def setUp(self):
        """Creates instances of the Tent, Tarp, and Hammock for testing."""
        print("Executing setUp.")
        # Create instances of Tent, Tarp, and Hammock classes for testing
        self.tent_instance = Tent(4, "nylon", 10, 100, True, 8.5, True)
        self.tarp_instance = Tarp(2, "polyester", 5, 50, 3.2, 15,)
        self.hammock_instance = Hammock(1, "canvas", 7, 2.5)

    def tearDown(self):
        """Delete instances of Tent, Tarp, and Hammock created in the setUp method."""
        print("Executing tearDown.")
        # Delete instances of Tent, Tarp, and Hammock created in setUp
        del self.tent_instance
        del self.tarp_instance
        del self.hammock_instance

    def test_str(self):
        """Tests if the __str__ method corresponds to the format."""
        print("Executing test_str.")
        self.assertEqual(str(
            self.tent_instance), "Tent(Shelter(num_occupants=4, material=nylon, setup_time=10, weight=8.5, seasons=3), sqft=100, vestibule=True, structure_poles=True)")
        self.assertEqual(str(
            self.tarp_instance), "Tarp(Shelter(num_occupants=2, material=polyester, setup_time=5, weight=3.2, seasons=15), sqft=50)")
        self.assertEqual(str(
            self.hammock_instance), "Hammock(Shelter(num_occupants=1, material=canvas, setup_time=7, weight=2.5, seasons=3), length=11)")

    def test_lt(self):
        """Tests if the __lt__ method is working as intended ."""
        print("Executing test_lt.")
        # Implement comparison based on weight as an example
        self.assertTrue(self.hammock_instance < self.tent_instance)

    def test_is_better(self):
        """Tests if the is_better method is working as intended."""
        print("Executing test_is_better.")
        # Example test
        self.assertTrue(self.tarp_instance.is_better(self.tent_instance))


if __name__ == "__main__":
    unittest.main()
