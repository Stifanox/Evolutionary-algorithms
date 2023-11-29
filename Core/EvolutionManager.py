from typing import *

from Core.FitnessFunction import FitnessFunction
from Core.Speciman import Specimen
from Core.EvolutionState import EvolutionState


# TODO: When specimen written, implement functions that get info about
# TODO: create function for init population
# TODO: create class that will take a snapshot of current state of manager (EvolutionState)
# FIXME: move function domain and fitness function somewhere else (maybe)

class EvolutionManager:

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
        if len(self.__newPopulation) + len(newSpecimens) > self.__populationSize and overflowPopulationWarning:
            print("Overall population is increasing. If it's intended don't bother by this message")
        self.__newPopulation.extend(newSpecimens)

    def updateSelectedPopulation(self, newSpecimens: Collection[Specimen]):
        if len(self.__selectedPopulation) + len(newSpecimens) > self.__populationSize:
            raise ValueError("Selected population would exceed the total population size.")
        self.__selectedPopulation.extend(newSpecimens)

    def updateEpoch(self):
        self.__currentPopulation = [x for x in self.__newPopulation]
        self.__populationSize = len(self.__currentPopulation)
        self.__newPopulation = []
        self.__selectedPopulation = []
        self.__currentEpoch += 1

    def getEpochSnapshot(self) -> EvolutionState:
        return EvolutionState(self.__populationSize, self.__currentEpoch, self.__currentPopulation,
                              self.__selectedPopulation, self.__newPopulation, self.__fitnessFunction)

    def setFirstPopulation(self, population: Collection[Specimen]):
        """
        Should be called only ONCE
        :param population:
        :return:
        """
        self.__currentPopulation.extend(population)