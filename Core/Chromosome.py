from typing import *
from abc import ABC


class Chromosome(ABC):
    """
    Class which represent a single chromosome (value) of specimen.
    """

    def __init__(self, chromosome: str | float, functionDomain: Tuple[float, float]):
        self._functionDomain = functionDomain
        self._chromosome = chromosome

    def getChromosome(self) -> float:
        """
        Get chromosome.

        :return: Chromosome value.
        """
        return self._chromosome

    def getFunctionDomain(self) -> tuple[float, float]:
        """
        Get a function domain for given chromosome.

        Lower bound is functionDomain[0] and higher bound is functionDomain[1].


        :return: Function domain in tuple.
        """

        return tuple(x for x in self._functionDomain)

    def updateChromosome(self, chromosome: float):
        """
        Change the chromosome value by providing number.

        If number is not in the domain of function this function will throw error.

        :param chromosome: Number with which we want to change value of chromosome.
        :return: None
        :rtype: None
        """
        if not self._checkIfNumberIsInDomain(chromosome):
            raise ValueError("The number is not in the domain of function")
        self._chromosome = chromosome

    def _checkIfNumberIsInDomain(self, chromosome: float):
        """
        Check if given value is in the domain of function.

        :param chromosome: Value to check.
        :return: If true value is in the domain of function
        """
        return self._functionDomain[0] <= chromosome <= self._functionDomain[1]
