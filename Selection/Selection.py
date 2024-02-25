from typing import Collection
from Core.Specimen import Specimen
from Core.FitnessFunction import FitnessFunction
import random


class Selection:
    """
    Class representing the selection process in a genetic algorithm.

    Attributes:
    - __fitnessFunction: Fitness function for evaluating specimens.
    - __selectionType: Type of selection strategy.
    - __selectionLimitType: Type of selection limit (Constant or Percentage).
    - __selectionLimitValue: Value of the selection limit.
    - __maximize: Boolean indicating whether to maximize or minimize the fitness function.
    - __specimens_selection_amount: Number of specimens to be selected.

    Methods:
    - selection(specimens: Collection[Specimen]) -> Collection[Specimen]:
        Selects specimens based on the configured selection strategy.
    """

    SelectionType_Top = 1
    SelectionType_Roulette = 2
    SelectionType_Tournament = 3
    LimitType_Constant = 1
    LimitType_Percentage = 2
    EvalMethod_Minimum = 1
    EvalMethod_Maximum = 2

    def __init__(self, fitnessFunction: FitnessFunction, selectionType: int, selectionLimitType: int,
                 selectionLimitValue: int, selectionEvalMethod: int):
        """
        Initializes the Selection object.

        :param fitnessFunction: Fitness function for evaluating specimens.
        :param selectionType: Type of selection strategy.
        :param selectionLimitType: Type of selection limit (Constant or Percentage).
        :param selectionLimitValue: Value of the selection limit.
        :param selectionEvalMethod: Evaluation method (Minimum or Maximum).
        """
        self.__fitnessFunction = fitnessFunction
        self.__selectionType = selectionType
        self.__selectionLimitType = selectionLimitType
        self.__selectionLimitValue = selectionLimitValue
        self.__maximize = selectionEvalMethod == Selection.EvalMethod_Maximum
        self.__specimens_selection_amount = 0

    def selection(self, specimens: Collection[Specimen]) -> Collection[Specimen]:
        """
        Selects specimens based on the configured selection strategy.

        :param specimens: Collection of specimens to select from.

        :return: Selected specimens based on the configured strategy.
        """
        specimens_copy = list(specimens)
        self.__specimens_selection_amount = self.calculate_selection_amount(specimens_copy)

        selection_strategy = self.get_selection_strategy()
        specimens_selected = selection_strategy.select(specimens_copy)

        return sorted(specimens_selected, key=lambda x: x.getSpecimenValue())

    def calculate_selection_amount(self, specimens_copy: Collection[Specimen]) -> int:
        """
        Calculates the number of specimens to be selected based on the configured limit.

        :param specimens_copy: Copy of the collection of specimens.

        :return: Calculated number of specimens to be selected.
        """
        selection_limit = self.__selectionLimitValue
        if self.__selectionLimitType == Selection.LimitType_Percentage:
            selection_limit = int(len(specimens_copy) * (selection_limit / 100))

        return max(1, min(selection_limit, len(specimens_copy)))

    def get_selection_strategy(self):
        """
        Returns the appropriate selection strategy based on the configured type.

        :return: Instance of the selected selection strategy.
        """
        if self.__selectionType == Selection.SelectionType_Top:
            return TopSelection(self.__specimens_selection_amount, self.__maximize)
        elif self.__selectionType == Selection.SelectionType_Roulette:
            return RouletteSelection(self.__specimens_selection_amount, self.__maximize)
        elif self.__selectionType == Selection.SelectionType_Tournament:
            return TournamentSelection(self.__specimens_selection_amount, self.__maximize)
        else:
            raise ValueError("Invalid selection type")


class TopSelection:
    """
    Class representing the top selection strategy.

    Attributes:
    - num_selections: Number of specimens to be selected.
    - maximize: Boolean indicating whether to maximize or minimize the fitness function.

    Methods:
    - select(specimens: Collection[Specimen]) -> Collection[Specimen]:
        Selects specimens based on the top selection strategy.
    """

    def __init__(self, num_selections: int, maximize: bool):
        """
        Initializes the TopSelection object.

        :param num_selections: Number of specimens to be selected.
        :param maximize: Boolean indicating whether to maximize or minimize the fitness function.
        """
        self.num_selections = num_selections
        self.maximize = maximize

    def select(self, specimens: Collection[Specimen]) -> Collection[Specimen]:
        """
        Selects specimens based on the top selection strategy.

        :param specimens: Collection of specimens to select from.

        :return: Selected specimens based on the top selection strategy.
        """
        return sorted(specimens, key=lambda x: x.getSpecimenValue(), reverse=self.maximize)[:self.num_selections]


class RouletteSelection:
    """
    Class representing the roulette wheel selection strategy.

    Attributes:
    - num_selections: Number of specimens to be selected.
    - maximize: Boolean indicating whether to maximize or minimize the fitness function.

    Methods:
    - select(specimens: Collection[Specimen]) -> Collection[Specimen]:
        Selects specimens based on the roulette wheel selection strategy.
    """

    def __init__(self, num_selections: int, maximize: bool):
        """
        Initializes the RouletteSelection object.

        :param num_selections: Number of specimens to be selected.
        :param maximize: Boolean indicating whether to maximize or minimize the fitness function.
        """
        self.num_selections = num_selections
        self.maximize = maximize

    def select(self, specimens: Collection[Specimen]) -> Collection[Specimen]:
        """
        Selects specimens based on the roulette wheel selection strategy.

        :param specimens: Collection of specimens to select from.

        :return: Selected specimens based on the roulette wheel selection strategy.
        """
        values = [specimen.getSpecimenValue() if self.maximize else -specimen.getSpecimenValue() for specimen in
                  specimens]
        lowest_value = min(values)
        current_fitness_sum = sum([value + abs(lowest_value) for value in values])


        weights = [(value + abs(lowest_value)) / current_fitness_sum if current_fitness_sum != 0 else 1 for value in
                   values]

        self.num_selections =int(self.num_selections)
        return random.choices(specimens, weights=weights, k=self.num_selections)


class TournamentSelection:
    """
    Class representing the tournament selection strategy.

    Attributes:
    - num_selections: Number of specimens to be selected.
    - maximize: Boolean indicating whether to maximize or minimize the fitness function.

    Methods:
    - select(specimens: Collection[Specimen]) -> Collection[Specimen]:
        Selects specimens based on the tournament selection strategy.
    """

    def __init__(self, num_selections: int, maximize: bool):
        """
        Initializes the TournamentSelection object.

        :param num_selections: Number of specimens to be selected.
        :param maximize: Boolean indicating whether to maximize or minimize the fitness function.
        """
        self.num_selections = num_selections
        self.maximize = maximize

    def select(self, specimens: Collection[Specimen]) -> Collection[Specimen]:
        """
        Selects specimens based on the tournament selection strategy.

        :param specimens: Collection of specimens to select from.

        :return: Selected specimens based on the tournament selection strategy.
        """
        selected_specimens = []

        while len(selected_specimens) < self.num_selections:
            copy_of_specimens = list(specimens)
            random.shuffle(copy_of_specimens)
            tournament_groups = [tuple(copy_of_specimens[ind:ind+3]) for ind in range(0, len(copy_of_specimens), 3) if ind + 2 < len(copy_of_specimens)]

            for group in tournament_groups:
                best_specimen = max(group, key=lambda x: x.getSpecimenValue()) if self.maximize else min(group, key=lambda x: x.getSpecimenValue())
                if len(selected_specimens) < self.num_selections:
                    selected_specimens.append(best_specimen)

        return selected_specimens
