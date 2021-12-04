class CrossoverParameters:
    """
    Class for coherent parameter definition for Crossover operator.
    """
    def __init__(self, type_of_crossover: str, crossover_probability: float, distribution_of_cut: str = "Uniform",
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
        if self.type_of_crossover == "One Point":
            self.distribution_of_cut = distribution_of_cut
        elif self.type_of_crossover == "Average":
            pass
        elif self.type_of_crossover == "Convex Combination":
            self.alpha_distribution = alpha_distribution


class Crossover:
    def __init__(self, parameters: CrossoverParameters):
        self.type_of_crossover = parameters.type_of_crossover
        self.parameters = parameters

    def cross(self, solution1, solution2):
        if self.type_of_crossover == "One Point":
            return self.__cross_one_point(solution1, solution2)

    def __cross_one_point(self,solution1, solution2):
        return



