import numpy as np
from numpy.random import default_rng


class SolutionParameters:
    def __init__(self, problem_name="TSOCOV19D", create_feasible: bool = True, solution_size: int = 365,
                 L_limit: int = 0, DL_limit: int = 0, L0: int = 0, **kwargs):
        self.problem_name = problem_name
        if self.problem_name == "TSOCOV19D":
            self.solution = np.array(solution_size)
            self.solution_size = solution_size
            self.create_feasible = create_feasible
            self.L_limit = L_limit
            self.DL_limit = DL_limit
            self.L0 = L0

            self.check()

    def check(self):
        if self.L_limit >= 0 and self.DL_limit >= 0:
            return True
        else:
            if self.L_limit < 0:
                raise WrongParametersError(f"Lower Workers limit should be non-negative (current limit is {self.L_limit})!")
            else:
                raise WrongParametersError(f"Upper increase limit of workers should not be negative (current limit is {self.DL_limit}!")


class Solution:
    def __init__(self, parameters: SolutionParameters):
        self.problem_name = parameters.problem_name
        self.parameters = parameters
        self.rng = default_rng()

    def initialize_solution(self):
        if self.problem_name == "TSOCOV19D":
            if self.parameters.create_feasible:
                return self.__create_feasible_TSOCOV()
            else:
                return self.__create_non_feasible_TSOCOV()

    def check_feasibility(self, solution) -> bool:
        if self.problem_name == "TSOCOV19D":
            return self.__check_feasible_TSOCOV19D(solution)

    def cast_feasible(self, solution):
        solution[0] = solution[0] if solution[0] <= self.parameters.DL_limit else self.parameters.DL_limit
        solution[0] = self.parameters.L_limit - self.parameters.L0 if self.parameters.L0 + solution[0] < self.parameters.L_limit else solution[0]
        for i in range(1, self.parameters.solution_size):
            solution[i] = solution[i] if solution[i] <= self.parameters.DL_limit else self.parameters.DL_limit
            solution[i] = self.parameters.L_limit - (np.cumsum(solution)[i-1] + self.parameters.L0) if np.cumsum(solution)[i-1] + self.parameters.L0 + solution[i] < self.parameters.L_limit else solution[i]
        return solution

    def get_solution(self, solution):
        return np.cumsum(solution) + self.parameters.L0

    def __create_feasible_TSOCOV(self):
        solution = np.zeros(self.parameters.solution_size)
        for i in range(self.parameters.solution_size):
            limit = self.parameters.L0 + np.cumsum(solution)[i] if i else self.parameters.L0
            solution[i] = self.rng.integers(self.parameters.L_limit - limit, self.parameters.DL_limit)
        return solution

    def __create_non_feasible_TSOCOV(self):
        solution = np.zeros(self.parameters.solution_size)
        for i in range(self.parameters.solution_size):
            solution[i] = self.rng.integers(-10000, 10000)
        return solution

    def __check_feasible_TSOCOV19D(self, solution) -> bool:
        return np.all(np.cumsum(solution)+self.parameters.L0 >= self.parameters.L_limit) and np.all(solution <= self.parameters.DL_limit)


class WrongParametersError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
