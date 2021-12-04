import numpy as np


class SolutionParameters:
    def __init__(self, problem_name="TSOCOV19", create_feasible: bool = True, solution_length: int = 365):
        self.problem_name = problem_name
        if self.problem_name == "TSOCOV19":
            self.solution = np.array(solution_length)
            self.solution_length = solution_length
            self.create_feasible = create_feasible


class Solution:
    def __init__(self, parameters: SolutionParameters):
        self.problem_name = parameters.problem_name
        self.parameters = parameters

    def initialize_solution(self):
        if self.problem_name == "TSOCOV19":
            if self.parameters.create_feasible:
                return self.__create_feasible_TSOCOV()
            else:
                return self.__create_non_feasible_TSOCOV()


    def check_feasibility(self, solution) -> bool:
        if self.problem_name == "TSOCOV19":
            return False  # TODO: uzupelnic

    def __create_feasible_TSOCOV(self):
        return

    def __create_non_feasible_TSOCOV(self):
        return
