import unittest
import os
from autompg import AutoMPG


class TestAutoMPG(unittest.TestCase):
    """
    A test class for the AutoMPGData functionalities.

    Methods:
    --------
    - setUpClass: Instantiate an object of the AutoMPGData class for testing.
    - tearDownClass: Delete the auto-mpg.clean.txt file.
    - setUp: Print 'setUp' to the console.
    - tearDown: Print 'tearDown' to the console.
    - test_str: Check if the string returned by the str method matches the expected format.
    - test_eq: Check if the __eq__ method is working as intended.
    - test_lt: Check if the __lt__ method is working as intended.
    - test_hash: Check if the hash function is working properly.
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate an object of AutoMPGData class before any tests are run.
        """
        print("Setting up class for AutoMPG tests.")
        cls.autoMPGData = AutoMPG('chevrolet', 'chevelle malibu', 1970, 18.0)

    @classmethod
    def tearDownClass(cls):
        """
        Delete the auto-mpg.clean.txt file.
        """
        print("Tearing down AutoMPG tests class.")
        try:
            os.remove('auto-mpg.clean.txt')  # Remove the file if it exists
        except FileNotFoundError:
            pass  # Ignore if the file does not exist

    def setUp(self):
        """
        Print 'setUp' to the console.
        """
        print("setUp")

    def tearDown(self):
        """
        Print 'tearDown' to the console.
        """
        print("tearDown")

    def test_str(self):
        """
        Check that the string returned by the str method matches the expected format.
        """
        print("Executing test_str.")
        self.assertEqual(str(self.autoMPGData),
                         "AutoMPG('chevrolet', 'chevelle malibu', 1970, 18.0)")

    def test_eq(self):
        """
        Check if the __eq__ method is working as intended.
        """
        print("Executing test_eq.")
        another_autoMPGData = AutoMPG(
            'chevrolet', 'chevelle malibu', 1970, 18.0)
        self.assertEqual(self.autoMPGData, another_autoMPGData)

    def test_lt(self):
        """
        Check if the __lt__ method is working as intended.

        """
        print("Executing test_lt.")
        another_autoMPGData = AutoMPG('ford', 'mustang', 1971, 18.5)
        self.assertTrue(self.autoMPGData < another_autoMPGData)

    def test_hash(self):
        """
        Check if the hash function is working properly.
        """
        print("Executing test_hash.")
        self.assertIsInstance(hash(self.autoMPGData), int)


if __name__ == '__main__':
    unittest.main()
