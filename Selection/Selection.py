from typing import *
import random
from Core.FitnessFunction import FitnessFunction
from Core.Specimen import Specimen


class Selection:
    """
    Class managing selection of population
    """

    SelectionType_Top = 1  # Top - we choose n amount of best specimens
    SelectionType_Roulette = 2  # Roulette - random, where fitness is a weight
    SelectionType_Tournament = 3  # Tournament - specimens fight each other in brackets until there are more than desired specimens

    LimitType_Constant = 1  # LimitValue=10 == 10 top osobnikow
    LimitType_Percentage = 2  # LimitValue=10 == 10% top osobnikow

    EvalMethod_Minimum = 1  # closer to zero the specimen fitness, the better
    EvalMethod_Maximum = 2  # higher the specimen fitness, the better

    def __init__(self, fitnessFunction: FitnessFunction, selectionType: int, selectionLimitType: str,
                 selectionLimitValue: int, selectionEvalMethod: int):
        """
        Constructor for Selection class

        :param fitnessFunction: Function to evaluate specimen fitness.
        :type fitnessFunction: FitnessFunction

        :param selectionType: Type of selection (Top,Roulette,Tournament).
        :type selectionType: int

        :param selectionLimitType: Type of final amount of selected specimens (Constant,Percentage).
        :type selectionLimitType: int

        :param selectionLimitValue: Value of final amount of selected specimens (Constant,Percentage).
        :type selectionLimitValue: int

        :param selectionEvalMethod: Method of evaluating specimens fitness (Minimum,Maximum).
        :type selectionEvalMethod: int
        """
        self.__fitnessFunction = fitnessFunction
        self.__selectionType = selectionType
        self.__selectionLimitType = selectionLimitType
        self.__selectionLimitValue = selectionLimitValue
        self.__maximize = True if selectionEvalMethod == Selection.EvalMethod_Maximum else False

        self.__specimens_selection_amount = 0

    def selection(self, specimens: Collection[Specimen]) -> Collection[Specimen]:
        """
        Select specimens based on their fitness and selection type.

        :param specimens: The specimens to select from.
        :type specimens: Collection[Specimen]
        :return: Selected top specimens.
        :rtype: Collection[Specimen]
        """
        # fitness values

        specimensCopy = [specimen for specimen in specimens]

        self.__specimens_selection_amount = 0
        self.__specimens_selection_amount += int(self.__selectionLimitType == Selection.LimitType_Constant) * max(1,
                                                                                                                  min(self.__selectionLimitValue,
                                                                                                                      len(specimensCopy)))  # if constant, then min(limit,len_of_species)
        self.__specimens_selection_amount += int(self.__selectionLimitType == Selection.LimitType_Percentage) * max(1,
                                                                                                                    min(int(
                                                                                                                        len(specimensCopy) * (
                                                                                                                                self.__selectionLimitValue / 100)),
                                                                                                                        len(specimensCopy)))  # if percentage, then min(len_of_species*percentage,len_of_species)

        self.__specimens_selection_amount = int(self.__specimens_selection_amount)
        specimens_selected = []

        if self.__selectionType == Selection.SelectionType_Top:
            specimens_selected = self.__selection_Top(specimensCopy, self.__maximize)

        if self.__selectionType == Selection.SelectionType_Roulette:
            specimens_selected = self.__selection_Roulette(specimensCopy, self.__maximize)

        if self.__selectionType == Selection.SelectionType_Tournament:
            specimens_selected = self.__selection_Tournament(specimensCopy, self.__maximize)

        specimens_selected = sorted(specimens_selected, key=lambda x: x.getSpecimenValue())  # sorting ascending
        return specimens_selected

    def __selection_Top(self, specimens: Collection[Specimen], maximize: bool) -> Collection[Specimen]:
        specimens = sorted(specimens, key=lambda x: x.getSpecimenValue(), reverse=maximize)

        return specimens[0:self.__specimens_selection_amount]

    def __selection_Roulette(self, specimens: Collection[Specimen], maximize: bool) -> Collection[Specimen]:
        values = []

        if maximize:
            values.extend([specimen.getSpecimenValue() for specimen in specimens])
        else:
            values.extend([specimen.getSpecimenValue() * -1 for specimen in specimens])

        lowestValue = min(values)
        currentFitnessSum = sum([value + abs(lowestValue) for value in values])
        if currentFitnessSum == 0:
            weights = [1 for _ in range(len(values))]
        else:
            weights = [(values[index] + abs(lowestValue)) / currentFitnessSum for index in range(len(values))]

        randomSelectedSpecimens = random.choices(specimens, weights=weights, k=self.__specimens_selection_amount)

        return randomSelectedSpecimens

    def __selection_Tournament(self, specimens: Collection[Specimen], maximize: bool) -> Collection[Specimen]:
        selectedSpecimens = []

        while len(selectedSpecimens) < self.__specimens_selection_amount:
            copyOfSpecimens = [specimen for specimen in specimens]
            random.shuffle(copyOfSpecimens)  # random setup of brackets
            tournamentGroups = [tuple([copyOfSpecimens[ind], copyOfSpecimens[ind + 1], copyOfSpecimens[ind + 2]]) for
                                ind in range(0, len(copyOfSpecimens), 3) if ind + 2 < len(copyOfSpecimens)]

            for group in tournamentGroups:
                if maximize:
                    bestSpecimen = max(group, key=lambda x: x.getSpecimenValue())
                else:
                    bestSpecimen = min(group, key=lambda x: x.getSpecimenValue())

                if len(selectedSpecimens) < self.__specimens_selection_amount:
                    selectedSpecimens.append(bestSpecimen)

        print(len(selectedSpecimens))
        return selectedSpecimens
