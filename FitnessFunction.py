import numpy as np


class FitnessFunctionParameters:
    def __init__(self, name_of_fitness_function: str = "TimeSeriesCovidProblem", x=0, y=0, z=0):
        self.name_of_fitness_function = name_of_fitness_function
        if name_of_fitness_function == "TimeSeriesCovidProblem":
            self.X = x
            self.Y = y
            self.Z = z


class FitnessFunction:
    def __init__(self, parameters: FitnessFunctionParameters):
        self.parameters = parameters

    def calculate_fitness(self, solution): #-> float:
        if self.parameters.name_of_fitness_function == "TimeSeriesCovidProblem":
            return self.__calculate_cov19_shit(solution)

    def __calculate_cov19_shit(self, solution):
        return np.sum(np.sum(solution))

