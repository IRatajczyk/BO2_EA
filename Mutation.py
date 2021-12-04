import numpy as np
import scipy.stats


class MutationParameters:
    def __init__(self, type_of_mutation, mutation_probability, mu=0, gamma=1, mean=0, std=1):
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
