class SelectionParameters:

    def __init__(self, type_of_selection: str = "Elitism", elite_count: int = 0):
        self.type_of_selection = type_of_selection

        self.elite_count = elite_count

    def check(self):
        # TODO: uzupełnić
        pass


class Selection:
    def __init__(self, parameters: SelectionParameters):
        self.type_of_selection = parameters.type_of_selection
        self.parameters = parameters

    def select(self, population):
        if self.type_of_selection == "Elitism":
            return self.__select_elite(population)
        elif self.type_of_selection == "Roulette Selection":
            return self.__select_roulette(population)
        elif self.type_of_selection == "Truncation":
            return self.__select_truncation(population)
        elif self.type_of_selection == "Tournament":
            return self.__select_tournament(population)
        elif self.type_of_selection == "Bolzmann":
            return self.__select_bolzmann(population)

    def __select_elite(self, population):
        #TODO: uzupełnić
        return None

    def __select_roulette(self, population):
        #TODO: uzupełnić
        return None

    def __select_tournament(self, population):
        #TODO: uzupełnić
        return None

    def __select_truncation(self, population):
        #TODO: uzupełnić
        return None

    def __select_bolzmann(self, population):
        #TODO: uzupełnić
        return None


