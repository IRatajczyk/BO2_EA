import numpy as np


class CrossoverParameters:
    """
    Class for coherent parameter definition for Crossover operator.
    """

    def __init__(self, type_of_crossover: str = "Convex Combination", crossover_probability: float = 0.5,
                 distribution_of_cut: str = "Uniform",
                 alpha_distribution: str = "Uniform"):
        """
        Class initializer for coherent parameter definition for Crossover operator.
        :param type_of_crossover:
        :param crossover_probability:
        :param distribution_of_cut:
        :param alpha_distribution:
        """
        self.type_of_crossover = type_of_crossover
        self.crossover_probability = crossover_probability
        self.distribution_of_cut = distribution_of_cut
        self.alpha_distribution = alpha_distribution

        self.check()

    def check(self):
        # TODO: Uzupełnić
        pass


class Crossover:

    def __init__(self, parameters: CrossoverParameters):
        self.type_of_crossover = parameters.type_of_crossover
        self.parameters = parameters

    def cross(self, solution1, solution2):
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

    def __cross_one_point(self, solution1, solution2):
        if self.parameters.distribution_of_cut == "Uniform":
            if solution1.shape != solution2.shape:
                raise ValueError(f"Solution shapes {solution1.shape} and {solution2.shape} don't match!")
            idx = np.random.randint(1, len(solution1))
            x, y = solution1.copy(), solution2.copy()
            x[idx:], y[idx:] = solution2[idx:], solution1[idx:]
            return x, y
        raise NotImplementedError(f"Crossing not implemented for {self.parameters.distribution_of_cut}!")

    def __cross_two_points(self, solution1, solution2):
        if self.parameters.distribution_of_cut == "Uniform":
            if solution1.shape != solution2.shape:
                raise ValueError(f"Solution shapes {solution1.shape} and {solution2.shape} don't match!")
            idx1, idx2 = np.sort(np.random.choice(range(1, len(solution1)), size=2, replace=False))
            x, y = solution1.copy(), solution2.copy()
            x[idx1:idx2], y[idx1:idx2] = solution2[idx1:idx2], solution1[idx1:idx2]
            return x, y
        raise NotImplementedError(f"Crossing not implemented for {self.parameters.distribution_of_cut}!")

    def __cross_average(self, solution1, solution2):
        if self.parameters.distribution_of_cut == "Uniform":
            if solution1.shape != solution2.shape:
                raise ValueError(f"Solution shapes {solution1.shape} and {solution2.shape} don't match!")
            x = (0.5 * solution1 + 0.5 * solution2).astype(int)
            return x, x
        raise NotImplementedError(f"Crossing not implemented for {self.parameters.distribution_of_cut}!")

    def __cross_convex(self, solution1, solution2):
        if self.parameters.distribution_of_cut == "Uniform":
            if solution1.shape != solution2.shape:
                raise ValueError(f"Solution shapes {solution1.shape} and {solution2.shape} don't match!")
            alpha = np.random.rand()
            x = (alpha * solution1 + (1 - alpha) * solution2).astype(int)
            y = ((1 - alpha) * solution1 + alpha * solution2).astype(int)
            return x, y
        raise NotImplementedError(f"Crossing not implemented for {self.parameters.distribution_of_cut}!")

    def __cross_uniform(self, solution1, solution2):
        if self.parameters.distribution_of_cut == "Uniform":
            if solution1.shape != solution2.shape:
                raise ValueError(f"Solution shapes {solution1.shape} and {solution2.shape} don't match!")
            pat = np.random.randint(2, size=len(solution1))
            pat_neg = 1 - pat
            x = (solution1 * pat + solution2 * pat_neg).astype(int)
            y = (solution1 * pat_neg + solution2 * pat).astype(int)
            return x, y
        raise NotImplementedError(f"Crossing not implemented for {self.parameters.distribution_of_cut}!")
