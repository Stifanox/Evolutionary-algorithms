from typing import *
from Core.Speciman import Specimen


class FitnessFunction:
    """
    Class to create info about all function related stuff.
    """

    def __init__(self, nDimension: int, functionDomain: Collection[Tuple[float, float]],
                 fitnessFunction: Callable[[Collection[float | int]], float]):
        if nDimension != len(functionDomain):
            raise ValueError("The numbers of variables in domain and fitness function is not the same")
        self.__nDimension = nDimension
        self.__fitnessFunction = fitnessFunction
        self.__functionDomain = functionDomain

    def calculateValue(self, specimen: Specimen) -> float:
        """
        Calculate value of provided function based on specimen.

        :param specimen: The specimen from which we calculate value of function.
        :type specimen: Specimen
        :return: Value of calculated function for given specimen
        :rtype: float
        """
        listOfChromosomesValue = [x.getChromosomeNumericValue() for x in specimen.getChromosomes()]
        return self.__fitnessFunction(listOfChromosomesValue)

    def getFunctionDimension(self) -> int:
        """
        Get the information about function dimension.

        :return: Dimension of function
        :rtype: int
        """
        return self.__nDimension

    def getFunctionDomain(self) -> Tuple[Tuple[float, float], ...]:
        """
        Get all function domain for all variables.

        For example functionDomain[0] gives you information about domain for variable x.

        :return: All function domains for each variable.
        :rtype: Tuple[Tuple[float, float], ...]
        """
        return tuple(x for x in self.__functionDomain)
