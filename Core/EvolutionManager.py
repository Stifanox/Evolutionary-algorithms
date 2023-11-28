from typing import *
import numpy as np

from Core.FitnessFunction import FitnessFunction


# TODO: When specimen written, implement functions that gets info about
# TODO: create function for init population
# TODO: create class that will take a snapshot of current state of manager (EvolutionState)
# FIXME: move function domain and fitness function somewhere else (maybe)
# noinspection PyArgumentList
class EvolutionManager:

    def __init__(self, populationSize: int, epochCount: int, functionDomain: Collection[Tuple[int, int]],
                 fitnessFunction: FitnessFunction):
        if fitnessFunction.nDimension != len(functionDomain):
            raise ValueError("The numbers of variables in domain and fitness function is not the same")
        self.__populationSize = populationSize
        self.__currentEpoch = 1
        self.__epochCount = epochCount
        self.__functionDomain = functionDomain
        self.__currentPopulation = np.empty(0, dtype=object)
        self.__newPopulation = np.empty(0, dtype=object)

        self.__disallowPopulationMutation()

    def __allowCurrentMutationDecorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(self, *args: Any, **kwargs: Any) -> Any:
            self.__allowCurrentPopulationMutation()
            func(*args, **kwargs)
            self.__disallowCurrentPopulationMutation()

        return wrapper

    def __allowPopulationMutationDecorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(self, *args: Any, **kwargs: Any) -> Any:
            self.__allowPopulationMutation()
            func(*args, **kwargs)
            self.__disallowPopulationMutation()

        return wrapper

    def __allowNewMutationDecorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(self, *args: Any, **kwargs: Any) -> Any:
            self.__allowNewPopulationMutation()
            func(self, *args, **kwargs)
            self.__disallowNewPopulationMutation()

        return wrapper

    # TODO: make all getters
    def getPopulation(self):
        return self.__currentPopulation

    @__allowNewMutationDecorator
    def updateNewPopulation(self, newSpecimens: Collection[int], overflowPopulationWarning: bool = True):
        # TODO: change type for new elements from int to Speciman
        if len(self.__newPopulation) + len(newSpecimens) > self.__populationSize and overflowPopulationWarning:
            print("Overall population is increasing. If it's intended don't bother by this message")
        self.__newPopulation = np.append(self.__newPopulation, newSpecimens)

    @__allowPopulationMutationDecorator
    def updateEpoch(self):
        self.__currentPopulation = self.__newPopulation
        self.__populationSize = len(self.__currentPopulation)
        self.__newPopulation = np.empty(0, dtype=np.object)
        self.__currentEpoch += 1

    def __allowNewPopulationMutation(self):
        self.__newPopulation.setflags(write=True)

    def __disallowNewPopulationMutation(self):
        self.__newPopulation.setflags(write=False)

    def __allowCurrentPopulationMutation(self):
        self.__currentPopulation.setflags(write=True)

    def __disallowCurrentPopulationMutation(self):
        self.__currentPopulation.setflags(write=False)

    def __allowPopulationMutation(self):
        self.__allowCurrentPopulationMutation()
        self.__allowNewPopulationMutation()

    def __disallowPopulationMutation(self):
        self.__disallowNewPopulationMutation()
        self.__disallowCurrentPopulationMutation()
