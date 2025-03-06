import os
import csv
from collections import namedtuple
from program.custom_logger import my_logger


class AutoMPG:
    """
    This class defines an AutoMPG (car) object

    Attributes:
    -----------------------------------------------
        make (str): manufacturer of the car
        model (str): car model
        year (int): model year
        mpg (float): miles per gallon

    Methods:
    -----------------------------------------------
        __init__: constructor of the AutoMPG class
        __repr__: calls __str__ method
        __str__: returns string representation of an instance
        with the form AutoMPG(make, model, year, mpg)
        __eq__: compares make, model, year and mpg for equality
        __lt__: checks that all 4 attributes are less than all 4
        attributes of an object of the same class
        __hash__: creates unique hashing value using a tuple of 
        all 4 attributes
    """

    def __init__(self, make: str, model: str, year: int, mpg: float) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg

    def __repr__(self):
        return self.__str__()

    def __str__(self) -> str:
        return f"AutoMPG({self.make}, {self.model}, {self.year}, {self.mpg})"

    def __eq__(self, other) -> bool:
        if type(self) == type(other):
            return (self.make, self.model, self.year, self.mpg) == \
                (other.make, other.model, other.year, other.mpg)
        else:
            return NotImplemented

    def __lt__(self, other):
        if type(self) == type(other):
            if (self.make, self.model, self.year, self.mpg) == \
                    (other.make, other.model, other.year, other.mpg):
                return False
            elif (self.make > other.make) or (self.model > other.model) or\
                    (self.year > other.year) or (self.mpg > other.mpg):
                return False
            else:
                return True
        else:
            return NotImplemented

    def __hash__(self) -> int:
        return hash((self.make, self.model, self.year, self.mpg))


class AutoMPGData:
    """
    This class will read in a data file, clean it, and generate a list
    of AutoMPG objects.
    Attributes:
    -----------------------------------------------
        data (list[AutoMPG]): list of AutoMPG objects

    Methods:
    -----------------------------------------------
        __init__: constructor of the AutoMPGData class. Loads data file
        __iter__: creates an iterator over the data attribute
        _load_data: reads in clean data file, if the file doesn't exist
        calls _clean_data to generate clean data file. When loading clean
        data, it creates a namedtuple 'Record' for each row and extracts 
        values needed to instantiate a series of AutoMPG objects which are
        loaded into the list attribute data.
        _clean_data: loads in original data file, expands tabs, removes
        unnecessary characters and creates auto-mpg.clean.txt file.
        sort_data: sorts the data by year or by mpg
        save_data: saves the data to a file with given file_path
    """

    def __init__(self,  logger, sort_year=False, sort_mpg=False, sort_year_mpg=False):
        self.data = []
        self._load_data()
        self.sort_year = sort_year
        self.sort_mpg = sort_mpg
        self.sort_year_mpg = sort_year_mpg
        self.logger = logger
        self.logger.debug("Data loaded.")  # Log message after data load
        return

    def __iter__(self):
        return iter(self.data)

    def _load_data(self):
        """
        Loads data from a clean data file and loads each observation into the
        data attribute
        """
        # Create clean data file is it doesn't exist:
        if not os.path.exists("auto-mpg.clean.txt"):
            self._clean_data()

        # Create namedtuple for storing records
        record_tuple = namedtuple("Record", ["mpg", "cylinders", "displacement",
                                             "horsepower", "weigt", "acceleration", "year", "origin", "name"])

        # Load data from clean data file
        with open("auto-mpg.clean.txt", "r") as rf:
            contents = csv.reader(rf, delimiter=" ")
            for line in contents:
                # Create Record tuple:
                line_record = record_tuple(*line)

                # Extract make, model, year, mpg from Record
                try:
                    make, model = line_record.name.split(maxsplit=1)
                except ValueError:
                    continue
                year = int("19" + line_record.year)
                mpg = float(line_record.mpg)

                self.data.append(AutoMPG(make, model, year, mpg))
        return

    def _clean_data(self):
        """
        Reads in dirty data, expands tabs and standardizes data rows
        """
        with open("auto-mpg.clean.txt", "w+") as wf:
            with open("auto-mpg.data.txt", "r") as rf:
                contents = csv.reader(rf)
                for line in contents:
                    wf.writelines(" ".join(line[0].split(maxsplit=8)) + "\n")
        return

    def sort_data(self):
        """
        Sorts the data by year or by mpg.

        Args:
        -----------------------------------------------
            by_year (bool): Whether to sort the data by year.
            by_mpg (bool): Whether to sort the data by mpg.
        """
        if self.sort_year_mpg:
            self.data.sort(key=lambda x: (x.year, x.mpg))
            self.logger.debug("Data sorted by year and mpg.")
        elif self.sort_year:
            self.data.sort(key=lambda x: x.year)
            self.logger.debug("Data sorted by year.")
        elif self.sort_mpg:
            self.data.sort(key=lambda x: x.mpg)
            self.logger.debug("Data sorted by mpg.")
        else:
            self.logger.debug("Data not sorted.")
        return

    def save_data(self, file_path):
        """
        Saves the data to a file with given file_path.

        Args:
        -----------------------------------------------
            file_path (str): The file path where data will be saved.
        """
        sort_criteria = ""
        if self.sort_year:
            sort_criteria = "year"
        if self.sort_mpg:
            sort_criteria = "mpg"
        if self.sort_year_mpg:
            sort_criteria = "year_mpg"

        file_name = (
            f"auto.data.{sort_criteria}.txt" if sort_criteria else "auto.data.txt")
        full_path = os.path.join(file_path, file_name)

        with open(full_path, "w") as f:
            for item in self.data:
                f.write(f"{item}\n")

        self.logger.debug(f"Data saved, sorted by {sort_criteria}!!!")
        return


def main():
    """
    Instantiates an AutoMPGData object and iterates over the data 
    list attribute. 
    Here is a recipe for some vegan "chicken" nuggets made with tofu. I would 
    recommend increasing the measurements for the sauce by 50%.
    https://www.youtube.com/watch?v=r4HAeSiNg-o&list=PLQS76C4HKZ770DiEhed-0CFboVmj8bJHB&index=19&t=300s

    Args:
        None

    Returns:
        None
    """
    auto_list = AutoMPGData()

    for car in auto_list:
        print(car)


if __name__ == "__main__":
    main()
