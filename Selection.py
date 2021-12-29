import numpy as np


class SelectionParameters:

    def __init__(self, type_of_selection: str = "Roulette", elite: bool = True, truncation: bool = False,
                 elite_count: int = 10, k: int = 10, p: float = 0.7, proportion: float = 0.25, **kwargs):
        """
        :param type_of_selection: Specify type of selection, possible values: "Roulette", "Tournament", "Boltzmann".
        :param elite_count: ???
        :param k: the tournament size, assuming tournament selection
        :param elite: #TODO
        :param truncation: #TODO
        :param p: probability of choosing the best individual, assuming tournament selection
        :param proportion: Specify the proportion of the fittest individuals to be selected and reproduced, assuming truncation selection.
        """
        self.type_of_selection = type_of_selection
        self.elite = elite
        self.truncation = truncation
        self.elite_count = elite_count if elite else 0
        self.k = k
        self.p = p
        self.proportion = proportion
        self.check()

    def check(self):
        if self.type_of_selection not in ("Roulette", "Tournament", "Boltzmann"):
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

    def select(self, population, fixed_len=None):
        if self.type_of_selection == "Roulette":
            return self.__select_roulette(population, fixed_len)
        elif self.type_of_selection == "Tournament":
            return self.__select_tournament(population, fixed_len)
        elif self.type_of_selection == "Boltzmann":
            return self.__select_boltzmann(population, fixed_len)

    def select_elite(self, population):
        if self.parameters.elite:
            res = self.__select_truncation(population) if self.parameters.truncation else self.__select_elite(population)
            return res

    def __select_roulette(self, population, fixed_len):
        if fixed_len is None:
            fixed_len = len(population)
        pop_copy = np.array(population, dtype=object)
        probs = np.array([genome[1] for genome in population])
        probs = probs / probs.sum()
        indices = np.random.choice(probs.shape[0], size=fixed_len, p=probs)
        return list(pop_copy[indices, :])

    def __select_tournament(self, population, fixed_len):
        if fixed_len is None:
            fixed_len = len(population)
        probs = [self.parameters.p * np.power(1 - self.parameters.p, i) for i in range(self.parameters.k)]
        population = np.array(population, dtype=object)
        selection = list()
        while len(selection) != fixed_len:
            indices = np.random.choice(len(population), size=self.parameters.k, replace=True)
            tournament = np.array(sorted(population[indices, :], key=lambda x: x[1], reverse=False), dtype=object)
            for i, prob in enumerate(probs):
                if np.random.rand() <= prob:
                    selection.append(tournament[i, :])
                    break
        return selection

    def __select_elite(self, population):
        sorted_by_fitness = sorted(population, key=lambda genome: genome[1], reverse=False)
        return sorted_by_fitness[:self.parameters.elite_count]

    def __select_truncation(self, population):
        elite = self.__select_elite(population)
        more_elite = list(elite[:int(self.parameters.proportion * len(elite))])
        return more_elite * int(1 / self.parameters.proportion)

    def __select_boltzmann(self, population, fixed_len):
        # TODO: uzupełnić
        return None


class WrongParametersError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
