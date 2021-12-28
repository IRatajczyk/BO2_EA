import Crossover
import FitnessFunction
import Solution
import Mutation
import Selection
import numpy as np


class EvolutionaryAlgorithmParameters:
    def __init__(self, allow_eps_ff_stop: bool = False, eps_ff: float = 1e-6, eps_ff_type: str = "Average",
                 allow_no_iter_stop: bool = True, no_iter: int = 1e6,
                 allow_indifferent_population_stop: bool = False, population_diversity_measure: str = "Std of FF",
                 pop_div_eps: float = 1e-2, population_number: int = 50, **kwargs):
        self.allow_eps_ff_stop = allow_eps_ff_stop
        self.eps_ff = eps_ff
        self.eps_ff_type = eps_ff_type

        self.allow_no_iter_stop = allow_no_iter_stop
        self.no_iter = no_iter

        self.allow_indifferent_population_stop = allow_indifferent_population_stop
        self.population_diversity_measure = population_diversity_measure
        self.pop_div_eps = pop_div_eps

        self.population_number = population_number

        self.check()

    def check(self):
        if (not self.allow_eps_ff_stop) and (not self.allow_no_iter_stop) and (
                not self.allow_indifferent_population_stop):
            raise NoStopCondition("Algorithm has no stop condition, it is recommended to activate one")


class EvolutionaryAlgorithm:
    def __init__(self, algorithm_parameters: EvolutionaryAlgorithmParameters):
        self.algorithm_parameters = algorithm_parameters

        self.time = 0

        self.solution = None
        self.solution_parameters = None

        self.population = []
        self.temporal_population = None
        self.offspring = None

        self.elite = []

        self.fitness_function = None
        self.fitness_function_parameters = None
        self.recent_ff_value = np.inf

        self.crossover = None
        self.crossover_parameters = None

        self.mutation = None
        self.mutation_parameters = None

        self.selection = None
        self.selection_parameters = None

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

    def proceed(self):  #TODO
        self.generate_population()
        while self.not_stop():
            self.time += 1
            self.proceed_fitness()




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
                      and self.__fitness_function_std() > self.algorithm_parameters.eps_ff
        no_iter = (not self.algorithm_parameters.allow_no_iter_stop) \
                  and self.algorithm_parameters.no_iter > self.time
        indiff_popul = (not self.algorithm_parameters.allow_indifferent_population_stop) \
                       and self.population_diversity() > self.algorithm_parameters.pop_div_eps
        return ff_eps_cond and no_iter and indiff_popul

    def population_diversity(self) -> float:
        if self.algorithm_parameters.population_diversity_measure == "Std of FF":
            return self.__population_std_of_ff()

    def __fitness_function_std(self) -> float:
        if self.algorithm_parameters.eps_ff_type == "Average":
            return 1

    def __population_std_of_ff(self) -> float:
        population_ff = np.array(self.population, dtype=object)[:, 1]
        return float(np.std(population_ff))


class NoStopCondition(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
