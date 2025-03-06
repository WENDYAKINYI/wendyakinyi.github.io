import unittest
from Assignment4 import Records


class TestCollections(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """prints “setUpClass” to the console and instantiates an object of the Record class using the credit card file and the complaints file."""
        print("setUpClass")
        cls.records = Records('credit_card.csv', 'Credit Card')
        cls.records.load_data('customer_complaints.csv', 'Complaints')

    @classmethod
    def tearDownClass(cls):
        """Deletes the Records instance after testing."""
        print("tearDownClass")
        del cls.records

    def setUp(self):
        """Prints “setUp” to the console."""
        print("setUp")

    def tearDown(self):
        """Prints “tearDown” to the console."""
        print("tearDown")

    def test_create_container(self):
        """check that the method is able to create a namedtuple with varying number of column names and that it raises the appropriate exceptions"""
        print("Executing test_create_container")

    def test_record_stats(self):
        """Checks that the function is able to compute record stats correctly for various columns and multiple files."""
        print("Executing test_record_stats")

    def test_extract_top_n(self):
        """Checks that the method is able to extract the correct top n values for the corresponding column record stats attribute."""
        print("Executing test_extract_top_n")


if __name__ == '__main__':
    unittest.main()
