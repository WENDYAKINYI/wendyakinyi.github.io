
from collections import namedtuple
import csv
import os

# step 1: AutoMPG class


class AutoMPG:
    """
    A class that represents an automobile's make, model, year, and mpg.

    Attributes:
    -----------
    make (str): Automobile manufacturer.
    model (str): Automobile model.
    year (int): Year of manufacture.
    mpg (float): Miles per gallon.

    """

    def __init__(self, make, model, year, mpg):
        """
        Initializes the AutoMPG object with make, model, year, and mpg.
        """
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg

    def __repr__(self):
        """
        A detailed string representation of the AutoMPG object.
        """
        return f"AutoMPG(make='{self.make}', model='{self.model}', year=19{self.year}, mpg={self.mpg})"

    def __str__(self):
        """
        A string representation of the AutoMPG object.
        """
        return f"AutoMPG(make='{self.make}', model='{self.model}', year=19{self.year}, mpg={self.mpg})"

    def __eq__(self, other):
        """
        Implements equality comparison between AutoMPG objects.
        """
        if not isinstance(other, AutoMPG):
            return NotImplemented
        return (self.make == other.make and
                self.model == other.model and
                self.year == other.year and
                self.mpg == other.mpg)

    def __lt__(self, other):
        """
        Implements less-than comparison between two AutoMPG objects
        """
        if not isinstance(other, AutoMPG):
            return NotImplemented
        return ((self.make, self.model, self.year, self.mpg) <
                (other.make, other.model, other.year, other.mpg))

    def __hash__(self):
        """
        Returns the hash value of the AutoMPG object.
        """
        return hash((self.make, self.model, self.year, self.mpg))


# Test
if __name__ == "__main__":
    car1 = AutoMPG('Chevrolet', 'Impala', 85, 25.0)
    car2 = AutoMPG('Ford', 'Mustang', 87, 20.0)

    print(car1)  # __str__ string representation
    print(repr(car2))  # __repr__ representation
    print(car1 == car2)  # __eq__ Equality comparison
    print(car1 < car2)  # __it__ Less-than comparison


# Step 2: AutoMPGData class

class AutoMPGData:
    """
    A class that represents the entire AutoMPG data set.

    Attributes:
    -----------
    data(list): A list of AutoMPG objects.

    """

    def __init__(self):
        """
        Constructor that initializes the AutoMPGData object and loads the data.
        """
        self.data = []
        self._load_data()

    def __iter__(self):
        """
        Returns an iterator over the data list.
        """
        return iter(self.data)

    def _load_data(self):
        """
        Loads the cleaned data file and instantiates AutoMPG objects and adds them to the data attribute.
        """
        clean_data_file = 'auto-mpg.clean.txt'
        if not os.path.exists(clean_data_file):
            self._clean_data()

        Record = namedtuple('Record', ['mpg', 'cylinders', 'displacement', 'horsepower',
                                       'weight', 'acceleration', 'model_year', 'origin', 'car_name'])

        with open(clean_data_file, 'r') as file:
            reader = csv.reader(file, delimiter=' ')
            for row in reader:
                if row:
                    record = Record(*filter(None, row))
                    make, *model = record.car_name.split()
                    model = ' '.join(model)
                    self.data.append(AutoMPG(make, model, int(
                        record.model_year), float(record.mpg)))

    def _clean_data(self):
        """
        Cleans the original data file and saves it to a new file.
        """
        original_data_file = 'auto-mpg.data.txt'
        clean_data_file = 'auto-mpg.clean.txt'

        with open(original_data_file, 'r') as infile, open(clean_data_file, 'w') as outfile:
            for line in infile:
                cleaned_line = line.expandtabs().strip()
                outfile.write(cleaned_line + '\n')


# Step 3: Main Function

def main():
    auto_mpg_data = AutoMPGData()
    for record in auto_mpg_data:
        print((record))


if __name__ == "__main__":
    main()
