import numpy as np


class SelectionParameters:

    def __init__(self, type_of_selection: str = "Elitism", elite_count: int = 10,
                 k: int = 10, p: float = 0.7, proportion: float = 0.25):
        """
        :param type_of_selection: Specify type of selection, possible values: "Elitism", "Roulette", "Truncation", "Tournament", "Boltzmann".
        :param elite_count: ???
        :param k: the tournament size, assuming tournament selection
        :param p: probability of choosing the best individual, assuming tournament selection
        :param proportion: Specify the proportion of the fittest individuals to be selected and reproduced, assuming truncation selection.
        """
        self.type_of_selection = type_of_selection
        self.elite_count = elite_count
        self.k = k
        self.p = p
        self.proportion = proportion
        self.check()

    def check(self):
        if self.type_of_selection not in ("Elitism", "Roulette", "Truncation", "Tournament", "Boltzmann"):
            raise NotImplementedError(f"Selection not implemented for {self.type_of_selection} type!")
        if not isinstance(self.elite_count, int) or self.elite_count < 1:
            raise WrongParametersError(f"Parameter elite count must be a positive integer!")
        if not isinstance(self.k, int) or self.k < 1:
            raise WrongParametersError(f"Parameter k (the tournament size) must be a positive integer!")
        if not 0 <= self.p <= 1:
            raise WrongParametersError(f"Probability p must be in <0, 1>!")
        if not 0 <= self.proportion <= 1:
            raise WrongParametersError(f"Parameter proportion must be in <0, 1>!")


class Selection:
    def __init__(self, parameters: SelectionParameters):
        self.type_of_selection = parameters.type_of_selection
        self.parameters = parameters

    def select(self, population):
        if self.type_of_selection == "Elitism":
            return self.__select_elite(population)
        elif self.type_of_selection == "Roulette":
            return self.__select_roulette(population)
        elif self.type_of_selection == "Truncation":
            return self.__select_truncation(population)
        elif self.type_of_selection == "Tournament":
            return self.__select_tournament(population)
        elif self.type_of_selection == "Boltzmann":
            return self.__select_boltzmann(population)

    def __select_elite(self, population):
        sorted_by_fitness = sorted(population, key=lambda genome: genome[1], reverse=True)
        # JAK DOPELNIAC????
        return [genome[0] for genome in sorted_by_fitness[:self.parameters.elite_count]]

    def __select_roulette(self, population):
        solutions = np.array([genome[0] for genome in population])
        probs = np.array([genome[1] for genome in population])
        probs = probs / probs.sum()
        indices = np.random.choice(solutions.shape[0], size=len(population), p=probs)
        return list(solutions[indices, :])

    def __select_tournament(self, population):
        probs = [self.parameters.p * np.power(1 - self.parameters.p, i) for i in range(self.parameters.k)]
        population = np.array(population, dtype=object)
        len_population, selection = len(population), []
        while len(selection) != len_population:
            indices = np.random.choice(len_population, size=self.parameters.k, replace=True)
            tournament = np.array(sorted(population[indices, :], key=lambda x: x[1], reverse=True), dtype=object)
            for i, prob in enumerate(probs):
                if np.random.rand() <= prob:
                    selection.append(tournament[i, :])
                    break
        return selection

    def __select_truncation(self, population):
        elite = self.__select_elite(population)
        more_elite = list(elite[:int(self.parameters.proportion * len(elite))])
        return more_elite * int(1 / self.parameters.proportion)

    def __select_boltzmann(self, population):
        # TODO: uzupełnić
        return None


class WrongParametersError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
