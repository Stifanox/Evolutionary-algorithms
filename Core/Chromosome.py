import multimethod
from typing import *
import re


# TODO: check if string chromosome is less or eq to chromosome precision
class Chromosome:

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
        return self.__chromosome

    def getChromosomePrecision(self):
        return self.__chromosomePrecision

    def getChromosomeSize(self):
        return self.__chromosomeSize

    def getFunctionDomain(self):
        return tuple(x for x in self.__functionDomain)

    def getChromosomeNumericValue(self) -> int:
        """
        Returns numeric value of chromosome
        :return:
        """
        (a, b) = self.__functionDomain
        x = a + int(self.__chromosome, 2) * (b - a) / (2 ** self.__chromosomeSize - 1)
        return x

    @multimethod.overload
    def updateChromosome(self, chromosome: str):
        if self.__checkChromosome(chromosome):
            raise ValueError(f"Chromosome is not built up from zeros and one. Your chromosome: {chromosome}")
        if self.__chromosomeSize < len(chromosome):
            raise ValueError(
                f"The chromosome size is too big. Desire length: {self.__chromosomeSize}, got: {len(chromosome)}")

        filledChromosome = self.__fillChromosome(chromosome)
        self.__chromosome = filledChromosome

    @multimethod.overload
    def updateChromosome(self, chromosome: int):
        if not self.__checkIfNumberIsInDomain(chromosome):
            raise ValueError("The number is not in the domain of function")

        self.__chromosome = self.__convertNumberToChromosome(chromosome)
        self.__chromosome = self.__fillChromosome(self.__chromosome[2:])

    @staticmethod
    def __checkChromosome(chromosome: str) -> bool:
        if re.search("^[01]+$", chromosome) is not None:
            return False
        else:
            return True

    # FIXME: fix this naive search for good length of chromosome
    def __calculateChromosomeSize(self, chromosomePrecision: int) -> int:
        i = 1
        (a, b) = self.__functionDomain
        while True:
            if (b - a) * 10 ** chromosomePrecision <= 2 ** i - 1:
                return i
            i += 1

    def __convertNumberToChromosome(self, number: float) -> str:
        """
        This will convert value BUT it will have some error to it (e.g. 9 will not convert to 9)
        :param number:
        :return:
        """
        (a, b) = self.__functionDomain
        chromosome = bin(int((number - a) / (b - a) * (2 ** self.__chromosomeSize - 1)))
        return chromosome

    def __fillChromosome(self, chromosome: str):
        tempChromosome = chromosome
        tempChromosome = ("0" * (self.__chromosomeSize - len(chromosome))) + tempChromosome
        return tempChromosome

    def __checkIfNumberIsInDomain(self, chromosome: float):
        return self.__functionDomain[0] <= chromosome <= self.__functionDomain[1]
