import numpy as np
from scipy.stats import arcsine


class CrossoverParameters:
    """
    Class for coherent parameter definition for Crossover operator.
    """

    def __init__(self, type_of_crossover: str = "Convex Combination", crossover_probability: float = 0.5,
                 distribution_of_cut: str = "Uniform",
                 alpha_distribution: str = "Uniform"):
        """
        Class initializer for coherent parameter definition for Crossover operator.
        :param type_of_crossover: Specify the desired type of crossover, possible values: "One point", "Two points", "Average", "Convex Combination", "Uniform".
        :param crossover_probability: Specify the probability of crossover.
        :param distribution_of_cut: Specify the desired distribution of cut, possible values: "Uniform"
        :param alpha_distribution: Specify the desired distribution of alpha parameter, assuming convex combination type of crossover. Possible values: "Uniform", "Arcsine"
        """
        self.type_of_crossover = type_of_crossover
        self.crossover_probability = crossover_probability
        self.distribution_of_cut = distribution_of_cut
        self.alpha_distribution = alpha_distribution
        self.check()

    def check(self):
        impl_crossover_types = ("One point", "Two points", "Average", "Convex Combination", "Uniform")
        impl_distribution_of_cut = ("Uniform",)
        impl_alpha_distribution = ("Uniform", "Arcsine")
        if self.type_of_crossover not in impl_crossover_types:
            raise NotImplementedError(f"{self.type_of_crossover} type of crossover not implemented!")
        if not 0 <= self.crossover_probability <= 1:
            raise WrongParametersError(f"Probability value must be in <0, 1>!")
        if self.distribution_of_cut not in impl_distribution_of_cut:
            raise NotImplementedError(f"{self.distribution_of_cut} distribution of cut not implemented!")
        if self.alpha_distribution not in impl_alpha_distribution:
            raise NotImplementedError(f"{self.alpha_distribution} distribution of alpha parameter not implemented!")


class Crossover:

    def __init__(self, parameters: CrossoverParameters):
        self.type_of_crossover = parameters.type_of_crossover
        self.parameters = parameters

    def cross(self, solution1: np.ndarray, solution2: np.ndarray) -> (np.ndarray, np.ndarray):
        if self.type_of_crossover == "One Point":
            return self.__cross_one_point(solution1, solution2)
        elif self.type_of_crossover == "Two Points":
            return self.__cross_two_points(solution1, solution2)
        elif self.type_of_crossover == "Average":
            return self.__cross_average(solution1, solution2)
        elif self.type_of_crossover == "Convex combination":
            return self.__cross_convex(solution1, solution2)
        elif self.type_of_crossover == "Uniform":
            return self.__cross_uniform(solution1, solution2)

    def __cross_one_point(self, solution1: np.ndarray, solution2: np.ndarray) -> (np.ndarray, np.ndarray):
        if self.parameters.distribution_of_cut == "Uniform":
            if solution1.shape != solution2.shape:
                raise ValueError(f"Solution shapes {solution1.shape} and {solution2.shape} don't match!")
            idx = np.random.randint(1, len(solution1))
            x, y = solution1.copy(), solution2.copy()
            x[idx:], y[idx:] = solution2[idx:], solution1[idx:]
            return x, y

    def __cross_two_points(self, solution1: np.ndarray, solution2: np.ndarray) -> (np.ndarray, np.ndarray):
        if self.parameters.distribution_of_cut == "Uniform":
            if solution1.shape != solution2.shape:
                raise ValueError(f"Solution shapes {solution1.shape} and {solution2.shape} don't match!")
            idx1, idx2 = np.sort(np.random.choice(range(1, len(solution1)), size=2, replace=False))
            x, y = solution1.copy(), solution2.copy()
            x[idx1:idx2], y[idx1:idx2] = solution2[idx1:idx2], solution1[idx1:idx2]
            return x, y

    def __cross_average(self, solution1: np.ndarray, solution2: np.ndarray) -> (np.ndarray, np.ndarray):
        if solution1.shape != solution2.shape:
            raise ValueError(f"Solution shapes {solution1.shape} and {solution2.shape} don't match!")
        x = (0.5 * solution1 + 0.5 * solution2).astype(int)
        return x #, x (???)

    def __cross_convex(self, solution1: np.ndarray, solution2: np.ndarray) -> (np.ndarray, np.ndarray):
        if solution1.shape != solution2.shape:
            raise ValueError(f"Solution shapes {solution1.shape} and {solution2.shape} don't match!")
        if self.parameters.alpha_distribution == "Uniform":
            alpha = np.random.rand()
        if self.parameters.alpha_distribution == "Arcsine":
            alpha = arcsine.rvs()
        x = (alpha * solution1 + (1 - alpha) * solution2).astype(int)
        y = ((1 - alpha) * solution1 + alpha * solution2).astype(int)
        return x, y

    def __cross_uniform(self, solution1: np.ndarray, solution2: np.ndarray) -> (np.ndarray, np.ndarray):
        if solution1.shape != solution2.shape:
            raise ValueError(f"Solution shapes {solution1.shape} and {solution2.shape} don't match!")
        pat = np.random.randint(2, size=len(solution1))
        pat_neg = 1 - pat
        x = (solution1 * pat + solution2 * pat_neg).astype(int)
        y = (solution1 * pat_neg + solution2 * pat).astype(int)
        return x, y


class WrongParametersError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
