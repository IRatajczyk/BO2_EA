import unittest
import Crossover
import utils
import numpy as np
import os


class CrossoverTestCase(unittest.TestCase):
    def test_cross_one_point(self):
        params = utils.load_config("test_config.json") if os.path.isfile("test_config.json") else dict()
        X_param = Crossover.CrossoverParameters(**params)
        X = Crossover.Crossover(X_param)
        s1 = np.array([2, 4, 6, 8])
        s2 = np.array([1, 3, 5, 7])

        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
