import numpy as np
import scipy.stats


class MutationParameters:
    """
    Class for coherent parameter definition for Mutation operator.
    """

    def __init__(self, type_of_mutation: str = "Cauchy", mutation_probability: float = .5,
                 mu: float = 0, gamma: float = 1,
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

        self.mu = mu
        self.gamma = gamma

        self.mean = mean
        self.std = std

        self.check()

    def check(self):
        if self.std < 0 or self.gamma < 0:
            if self.std < 0:
                raise WrongParametersError(f"Standard deviation must be non negative (std = {self.std})")
            else:
                raise WrongParametersError(f"Gamma parameter must be non negative (std = {self.gamma})")
        if self.type_of_mutation not in ("Gaussian", "Cauchy"):
            pass #TODO: poprawić


class Mutation:
    def __init__(self, parameters: MutationParameters):
        self.type_of_mutation = parameters.type_of_mutation
        self.parameters = parameters

    def mutate(self, solution):
        """
        Method dedicated to mutating given solution.
        :param solution: Solution of a problem that is going to be mutated
        :return: Mutated solution
        """
        if self.type_of_mutation == "Gaussian":
            return self.__mutate_gaussian(solution)
        elif self.type_of_mutation == "Cauchy":
            return self.__mutate_cauchy(solution)
        elif self.type_of_mutation == "Bit negation":
            return self.__mutate_bit_negation(solution)
        elif self.type_of_mutation == "Random Bit":
            return self.__mutate_random_bit(solution)

    def __mutate_gaussian(self, solution):
        #TODO: poprawić
        solution += np.random.normal(self.parameters.mu, self.parameters.std, solution.shape)
        return solution

    def __mutate_cauchy(self, solution):
        # TODO: poprawić
        solution += scipy.stats.cauchy.rvs(self.parameters.mu, self.parameters.std, solution.shape)
        return solution

    def __mutate_bit_negation(self, solution):
        # TODO: Uzupełnić
        pass

    def __mutate_random_bit(self, solution):
        # TODO: Uzupełnić
        pass


class WrongParametersError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
