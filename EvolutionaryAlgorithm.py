import Crossover
import FitnessFunction
import Solution
import Mutation
import Selection
import HybridOptimizer
import numpy as np


class EvolutionaryAlgorithmParameters:
    def __init__(self,
                 allow_eps_ff_stop: bool = False, eps_ff: float = 1e-6, eps_ff_type: str = "Best", no_back: int = 50,
                 allow_no_iter_stop: bool = True, no_iter: int = 1e6,
                 allow_indifferent_population_stop: bool = False, population_diversity_measure: str = "Std of FF",
                 pop_div_eps: float = 1e-2,
                 population_number: int = 50,
                 hybrid: bool = True, **kwargs):

        self.allow_eps_ff_stop = allow_eps_ff_stop
        self.eps_ff = eps_ff
        self.eps_ff_type = eps_ff_type
        self.no_back = no_back

        self.allow_no_iter_stop = allow_no_iter_stop
        self.no_iter = no_iter

        self.allow_indifferent_population_stop = allow_indifferent_population_stop
        self.population_diversity_measure = population_diversity_measure
        self.pop_div_eps = pop_div_eps

        self.population_number = population_number

        self.hybrid_optimizer = hybrid

        self.check()

    def check(self):
        if (not self.allow_eps_ff_stop) and (not self.allow_no_iter_stop) and (
                not self.allow_indifferent_population_stop):
            raise NoStopCondition("Algorithm has no stop condition, it is recommended to activate one")
        if self.no_back < 1:
            raise WrongParametersError("Number of iter for ff change should be an integer greater than 0!")


class EvolutionaryAlgorithm:
    def __init__(self, algorithm_parameters: EvolutionaryAlgorithmParameters):
        self.algorithm_parameters = algorithm_parameters

        self.time = 0

        self.solution = None
        self.solution_parameters = None

        self.population = []
        self.elite = []
        self.best_fitness_history = []
        self.average_fitness_history = []

        self.fitness_function = None
        self.fitness_function_parameters = None
        self.recent_ff_value = np.inf

        self.crossover = None
        self.crossover_parameters = None

        self.mutation = None
        self.mutation_parameters = None

        self.selection = None
        self.selection_parameters = None

        self.hybrid_optimizer = None
        self.hybrid_optimizer_parameters = None

    def set_solution(self, solution: Solution) -> None:
        self.solution = solution
        self.solution_parameters = solution.parameters

    def set_fitness_function(self, fitness_function: FitnessFunction) -> None:
        self.fitness_function = fitness_function
        self.fitness_function_parameters = fitness_function.parameters

    def set_crossover(self, crossover: Crossover) -> None:
        self.crossover = crossover
        self.crossover_parameters = crossover.parameters

    def set_mutation(self, mutation: Mutation) -> None:
        self.mutation = mutation
        self.mutation_parameters = self.mutation.parameters

    def set_selection(self, selection: Selection) -> None:
        self.selection = selection
        self.selection_parameters = selection.parameters

    def set_hybrid_optimizer(self, hybrid_optimizer: HybridOptimizer) -> None:
        self.hybrid_optimizer = hybrid_optimizer
        self.hybrid_optimizer_parameters = hybrid_optimizer.parameters

    def get_time(self):
        return self.time

    def get_best_fitness_history(self):
        return self.best_fitness_history

    def clear(self):
        self.time = 0
        self.population = []
        self.elite = []
        self.best_fitness_history = []
        self.average_fitness_history = []

    def proceed(self):
        self.generate_population()
        self.proceed_fitness()
        self.elite = self.selection.select_elite(self.population)

        while self.not_stop():
            self.time += 1

            for i in range(0, self.algorithm_parameters.population_number, 2):
                if np.random.rand() <= self.crossover_parameters.crossover_probability:
                    crossover_result = self.crossover.cross(self.population[i][0], self.population[i + 1][0])
                    x0 = self.solution.cast_feasible(crossover_result[0])
                    x1 = self.solution.cast_feasible(crossover_result[1])
                    self.population.append([x0, 0])
                    self.population.append([x1, 0])

            for i, solution in enumerate(self.population):
                if np.random.rand() <= self.mutation_parameters.mutation_probability:
                    self.population[i][0] = self.mutation.mutate(solution[0])
                    self.population[i][0] = self.solution.cast_feasible(self.population[i][0])

            self.proceed_fitness()
            self.population = self.selection.select(self.population + self.elite,
                                                    fixed_len=self.algorithm_parameters.population_number)
            self.elite = self.selection.select_elite(self.population + self.elite)

            population_fitness = [genome[1] for genome in self.population]
            best_fitness = self.elite[0][1] if self.selection_parameters.elite else max(population_fitness)
            average_fitness = sum(population_fitness) / len(population_fitness)
            self.best_fitness_history.append(best_fitness)
            self.average_fitness_history.append(average_fitness)

        best_solution, best_fitness = sorted(self.population + self.elite, key=lambda genome: genome[1], reverse=False)[
            0]
        if self.algorithm_parameters.hybrid_optimizer:
            best_solution, best_fitness = self.hybrid_optimizer.optimize(best_solution)
        return self.solution.get_solution(best_solution), self.solution.check_feasibility(best_solution), best_fitness

    def generate_population(self) -> None:
        if self.population is None:
            self.population = []
        for _ in range(self.algorithm_parameters.population_number):
            sol = self.solution.initialize_solution()
            self.population.append([sol, 0])

    def proceed_fitness(self) -> None:
        for idx, solution in enumerate(self.population):
            self.population[idx][1] = self.fitness_function.calculate_fitness(solution[0])

    def not_stop(self) -> bool:
        ff_eps_cond = (not self.algorithm_parameters.allow_eps_ff_stop) \
                      or self.fitness_function_std() > self.algorithm_parameters.eps_ff
        no_iter = (not self.algorithm_parameters.allow_no_iter_stop) \
                  or self.algorithm_parameters.no_iter > self.time
        indiff_popul = (not self.algorithm_parameters.allow_indifferent_population_stop) \
                       or self.population_diversity() > self.algorithm_parameters.pop_div_eps
        return ff_eps_cond and no_iter and indiff_popul

    def population_diversity(self) -> float:
        if self.algorithm_parameters.population_diversity_measure == "Std of FF":
            return self.__population_std_of_ff()

    def fitness_function_std(self) -> float:
        if self.algorithm_parameters.eps_ff_type == "Average":
            return self.__change_of_average_ff()
        elif self.algorithm_parameters.eps_ff_type == "Best":
            return self.__change_of_best_ff()

    def __change_of_average_ff(self) -> float:
        try:
            return abs(
                self.average_fitness_history[-1] - self.average_fitness_history[-1 - self.algorithm_parameters.no_back])
        except Exception:
            return np.inf

    def __change_of_best_ff(self) -> float:
        try:
            return abs(
                self.best_fitness_history[-1] - self.best_fitness_history[-1 - self.algorithm_parameters.no_back])
        except Exception:
            return np.inf

    def __population_std_of_ff(self) -> float:
        population_ff = np.array(self.population, dtype=object)[:, 1]
        return float(np.std(population_ff))


class NoStopCondition(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class WrongParametersError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
