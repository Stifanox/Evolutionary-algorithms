import multimethod
from typing import *
import re
import math
from Core.Chromosome import Chromosome


class ChromosomeBinary(Chromosome):
    """
    Class which represent a single chromosome (value) of specimen in binary.
    """

    def __init__(self, chromosome: str, chromosomePrecision: int, functionDomain: Tuple[float, float]):
        super(ChromosomeBinary, self).__init__(chromosome, functionDomain)
        self.__chromosomePrecision = chromosomePrecision
        self.__chromosomeSize = self.__calculateChromosomeSize(self.__chromosomePrecision)
        self._chromosome = ""

        if self.__checkChromosome(chromosome):
            raise ValueError(f"Chromosome is not built up from zeros and one. Your chromosome: {chromosome}")

        filledChromosome = self.__fillChromosome(chromosome)
        self.updateChromosome(filledChromosome)

    def getChromosome(self) -> float:
        """
        Returns numeric value of chromosome. The value may be not the exact (if chromosome created from float) but is very close to that representation.

        :return: Numeric value of chromosome.
        """
        (a, b) = self._functionDomain
        x = a + int(self._chromosome, 2) * (b - a) / (2 ** self.__chromosomeSize - 1)
        return x

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

    def getChromosomeBinaryValue(self) -> str:
        """
        Get chromosome represented in bytes.

        :return: Chromosome in bytes.
        """
        return self._chromosome

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
        self._chromosome = filledChromosome

    @multimethod.overload
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

        self._chromosome = self.__convertNumberToChromosome(chromosome)
        self._chromosome = self.__fillChromosome(self._chromosome[2:])

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

    def __calculateChromosomeSize(self, chromosomePrecision: int) -> int:
        """
        Calculate chromosome length with given precision.

        :param chromosomePrecision: Number of precision
        :return: Chromosome length
        """
        (a, b) = self._functionDomain

        chromosomeSize = math.ceil(math.log2((b - a) * 10 ** chromosomePrecision) + math.log2(1))
        return chromosomeSize

    def __convertNumberToChromosome(self, number: float) -> str:
        """
        Convert value BUT it will have some marginal error to it (e.g. 9 will not convert to 9 in bytes)

        :param number: Number we want to convert
        :return: Chromosome represented in binary
        """
        (a, b) = self._functionDomain
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
