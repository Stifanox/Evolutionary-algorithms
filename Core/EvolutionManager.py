from typing import *

from Core.FitnessFunction import FitnessFunction
from Core.Speciman import Specimen
from Core.EvolutionState import EvolutionState


class EvolutionManager:
    """
    EvolutionManager is the state manager for currently running simulation of evolution.
    Here all the data is managed and updated.
    """

    def __init__(self, populationSize: int, epochCount: int,
                 fitnessFunction: FitnessFunction):
        self.__populationSize = populationSize
        self.__fitnessFunction = fitnessFunction
        self.__currentEpoch = 1
        self.__epochCount = epochCount
        self.__currentPopulation: List[Specimen] = []
        self.__selectedPopulation: List[Specimen] = []
        self.__newPopulation: List[Specimen] = []

    def updateNewPopulation(self, newSpecimens: Collection[Specimen], overflowPopulationWarning: bool = True):
        """
        Add to new population a list of new specimens.

        :param newSpecimens: Collection[Specimen] ; Any collection which contain specimens, that is desired to add to new population
        :param overflowPopulationWarning: bool ; Flag for displaying warnings. Default value is true.
        :return: None
        """
        if len(self.__newPopulation) + len(newSpecimens) > self.__populationSize and overflowPopulationWarning:
            print("Overall population is increasing. If it's intended don't bother by this message")
        self.__newPopulation.extend(newSpecimens)

    def updateSelectedPopulation(self, newSpecimens: Collection[Specimen]):
        """
        Add to selected population a list of new specimens.

        :param newSpecimens: Collection[Specimen] ; Any collection which contain specimens, that is desired to add to new population
        :return: None
        """
        if len(self.__selectedPopulation) + len(newSpecimens) > self.__populationSize:
            raise ValueError("Selected population would exceed the total population size.")
        self.__selectedPopulation.extend(newSpecimens)

    def updateEpoch(self, warningFlag: bool = True):
        """
        Move to next generation. It moves all 'new specimens' to 'current specimen' for current epoch.
        Besides, that new specimens are reset to zero which is the same for selected specimens.

        :param warningFlag: bool ; Display warning about overpopulation or underpopulation. Default value is True.
        :return: None
        """
        if self.__currentEpoch > self.__epochCount:
            print("The evolution has ended, can't go to next stage")
            return

        if len(self.__newPopulation) < self.__populationSize and warningFlag:
            print(f"The population of new population is less than declared. Epoch: {self.__currentEpoch}")
        elif len(self.__newPopulation) > self.__populationSize and warningFlag:
            print(f"The population of new population is more than declared. Epoch: {self.__currentEpoch}")

        self.__currentPopulation = [x for x in self.__newPopulation]
        self.__populationSize = len(self.__currentPopulation)
        self.__newPopulation = []
        self.__selectedPopulation = []
        self.__currentEpoch += 1

    def getEpochSnapshot(self) -> EvolutionState:
        """
        Get snapshot of current state.

        :return: EvolutionState
        """
        return EvolutionState(self.__populationSize, self.__currentEpoch, self.__currentPopulation,
                              self.__selectedPopulation, self.__newPopulation, self.__fitnessFunction, self.__epochCount)

    def setFirstPopulation(self, population: Collection[Specimen]):
        """
        Populate first population at the start of evolution. This method should be called ONCE at the start of simulation.
        Otherwise, the current population will be overriden.

        :param population: Collection[Specimen]; List of specimens to populate first population in epoch.
        :return: None
        """
        self.__currentPopulation.extend(population)
