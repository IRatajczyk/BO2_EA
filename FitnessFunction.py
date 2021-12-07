import numpy as np


class FitnessFunctionParameters:
    """
    Class for coherent parameter definition for Fitness Function.
    """

    def __init__(self, name_of_fitness_function: str = "TimeSeriesCovidProblemNaive", worker_cost: float = 0,
                 death_probability: float = 0, cost_of_death: float = 0, training_cost: float = 0,
                 swabs_per_day: int = 0,
                 delay=0, cost_of_non_immediate_swab: float = 0, days_for_swab: int = 14, delayed_cost: bool = True,
                 time_series=None, learning_type: str = None, learning_parameter: float = 0):
        """
        Class initializer for coherent parameter definition for Fitness Function.
        :param name_of_fitness_function: Specify the desired Fitness Function, possible values: "TimeSeriesCovidProblem"
        ,"TimeSeriesCovidProblemNaive"
        :param worker_cost: cost of every worker per day
        :param death_probability: death probability of unswabbed patient
        :param cost_of_death: expected cost of one death of man
        :param training_cost: cost of training one labourer
        :param swabs_per_day: amount of swabs that labourer can proceed during one day
        :param delay: TBA
        """
        self.name_of_fitness_function = name_of_fitness_function
        self.learning_type = learning_type

        self.worker_cost = worker_cost
        self.cost_of_death = cost_of_death
        self.death_probability = death_probability
        self.training_cost = training_cost
        self.swabs_per_day = swabs_per_day
        self.delay = delay
        self.time_series = time_series
        self.cost_of_non_immediate_swab = death_probability * cost_of_death / 2 if delayed_cost else cost_of_non_immediate_swab
        self.days_for_swab = days_for_swab

        self.learning_parameter = learning_parameter

        self.check()

    def check(self):
        if not (0 <= self.death_probability <= 1):
            raise WrongParametersError(
                f"Probability should be less than 1 and greater than 0 (currently p = {self.death_probability})")


class FitnessFunction:
    def __init__(self, parameters: FitnessFunctionParameters):
        self.parameters = parameters

    def calculate_fitness(self, solution) -> float:
        if self.parameters.name_of_fitness_function == "TimeSeriesCovidProblem":
            return self.__calculate_cov19_ff(solution)
        elif self.parameters.name_of_fitness_function == "TimeSeriesCovidProblemNaive":
            return self.__calculate_cov19_naive_ff(solution)

    def __calculate_cov19_ff(self, solution) -> float:
        L = np.cumsum(solution)
        chi = self.parameters.time_series
        X = self.parameters.worker_cost
        Y = self.parameters.cost_of_non_immediate_swab
        Z = self.parameters.training_cost
        N = self.parameters.swabs_per_day
        J = 0
        cumulative_list = [0 for _ in range(self.parameters.days_for_swab)]
        for i in range(solution.size):
            J += X * L[i] + Z * np.max(solution[i], 0)
            for j in range(self.parameters.days_for_swab - 1, 0, -1):
                J += cumulative_list[j] * (2 ** (-j)) * Y
                cumulative_list[j] = cumulative_list[j - 1]
            patients_left = 0
            if chi[i] - N * L[i] < 0:
                to_swab = N * L[i] - chi[i]
                delayed_patients = 0
                j = self.parameters.days_for_swab - 1
                while delayed_patients < to_swab and j > 0:
                    while delayed_patients < to_swab and cumulative_list[j] > 0:
                        delayed_patients += 1
                        cumulative_list[j] -= 1
                    j -= 1
            elif chi[i] - N * L[i] > 0:
                patients_left = chi[i] - N * L[i]
            cumulative_list[0] = patients_left
        return J

    def __calculate_cov19_naive_ff(self, solution) -> float:
        L = np.cumsum(solution)
        chi = self.parameters.time_series
        X = self.parameters.worker_cost
        Y = self.parameters.death_probability * self.parameters.cost_of_death
        Z = self.parameters.training_cost
        N = self.parameters.swabs_per_day
        J = np.sum(X * L + Y * np.maximum((chi - N * L), 0) + Z * np.maximum(solution, 0))
        return J


class WrongParametersError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
