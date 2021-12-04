import Crossover
import FitnessFunction
import Solution


class EvolutionaryAlgorithm:
    def __init__(self, class_with_parameters):
        self.population = None
        self.parameters = class_with_parameters
        self.crossover = None
        self.mutation = None
        self.selection = None
        self.fitness_function = None

    def generate_population(self):
        self.population = None

    def add_crossover(self, crossover: Crossover):
        self.crossover = crossover

    def proceed(self):
        pass
