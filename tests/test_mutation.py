import unittest
import utils
import numpy as np
import os
import Mutation


class MutationTestCase(unittest.TestCase):
    def test_cauchy(self):
        np.random.seed(42)
        sol = np.array([0, 2, 4, 6, 8, 10])

        params = utils.load_config("test_config.json") if os.path.isfile("test_config.json") else dict()
        params["type_of_mutation"] = "Cauchy"
        mut_params = Mutation.MutationParameters(**params)
        mut = Mutation.Mutation(mut_params)

        result = mut.mutate(sol)
        true_val = np.array([0, 8, 4, 6, 6, 8])
        self.assert_all_true(true_val, result)

    def test_gaussian(self):
        np.random.seed(42)
        sol = np.array([0, 2, 4, 6, 8, 10])

        params = utils.load_config("test_config.json") if os.path.isfile("test_config.json") else dict()
        params["type_of_mutation"] = "Gaussian"
        mut_params = Mutation.MutationParameters(**params)
        mut = Mutation.Mutation(mut_params)

        result = mut.mutate(sol)
        true_val = np.array([0, 1, 4, 7, 7, 9])
        self.assert_all_true(true_val, result)

    def assert_all_true(self, true_val, result):
        assertion = np.abs(true_val - result) < np.finfo(np.float32).eps
        self.assertTrue(np.all(assertion))


if __name__ == '__main__':
    unittest.main()
