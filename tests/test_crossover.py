import unittest
import Crossover
import utils
import numpy as np
import os


class CrossoverTestCase(unittest.TestCase):
    def test_cross_one_point(self):
        np.random.seed(42)
        s1 = np.array([2, 4, 6, 8])
        s2 = np.array([1, 3, 5, 7])

        params = utils.load_config("test_config.json") if os.path.isfile("test_config.json") else dict()
        params["type_of_crossover"] = "One Point"
        X_param = Crossover.CrossoverParameters(**params)
        X = Crossover.Crossover(X_param)

        result = X.cross(s1, s2)
        true_val = np.array([2, 4, 6, 7]), np.array([1, 3, 5, 8])
        self.assert_all_true(true_val, result)

    def test_cross_two_points(self):
        np.random.seed(42)
        s1 = np.array([2, 4, 6, 8])
        s2 = np.array([1, 3, 5, 7])

        params = utils.load_config("test_config.json") if os.path.isfile("test_config.json") else dict()
        params["type_of_crossover"] = "Two Points"
        X_param = Crossover.CrossoverParameters(**params)
        X = Crossover.Crossover(X_param)

        result = X.cross(s1, s2)
        true_val = np.array([2, 3, 6, 8]), np.array([1, 4, 5, 7])
        self.assert_all_true(true_val, result)

    def test_convex_combination(self):
        np.random.seed(42)
        s1 = np.array([2, 4, 6, 8, 10])
        s2 = np.array([1, 3, 5, 7, 9])

        params = utils.load_config("test_config.json") if os.path.isfile("test_config.json") else dict()
        params["type_of_crossover"] = "Convex Combination"
        X_param = Crossover.CrossoverParameters(**params)
        X = Crossover.Crossover(X_param)

        result = X.cross(s1, s2)
        true_alpha = 0.3745401188473625
        true_val = (true_alpha * s1 + (1 - true_alpha) * s2).astype(int), ((1 - true_alpha) * s1 + true_alpha * s2).astype(int)
        self.assert_all_true(true_val, result)

    def test_cross_uniform(self):
        np.random.seed(42)
        s1 = np.array([2, 4, 6, 8, 10, 12])
        s2 = np.array([1, 3, 5, 7, 9, 11])

        params = utils.load_config("test_config.json") if os.path.isfile("test_config.json") else dict()
        params["type_of_crossover"] = "Uniform"
        X_param = Crossover.CrossoverParameters(**params)
        X = Crossover.Crossover(X_param)

        result = X.cross(s1, s2)
        true_val = np.array([1, 4, 5, 7, 9, 12]), np.array([2, 3, 6, 8, 10, 11])
        self.assert_all_true(true_val, result)

    def assert_all_true(self, true_vals, results):
        for true_val, result in zip(true_vals, results):
            assertion = np.abs(true_val - result) < np.finfo(np.float32).eps
            self.assertTrue(np.all(assertion))


if __name__ == '__main__':
    unittest.main()
