class SelectionParameters:
    def __init__(self, type_of_selection: str, elite_count: int = 0):
        self.type_of_selection = type_of_selection
        if self.type_of_selection == "Elitism":
            self.elite_count = elite_count


class Selection:
    def __init__(self, parameters: SelectionParameters):
        self.type_of_selection = parameters.type_of_selection
        self.parameters = parameters

    def select(self):
        if self.type_of_selection == "Elitism":
            return self.__select_elite()

    def __select_elite(self):
        return None
