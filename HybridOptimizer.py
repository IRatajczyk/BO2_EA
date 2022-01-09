import numpy as np
import Solution
import FitnessFunction


class HybridOptimizerParameters:
    def __init__(self, type_of_hybrid: str = "Feasible extremely greedy", **kwargs):
        self.type_of_hybrid = type_of_hybrid

    def check(self):
        if self.type_of_hybrid not in ("Feasible greedy",):
            raise NotImplementedError(f"Hybrid Optimizer not implemented for {self.type_of_hybrid} type!")


class HybridOptimizer:
    def __init__(self, parameters: HybridOptimizerParameters, solution: Solution.Solution, fitness_function: FitnessFunction.FitnessFunction):
        self.type_of_hybrid = parameters.type_of_hybrid
        self.parameters = parameters
        self.solution = solution
        self.solution_parameters = solution.parameters
        self.fitness_function = fitness_function

    def optimize(self, solution):
        if self.type_of_hybrid == "Feasible greedy":
            return self.__feasible_greedy_optimizer(solution)
        if self.type_of_hybrid == "Feasible extremely greedy":
            return self.__feasible_extremely_greedy_optimizer(solution)

    def __feasible_greedy_optimizer(self, solution):
        ff = self.fitness_function.calculate_fitness(solution)
        DL = self.solution_parameters.DL_limit
        for idx in range(1, self.solution_parameters.solution_size):
            cumulative_sum = np.cumsum(solution)[idx-1] + self.solution_parameters.L0
            for d in range(int(-cumulative_sum), DL):
                old_sol = solution.copy()
                solution[idx] = d
                new_sol = solution if self.solution.check_feasibility(solution) else old_sol
                new_ff = self.fitness_function.calculate_fitness(new_sol)
                (solution, ff) = (new_sol, new_ff) if new_ff < ff else (old_sol, ff)
        return solution, ff

    def __feasible_extremely_greedy_optimizer(self, solution):
        change = True
        ff = self.fitness_function.calculate_fitness(solution)
        DL = self.solution_parameters.DL_limit
        while change:
            change = False
            for idx in range(1, self.solution_parameters.solution_size - 1):
                cumulative_sum = np.cumsum(solution)[idx-1] + self.solution_parameters.L0
                for d in range(-cumulative_sum, DL):
                    old_sol = solution.copy()
                    solution[idx] = d
                    new_sol = solution if self.solution.check_feasibility(solution) else old_sol
                    new_ff = self.fitness_function.calculate_fitness(new_sol)
                    (solution, ff, change) = (new_sol, new_ff, True) if new_ff < ff else (old_sol, ff, False)

        return solution, ff