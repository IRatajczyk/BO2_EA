import numpy as np
import scipy.stats


class MutationParameters:
    """
    Class for coherent parameter definition for Mutation operator.
    """

    def __init__(self, type_of_mutation:str , mutation_probability: float = .5, mu: float = 0, gamma: float = 1,
                 mean: float = 0, std: float = 1):
        """
        Class initializer for coherent parameter definition for Mutation operator.
        :param type_of_mutation: Specify the desired operator of mutation, possible values: "Cauchy","Gaussian","Bit negation"
        :param mutation_probability: Specify the probability of mutation.
        :param mu: Stands for mu(mean) parameter of Cauchy-Lorenz noice, assuming "Cauchy" mutation
        :param gamma: Stands for gamma(spread-like) parameter of Cauchy-Lorenz noice, assuming "Cauchy" mutation
        :param mean: Stands for mean of gaussian noice, assuming "Gaussian" mutation
        :param std: Stands for standard deviation of gaussian noice, assuming "Gaussian" mutation
        """
        self.type_of_mutation = type_of_mutation
        self.mutation_probability = mutation_probability
        if self.type_of_mutation == "Cauchy":
            self.mu = mu
            self.gamma = gamma
        elif self.type_of_mutation == "Gaussian":
            self.mean = mean
            self.std = std
        elif self.type_of_mutation == "Bit Negation":
            self._bn = None
        elif self.type_of_mutation == "Random Bit":
            self._rb = None


class Mutation:
    def __init__(self, parameters: MutationParameters):
        self.parameters = parameters

    def mutate(self, solution):
        """
        Method dedicated to mutating given solution.
        :param solution: Solution of a problem that is going to be mutated
        :return: Mutated solution
        """
        if self.parameters.type_of_mutation == "Gaussian":
            return self.__mutate_gaussian(solution)
        elif self.parameters.type_of_mutation == "Cauchy":
            return self.__mutate_cauchy(solution)

    def __mutate_gaussian(self, solution):
        solution += np.random.normal(self.parameters.mu, self.parameters.std, solution.shape)
        return solution

    def __mutate_cauchy(self, solution):
        solution += scipy.stats.cauchy.rvs(self.parameters.mu, self.parameters.std, solution.shape)
        return solution
