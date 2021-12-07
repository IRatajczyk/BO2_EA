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
        # TODO: Uzupełnić
        return

    def __cross_two_points(self, solution1, solution2):
        # TODO: Uzupełnić
        return

    def __cross_average(self, solution1, solution2):
        # TODO: Uzupełnić
        return

    def __cross_convex(self, solution1, solution2):
        # TODO: Uzupełnić
        return

    def __cross_uniform(self, solution1, solution2):
        # TODO: Uzupełnić
        return
