# Import the Car class from homework4
import unittest
from hw4 import Car

# Create car1 instance
car1 = Car("yellow", 2010, "Ferrari", "LaFerrari", 3, "gas", 245, 6)

# Create car2 instance
car2 = Car("red", 2010, "Lamborghini", "Aventador", 3, "gas", 252, 6.2)


class TestCarMethods(unittest.TestCase):
    def test_betterGasMileage(self):

        # Calculate betterGasMileage for car1 and car2
        better_mileage1 = car1.betterGasMileage()
        better_mileage2 = car2.betterGasMileage()

        # Assert that the betterGasMileage values are correct with a delta tolerance
        self.assertAlmostEqual(better_mileage1, better_mileage2,
                               delta=0.01, msg="Gas mileage comparison failed")

    def test_changeColor(self):
        # Create a car1 instance with the initial color
        initial_color = "yellow"
        car1 = Car(initial_color, 2010, "Ferrari",
                   "LaFerrari", 3, "gas", 245, 6)

        # Check if the initial color matches
        self.assertEqual(car1.color, initial_color,
                         f"Initial color should be {initial_color}")

        # Change the car's color to blue
        new_color = "blue"
        car1.changeColor(new_color)

        # Check if the car's color is now blue
        self.assertEqual(car1.color, new_color,
                         f"Car's color should be {new_color}")

    def test_mpg(self):

        # Calculate better gas mileage for both cars
        better_mileage1 = car1.betterGasMileage()
        better_mileage2 = car2.betterGasMileage()

        # Check that car2 has better mileage than car1
        self.assertGreater(better_mileage2, better_mileage1,
                           "Car2 should have better mileage than Car1")


if __name__ == "__main__":
    unittest.main()
