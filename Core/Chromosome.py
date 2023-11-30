import multimethod
from typing import *
import re


# TODO: check if string chromosome is less or eq to chromosome precision
class Chromosome:
    """
    Class which represent a single chromosome (value) of specimen.
    """

    def __init__(self, chromosome: str | float, chromosomePrecision: int, functionDomain: Tuple[float, float]):
        self.__functionDomain = functionDomain
        self.__chromosomePrecision = chromosomePrecision
        self.__chromosomeSize = self.__calculateChromosomeSize(self.__chromosomePrecision)
        self.__chromosome: str | int
        if isinstance(chromosome, str) and self.__checkChromosome(chromosome):
            raise ValueError(f"Chromosome is not built up from zeros and one. Your chromosome: {chromosome}")

        if isinstance(chromosome, (float, int)) and functionDomain[0] > chromosome > functionDomain[1]:
            raise ValueError(
                f"Chromosome is out of function domain. Domain: ({functionDomain[0]},{functionDomain[1]}). "
                f"Your value: {chromosome}")
        if isinstance(chromosome, (float, int)) and not self.__checkIfNumberIsInDomain(chromosome):
            raise ValueError("Number is not in the domain of function")

        if isinstance(chromosome, str):
            filledChromosome = self.__fillChromosome(chromosome)
            self.updateChromosome(filledChromosome)

        elif isinstance(chromosome, (float, int)):
            self.__chromosome = self.__convertNumberToChromosome(chromosome)
            self.__chromosome = self.__fillChromosome(self.__chromosome[2:])

    def getChromosome(self) -> str:
        """
        Get chromosome represented in bytes.

        :return: Chromosome in bytes.
        """
        return self.__chromosome

    def getChromosomePrecision(self):
        """
        Get chromosome precision.

        :return: Chromosome precision.
        """
        return self.__chromosomePrecision

    def getChromosomeSize(self):
        """
        Get chromosome length (the byte one).

        :return: Chromosome length (bytes).
        """
        return self.__chromosomeSize

    def getFunctionDomain(self) -> tuple[float, float]:
        """
        Get a function domain for given chromosome.

        Lower bound is functionDomain[0] and higher bound is functionDomain[1].


        :return: Function domain in tuple.
        """

        return tuple(x for x in self.__functionDomain)

    def getChromosomeNumericValue(self) -> float:
        """
        Returns numeric value of chromosome. The value may be not the exact (if chromosome created from float) but is very close to that representation.

        :return: Numeric value of chromosome.
        """
        (a, b) = self.__functionDomain
        x = a + int(self.__chromosome, 2) * (b - a) / (2 ** self.__chromosomeSize - 1)
        return x

    @multimethod.overload
    def updateChromosome(self, chromosome: str):
        """
        Change the chromosome value by providing string.

        If provided string is smaller than chromosome length, chromosome will be automatically filled with leading zeros.

        :param chromosome: String which is built from zeros and ones.
        :return: None
        :rtype: None
        """
        if self.__checkChromosome(chromosome):
            raise ValueError(f"Chromosome is not built up from zeros and one. Your chromosome: {chromosome}")
        if self.__chromosomeSize < len(chromosome):
            raise ValueError(
                f"The chromosome size is too big. Desire length: {self.__chromosomeSize}, got: {len(chromosome)}")

        filledChromosome = self.__fillChromosome(chromosome)
        self.__chromosome = filledChromosome

    @multimethod.overload
    def updateChromosome(self, chromosome: float):
        """
        Change the chromosome value by providing number.

        If number is not in the domain of function this function will throw error.

        :param chromosome: Number with which we want to change value of chromosome.
        :return: None
        :rtype: None
        """
        if not self.__checkIfNumberIsInDomain(chromosome):
            raise ValueError("The number is not in the domain of function")

        self.__chromosome = self.__convertNumberToChromosome(chromosome)
        self.__chromosome = self.__fillChromosome(self.__chromosome[2:])

    @staticmethod
    def __checkChromosome(chromosome: str) -> bool:
        """
        Check if string is built from zeros and ones.

        :param chromosome: String which are checking
        :return: If value is true that means that string contain other signs beside zeros and ones.
        """
        if re.search("^[01]+$", chromosome) is not None:
            return False
        else:
            return True

    # FIXME: fix this naive search for good length of chromosome
    def __calculateChromosomeSize(self, chromosomePrecision: int) -> int:
        """
        Calculate chromosome length with given precision.

        :param chromosomePrecision: Number of precision
        :return: Chromosome length
        """
        i = 1
        (a, b) = self.__functionDomain
        while True:
            if (b - a) * 10 ** chromosomePrecision <= 2 ** i - 1:
                return i
            i += 1

    def __convertNumberToChromosome(self, number: float) -> str:
        """
        Convert value BUT it will have some marginal error to it (e.g. 9 will not convert to 9 in bytes)

        :param number: Number we want to convert
        :return: Chromosome represented in binary
        """
        (a, b) = self.__functionDomain
        chromosome = bin(int((number - a) / (b - a) * (2 ** self.__chromosomeSize - 1)))
        return chromosome

    def __fillChromosome(self, chromosome: str):
        """
        Fill chromosome with leading zeros by the difference between desired chromosome length and current chromosome length.

        :param chromosome: Chromosome which we want to fill in.
        :return: Filled chromosome
        """
        tempChromosome = chromosome
        tempChromosome = ("0" * (self.__chromosomeSize - len(chromosome))) + tempChromosome
        return tempChromosome

    def __checkIfNumberIsInDomain(self, chromosome: float):
        """
        Check if given value is in the domain of function.

        :param chromosome: Value to check.
        :return: If true value is in the domain of function
        """
        return self.__functionDomain[0] <= chromosome <= self.__functionDomain[1]
