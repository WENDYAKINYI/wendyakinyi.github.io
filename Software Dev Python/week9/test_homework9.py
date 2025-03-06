import unittest
import numpy as np
import math
from Assignment9 import Distributions, NumpyDistribution


# # Assignment 9.4:
# # In a separate file, test_homework9.py, write the necessary unittests for questions 9.1 and 9.2. Take careful consideration to
# # test valid and invalid values for the creation of any of the distributions.


class TestDistributions(unittest.TestCase):
    """
    Test cases for the Distributions class.

    """

    def test_valid_distribution_creation(self):
        """
        Test creating distributions with valid parameters.

        For each valid distribution type, this test case verifies that a
        distribution object can be created with the specified parameters,
        and the attributes of the distribution object are set correctly.

        """
        dist_types = ['normal', 'lognormal', 'laplace']
        for dist_type in dist_types:
            with self.subTest(dist_type=dist_type):
                dist = Distributions(dist=dist_type, mean=0, std=1, size=100)
                self.assertEqual(dist.distribution, dist_type)
                self.assertEqual(dist.mean, 0)
                self.assertEqual(dist.std, 1)
                self.assertEqual(dist.size, 100)
                self.assertEqual(len(dist.samples), 100)

    def test_invalid_distribution_creation(self):
        """
        Test creating distributions with an invalid distribution type.

        This test case verifies that attempting to create a distribution
        object with an invalid distribution type raises a ValueError.

        """
        with self.assertRaises(ValueError):
            Distributions(dist="invalid_dist", mean=0, std=1, size=100)

    def test_normal_distribution_samples(self):
        """
        Test that normal distribution samples have the correct mean and std.


        """
        dist = Distributions(dist="normal", mean=0, std=1, size=1000)
        samples_mean = sum(dist.samples) / len(dist.samples)
        samples_variance = sum((x - samples_mean) **
                               2 for x in dist.samples) / len(dist.samples)
        samples_std = math.sqrt(samples_variance)
        self.assertAlmostEqual(samples_mean, 0, delta=0.1)
        self.assertAlmostEqual(samples_std, 1, delta=0.1)

    def test_lognormal_distribution_samples(self):
        """
        Test that lognormal distribution samples have the correct mean and std.

        """
        mu = 0
        sigma = 1
        expected_mean = math.exp(mu + (sigma ** 2) / 2)
        expected_std = math.sqrt(
            (math.exp(sigma ** 2) - 1) * math.exp(2 * mu + sigma ** 2))
        dist = Distributions(dist="lognormal", mean=mu, std=sigma, size=1000)
        samples_mean = sum(dist.samples) / len(dist.samples)
        samples_variance = sum((x - samples_mean) **
                               2 for x in dist.samples) / len(dist.samples)
        samples_std = math.sqrt(samples_variance)
        self.assertAlmostEqual(samples_mean, expected_mean, delta=0.5)
        self.assertAlmostEqual(samples_std, expected_std, delta=0.5)

    def test_laplace_distribution_samples(self):
        """
        Test that laplace distribution samples have the correct mean and std.

        """
        dist = Distributions(dist="laplace", mean=0, std=1, size=1000)
        samples_mean = sum(dist.samples) / len(dist.samples)
        samples_variance = sum((x - samples_mean) **
                               2 for x in dist.samples) / len(dist.samples)
        samples_std = math.sqrt(samples_variance)
        self.assertAlmostEqual(samples_mean, 0, delta=0.1)
        self.assertAlmostEqual(samples_std, 1, delta=0.1)

        return

# TestNumpy


class TestNumpyDistribution(unittest.TestCase):
    """
    Test cases for the NumpyDistribution class.

    """

    def test_valid_numpy_distribution_creation(self):
        """
        Test creating numpy distributions with valid parameters.

        """
        dist_types = ['normal', 'lognormal', 'laplace']
        for dist_type in dist_types:
            with self.subTest(dist_type=dist_type):
                dist = NumpyDistribution(
                    dist=dist_type, mean=0, std=1, size=100)
                self.assertEqual(dist.distribution, dist_type)
                self.assertEqual(dist.mean, 0)
                self.assertEqual(dist.std, 1)
                self.assertEqual(dist.size, 100)
                self.assertEqual(len(dist.samples), 100)

    def test_invalid_numpy_distribution_creation(self):
        """
        Test creating numpy distributions with an invalid distribution type.

        """
        with self.assertRaises(ValueError):
            NumpyDistribution(dist="invalid_dist", mean=0, std=1, size=100)

    def test_normal_numpy_distribution_samples(self):
        """
        Test that numpy normal distribution samples have the correct mean and std.

        """
        dist = NumpyDistribution(dist="normal", mean=0, std=1, size=1000)
        samples_mean = np.mean(dist.samples)
        samples_std = np.std(dist.samples)
        self.assertAlmostEqual(samples_mean, 0, delta=0.1)
        self.assertAlmostEqual(samples_std, 1, delta=0.1)

    def test_lognormal_numpy_distribution_samples(self):
        """
        Test that numpy lognormal distribution samples have the correct mean and std.

        """
        dist = NumpyDistribution(dist="lognormal", mean=0, std=1, size=1000)
        samples_mean = np.mean(np.log(dist.samples))
        samples_std = np.std(np.log(dist.samples))
        self.assertAlmostEqual(samples_mean, 0, delta=0.1)
        self.assertAlmostEqual(samples_std, 1, delta=0.1)

    def test_laplace_numpy_distribution_samples(self):
        """
        Test that numpy laplace distribution samples have the correct mean and std.

        """
        dist = NumpyDistribution(
            dist="laplace", mean=0, std=1 / np.sqrt(2), size=1000)
        samples_mean = np.mean(dist.samples)
        samples_std = np.std(dist.samples)
        expected_mean = 0
        expected_std = 1 / np.sqrt(2)
        self.assertAlmostEqual(samples_mean, expected_mean, delta=0.1)
        self.assertAlmostEqual(samples_std, expected_std,  delta=0.1)

        return


if __name__ == '__main__':
    unittest.main()
