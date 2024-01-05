import heapq
from abc import ABC
from typing import Collection, List
from Core.Specimen import Specimen


class Elitism(ABC):
    """
    Class that's baseline for elitism.
    """

    def __init__(self, elitismArgument: float, maximize: bool):
        self._elitismArgument = elitismArgument
        self._maximize = maximize

    def selectBest(self, currentPopulation: Collection[Specimen]) -> Collection[Specimen]:
        pass


class ElitismByPercent(Elitism):
    """
    Enable to choose best % of specimens from current population and move it to new population
    """

    def __init__(self, elitismArgument: float, maximize: bool):
        super().__init__(elitismArgument, maximize)

    def selectBest(self, currentPopulation: Collection[Specimen]) -> Collection[Specimen]:
        """
        Selects the percent of current population and moves it to the new population.

        :return:None
        """
        if not 0 <= self._elitismArgument <= 1:
            raise ValueError(
                f"The percent of population is lower than 0 or higher than 1. Value given: {self._elitismArgument}")

        bestSpecimens: List[Specimen] = []
        if self._maximize:
            bestSpecimens.extend(
                heapq.nlargest(int(len(currentPopulation) * self._elitismArgument), currentPopulation,
                               lambda x: x.getSpecimenValue()))
        else:
            bestSpecimens.extend(
                heapq.nsmallest(int(len(currentPopulation) * self._elitismArgument), currentPopulation,
                                lambda x: x.getSpecimenValue()))

        return bestSpecimens


class ElitismByCount(Elitism):
    """
    Enable to choose best number of specimens from current population and move it to new population
    """

    def __init__(self, elitismArgument: float, maximize: bool):
        super().__init__(elitismArgument, maximize)

    def selectBest(self, currentPopulation: Collection[Specimen]) -> Collection[Specimen]:
        """
        Selects the number of current population and moves it the to new population.

        :return:None
        """
        if not 0 <= self._elitismArgument <= len(currentPopulation):
            raise ValueError(
                f"The number of specimen to move to new population is lower than 0 or higher than current population size. "
                f"Value given: {self._elitismArgument}, value expected: in range of 0 to {len(currentPopulation)}")

        bestSpecimens: List[Specimen] = []
        if self._maximize:
            bestSpecimens.extend(
                heapq.nlargest(int(self._elitismArgument), currentPopulation, lambda x: x.getSpecimenValue()))
        else:
            bestSpecimens.extend(
                heapq.nsmallest(int(self._elitismArgument), currentPopulation, lambda x: x.getSpecimenValue()))

        return bestSpecimens
