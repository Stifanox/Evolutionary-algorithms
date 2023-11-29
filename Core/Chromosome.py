from typing import *
import re
from functools import singledispatchmethod


class Chromosome:

    def __init__(self, chromosome: str | float, chromosomePrecision: int, functionDomain: Tuple[float, float]):
        if isinstance(chromosome, str) and self.__checkChromosome(chromosome):
            raise ValueError(f"Chromosome is not built up from zeros and one. Your chromosome: {chromosome}")

        if isinstance(chromosome, float) and functionDomain[0] > chromosome > functionDomain[1]:
            raise ValueError(
                f"Chromosome is out of function domain. Domain: ({functionDomain[0]},{functionDomain[1]}). Your value: {chromosome}")

        self.__functionDomain = functionDomain
        self.__chromosomePrecision = chromosomePrecision
        self.__chromosomeSize = self.__calculateChromosomeSize(self.__chromosomePrecision)
        if isinstance(chromosome, str):
            self.__chromosome = chromosome
        elif isinstance(chromosome, float):
            self.__chromosome = self.__convertNumberToChromosome(chromosome)

    def getChromosome(self) -> str:
        return self.__chromosome

    def getChromosomeNumericValue(self) -> int:
        """
        Returns numeric value of chromosome
        :return:
        """
        (a, b) = self.__functionDomain
        x = a + int(self.__chromosome, 2) * (b - a) / (2 ** self.__chromosomeSize - 1)
        return x

    # TODO: jeżeli length jest mniejszy to wypełnić zerami aż nie będzie dobra wielosc
    @singledispatchmethod
    def updateChromosome(self, chromosome: str):
        if self.__checkChromosome(chromosome):
            raise ValueError(f"Chromosome is not built up from zeros and one. Your chromosome: {chromosome}")
        if self.__chromosomeSize != len(chromosome):
            raise ValueError(
                f"The chromosome size is wrong. Desire length: {self.__chromosomeSize}, got: {len(chromosome)}")

        self.__chromosome = chromosome

    @updateChromosome.register(int)
    def updateChromosome(self, chromosome: int):
        if self.__functionDomain[0] > chromosome > self.__functionDomain[1]:
            raise ValueError("The number is not in the domain of function")

        self.__chromosome = self.__convertNumberToChromosome(chromosome)

    def __checkChromosome(self, chromosome: str) -> bool:
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
        This will convert value BUT it will have some error to it (e.g. 9 will no convert to 9)
        :param number:
        :return:
        """
        (a, b) = self.__functionDomain
        chromosome = bin(int((number - a) / (b - a) * (2 ** self.__chromosomeSize - 1)))
        return chromosome
