import unittest
import numpy as np
import utils
import os
import Selection


class SelectionTestCase(unittest.TestCase):
    def test_roulette(self):
        np.random.seed(42)
        population = [[[1, 2, 3, 4], 10], [[5, 6, 7, 8], 90]] * 10

        params = utils.load_config("test_config.json") if os.path.isfile("test_config.json") else dict()
        params["type_of_selection"] = "Roulette"
        sel_param = Selection.SelectionParameters(**params)
        sel = Selection.Selection(sel_param)

        result = sel.select(population)
        true_indices = (7, 19, 15, 11, 3, 3, 1, 17, 12, 14, 1, 19, 17, 5, 3, 3, 6, 11, 9, 5)
        true_val = list(np.array(population)[true_indices, :])
        self.assert_all_true(true_val, result)

    def test_tournament(self):
        np.random.seed(42)
        population = [[[1, 2, 3, 4], 10], [[5, 6, 7, 8], 90]] * 10

        params = utils.load_config("test_config.json") if os.path.isfile("test_config.json") else dict()
        params["type_of_selection"] = "Tournament"
        sel_param = Selection.SelectionParameters(**params)
        sel = Selection.Selection(sel_param)

        result = sel.select(population)
        true_val = [[[5, 6, 7, 8], 90]] * 10
        self.assert_all_true(true_val, result)

    def assert_all_true(self, true_vals, results):
        for true_val, result in zip(true_vals, results):
            true_sol, true_fitness = true_val
            result_sol, result_fitness = result
            assertion = np.abs(np.array(true_sol) - np.array(result_sol)) < np.finfo(np.float32).eps
            self.assertTrue(np.all(assertion))
            self.assertEqual(true_fitness, result_fitness)


if __name__ == '__main__':
    unittest.main()
