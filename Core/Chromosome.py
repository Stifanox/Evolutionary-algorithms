from typing import *
import re
import numpy as np


class Chromosome:
    # jedna zmienna w funkcji = jeden chromosome
    # TODO: implement chromosome so that u can either pass str and int for ALL functions that modify chromosome
    def __init__(self, chromosome: str | int, chromosomePrecision: int, functionDomain: Tuple[int, int]):
        if self.__checkChromosome(chromosome) and type(chromosome) is str:
            raise ValueError(f"Chromosome is not built up from zeros and one. Your chromosome: {chromosome}")

        if type(chromosome) is str:
            self.__chromosome = chromosome
        elif type(chromosome) is int:
            self.__chromosome = self.__convertNumberToChromosome(chromosome)

        self.__functionDomain = functionDomain
        self.__chromosomePrecision = chromosomePrecision
        self.__chromosomeSize = self.__calculateChromosomeSize(self.__chromosomePrecision)

    def getChromosome(self) -> str:
        return self.__chromosome

    def getChromosomeNumericValue(self) -> int:
        (a, b) = self.__functionDomain
        x = a + int(self.__chromosome, 2) * (b - a) / (2 ** self.__chromosomeSize - 1)
        return x

    def updateChromosome(self, chromosome: str | int):
        if self.__checkChromosome(chromosome) and type(chromosome) is str:
            raise ValueError(f"Chromosome is not built up from zeros and one. Your chromosome: {chromosome}")
        if self.__chromosomeSize != len(chromosome) and type(chromosome) is str:
            raise ValueError(
                f"The chromosome size is wrong. Desire length: {self.__chromosomeSize}, got: {len(chromosome)}")

        if type(chromosome) is str:
            self.__chromosome = chromosome
        elif type(chromosome) is int:
            self.__chromosome = self.__convertNumberToChromosome(chromosome)

    def __checkChromosome(self, chromosome: str) -> bool:
        if re.search("^[01]+$", chromosome) is not None:
            return True
        else:
            return False

    # FIXME: fix this naive search for good length of chromosome
    def __calculateChromosomeSize(self, chromosomePrecision: int) -> int:
        i = 1
        (a, b) = self.__functionDomain
        while True:
            if (b - a) * 10 ** chromosomePrecision <= 2 ** i - 1:
                return i
            i += 1

    def __convertNumberToChromosome(self, number: int) -> str:
        """
        This will convert value BUT it will have some error to it (e.g. 9 will no convert to 9)
        :param number:
        :return:
        """
        (a, b) = self.__functionDomain
        chromosome = bin(int((number - a) / (b - a) * (2 ** self.__chromosomeSize - 1)))
        return chromosome
