from Core.EvolutionManager import EvolutionManager
import heapq


class Elitism:
    """
    Class that's enable to choose best % or number of specimens from current population and move it to new population
    """

    @staticmethod
    def selectEliteSpecimensPercent(howManySpecimens: float, maximize: bool,
                                    evolutionaryManager: EvolutionManager) -> None:
        """
        Selects the percent of current population and moves it to the new population.

        :param howManySpecimens: Percent of current population that will be moved to new population.
        :param maximize: Whether to look for max or min values.
        :param evolutionaryManager: Evolutionary manager that keep info about everything.
        :return:None
        """
        if not 0 <= howManySpecimens <= 1:
            raise ValueError(
                f"The percent of population is lower than 0 or higher than 1. Value given: {howManySpecimens}")

        evolutionState = evolutionaryManager.getEpochSnapshot()
        currentPopulation = evolutionState.currentPopulation
        bestSpecimens = []
        if maximize:
            bestSpecimens.extend(
                heapq.nlargest(int(evolutionState.populationSize * howManySpecimens), currentPopulation,
                               lambda x: x.getSpecimenValue()))
        else:
            bestSpecimens.extend(
                heapq.nsmallest(int(evolutionState.populationSize * howManySpecimens), currentPopulation,
                                lambda x: x.getSpecimenValue()))

        evolutionaryManager.updateNewPopulation(bestSpecimens)

    @staticmethod
    def selectEliteSpecimensCount(howManySpecimens: int, maximize: bool,
                                  evolutionaryManager: EvolutionManager) -> None:
        """
        Selects the number of current population and moves it the to new population.

        :param howManySpecimens: Number of current population that will be moved to new population.
        :param maximize: Whether to look for max or min values.
        :param evolutionaryManager: Evolutionary manager that keep info about everything.
        :return:None
        """
        evolutionState = evolutionaryManager.getEpochSnapshot()
        if not 0 <= howManySpecimens <= evolutionState.populationSize:
            raise ValueError(
                f"The number of specimen to move to new population is lower than 0 or higher than current population size. "
                f"Value given: {howManySpecimens}, value expected: in range of 0 to {evolutionState.populationSize}")

        currentPopulation = evolutionState.currentPopulation
        bestSpecimens = []
        if maximize:
            bestSpecimens.extend(
                heapq.nlargest(howManySpecimens, currentPopulation, lambda x: x.getSpecimenValue()))
        else:
            bestSpecimens.extend(
                heapq.nsmallest(howManySpecimens, currentPopulation, lambda x: x.getSpecimenValue()))

        evolutionaryManager.updateNewPopulation(bestSpecimens)
