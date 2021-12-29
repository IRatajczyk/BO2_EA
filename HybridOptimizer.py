import numpy
import Solution
import FitnessFunction


class HybridOptimizerParameters:
    def __init__(self, type_of_hybrid: str = "Feasible greedy", **kwargs):
        self.type_of_hybrid = type_of_hybrid

    def check(self):
        if self.type_of_hybrid not in ("Feasible greedy",):
            raise NotImplementedError(f"Mutation not implemented for {self.type_of_hybrid} type!")


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

    def __feasible_greedy_optimizer(self, solution):
        change = True
        ff = self.fitness_function.calculate_fitness(solution)
        cumulative_sum = self.solution_parameters.L0
        DL = self.solution_parameters.DL_limit
        while change:
            change = False
            for idx in range(1, self.solution_parameters.solution_size - 1):
                for d in range(-cumulative_sum - solution[idx], DL - solution[idx]):
                    old_sol = solution
                    solution[idx] = d
                    new_sol = solution if self.solution.check_feasibility(solution) else old_sol
                    new_ff = self.fitness_function.calculate_fitness(solution)
                    (solution, ff, change) = (new_sol, new_ff, True) if new_ff < ff else (old_sol, ff, False)
        return solution, ff
