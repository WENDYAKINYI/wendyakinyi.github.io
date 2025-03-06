'''
COMP 3006
Homework 9 - Numpy

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
# --------------------------------------------------------------------------#

# Assignment 9.1
# Create a class, called Distributions, that has the following attributes : distribution, mean, standard deviation and size.
# It should have a constructor, __str__ method and the ability to generate a normal distribution, lognormal and laplace distributions
# based on the distribution attribute.
# For example:
# my_distribution = Distributions(dist="lognormal", mean=1, std=5, samples=100000)
# should be a lognormal distribution with a mean of 1, standard deviation of 5 and have 100000 samples from the distribution


import numpy as np
import random
import math


class Distributions:
    """
    A class to represent different statistical distributions.

    Attributes:
    -----------
    distribution(str) : The type of distribution (normal, lognormal, laplace).
    mean (float) : The mean of the distribution.
    std (float):The standard deviation of the distribution.
    size (int):The number of samples to generate from the distribution.

    Methods:
    --------
    __str__():Provides a string representation of the distribution object.
    generate_samples():Generates samples based on the specified distribution type and stores them in the `samples` attribute.

    """

    def __init__(self, dist, mean, std, size):
        """
        Constructs all the necessary attributes for the Distributions object.

        Parameters:
        -----------
        dist (str): The type of distribution (normal, lognormal, laplace).
        mean (float): The mean of the distribution.
        std (float): The standard deviation of the distribution.
        samples (int): The number of samples to generate from the distribution.

        """
        self.distribution = dist
        self.mean = mean
        self.std = std
        self.size = size
        self.samples = self.generate_samples()

    def __str__(self):
        """
        Provides a string representation of the Distributions object.

        Returns:
        --------
        str : A string describing the distribution, its mean, standard deviation, and sample size.

        """
        return f"Distribution: {self.distribution}, Mean: {self.mean}, Std: {self.std}, Size: {self.size}"

    def generate_samples(self):
        """
        Generates samples based on the specified distribution type.

        Returns:
        --------
        list : A list of samples generated from the specified distribution.

        """
        if self.distribution == "normal":
            return [self.mean + self.std * math.sqrt(-2 * math.log(random.random())) * math.cos(2 * math.pi * random.random()) for _ in range(self.size)]
        elif self.distribution == "lognormal":
            return [math.exp(self.mean + self.std * random.gauss(0, 1)) for _ in range(self.size)]
        elif self.distribution == "laplace":
            return [random.gauss(self.mean, self.std / math.sqrt(2)) + random.gauss(self.mean, self.std / math.sqrt(2)) for _ in range(self.size)]
        else:
            raise ValueError("Invalid distribution specified")


if __name__ == "__main__":

    my_normal_distribution = Distributions(
        dist="normal", mean=1, std=5, size=100000)
    print(my_normal_distribution)
    print(f"10 samples from the normal distribution: {
          my_normal_distribution.samples[:10]}")

    my_log_distribution = Distributions(
        dist="lognormal", mean=1, std=5, size=100000)
    print(my_log_distribution)
    print(f"10 samples from the lognormal distribution: {
          my_log_distribution.samples[:10]}")

    my_lap_distribution = Distributions(
        dist="laplace", mean=1, std=5, size=100000)
    print(my_lap_distribution)
    print(f"10 samples from the laplace distribution: {
          my_lap_distribution.samples[:10]}")


# # # Assignment 9.2:
# # # Repeat the first part, this time calling the class NumpyDistribution, using only numpy methods
# # # Hint: https://numpy.org/doc/1.22/, you may want to looks at using args and kwargs


class NumpyDistribution:
    """
    A class to represent different statistical distributions using NumPy.

    Attributes:
    -----------
    distribution (str): The type of distribution (normal, lognormal, laplace).
    mean (float) :The mean of the distribution.
    std (float) : The standard deviation of the distribution.
    size (int) : The number of samples to generate from the distribution.
    samples (np.ndarray) : The array of samples generated from the specified distribution.

    Methods:
    --------
    __str__(): Provides a string representation of the distribution object.
    generate_samples(): Generates samples based on the specified distribution type using NumPy and stores them in the `samples` attribute.
    """

    def __init__(self, dist, mean, std, size):
        """
        Constructs all the necessary attributes for the NumpyDistribution object.

        Parameters:
        -----------
        dist (str) :The type of distribution (normal, lognormal, laplace).
        mean (float):The mean of the distribution.
        std (float): The standard deviation of the distribution.
        size (int): The number of samples to generate from the distribution.
        """
        self.distribution = dist
        self.mean = mean
        self.std = std
        self.size = size
        self.samples = self.generate_samples()

    def __str__(self):
        """
        Provides a string representation of the NumpyDistribution object.

        Returns:
        --------
        str : A string describing the distribution, its mean, standard deviation, and sample size.
        """
        return f"NumpyDistributions(self.dist='{self.distribution}', self.mean={self.mean}, self.std={self.std}, self.samples={self.size})"

    def generate_samples(self):
        """
        Generates samples based on the specified distribution type using NumPy and stores them in the `samples` attribute.

        Returns:
        --------
        np.ndarray : An array of samples generated from the specified distribution.
        """
        if self.distribution == "normal":
            return np.random.normal(loc=self.mean, scale=self.std, size=self.size)
        elif self.distribution == "lognormal":
            return np.random.lognormal(mean=self.mean, sigma=self.std, size=self.size)
        elif self.distribution == "laplace":
            return np.random.laplace(loc=self.mean, scale=self.std / np.sqrt(2), size=self.size)
        else:
            raise ValueError("Invalid distribution specified")


if __name__ == "__main__":
    np_normal_distribution = NumpyDistribution(
        dist="normal", mean=1, std=5, size=10000)
    print(np_normal_distribution)
    print(f"10 samples from the (numpy) normal distribution: {
          np_normal_distribution.samples[:10]}")

    np_log_distribution = NumpyDistribution(
        dist="lognormal", mean=1, std=5, size=10000)
    print(np_log_distribution)
    print(f"10 samples from the (numpy) lognormal distribution: {
          np_log_distribution.samples[:10]}")

    np_lap_distribution = NumpyDistribution(
        dist="laplace", mean=1, std=5, size=10000)
    print(np_lap_distribution)
    print(f"10 samples from the (numpy) laplace distribution: {
          np_lap_distribution.samples[:10]}")
