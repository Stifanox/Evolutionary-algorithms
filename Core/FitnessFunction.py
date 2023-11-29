from typing import *
from Core.Speciman import Specimen


class FitnessFunction:

    def __init__(self, nDimension: int, functionDomain: Collection[Tuple[float, float]],
                 fitnessFunction: Callable[[Collection[float | int]], float]):
        if nDimension != len(functionDomain):
            raise ValueError("The numbers of variables in domain and fitness function is not the same")
        self.__nDimension = nDimension
        self.__fitnessFunction = fitnessFunction
        self.__functionDomain = functionDomain

    def calculateValue(self, specimen: Specimen) -> float:
        listOfChromosomesValue = [x.getChromosomeNumericValue() for x in specimen.getChromosomes()]
        return self.__fitnessFunction(listOfChromosomesValue)

    def getFunctionDimension(self):
        return self.__nDimension

    def getFunctionDomain(self):
        return tuple(x for x in self.__functionDomain)
