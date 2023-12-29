from typing import Tuple
import math
from Core.Chromosome import Chromosome


class ChromosomeFactory:

    @staticmethod
    def fromFloat(chromosome: float, chromosomePrecision: int, functionDomain: Tuple[float, float]) -> Chromosome:
        """
        Create chromosome from number
        :param chromosome: Number from which we want to create chromosome
        :param chromosomePrecision: Precision of chromosome
        :param functionDomain: Domain of function
        :return: Chromosome instance
        """
        if not functionDomain[0] <= chromosome <= functionDomain[1]:
            raise ValueError(
                f"Chromosome is out of function domain. Domain: ({functionDomain[0]},{functionDomain[1]}). "
                f"Your value: {chromosome}")

        chromosomeSize = ChromosomeFactory.__calculateChromosomeSize(chromosomePrecision, functionDomain)
        chromosomeString = ChromosomeFactory.__convertNumberToChromosome(chromosome, functionDomain, chromosomeSize)
        chromosomeString = chromosomeString[2:]

        return Chromosome(chromosomeString, chromosomePrecision, functionDomain)

    @staticmethod
    def fromString(chromosome: str, chromosomePrecision: int, functionDomain: Tuple[float, float]) -> Chromosome:
        """
        Create chromosome from string
        :param chromosome: String to create chromosome
        :param chromosomePrecision: Precision of chromosome
        :param functionDomain: Domain of function
        :return: Chromosome instance
        """
        return Chromosome(chromosome, chromosomePrecision, functionDomain)

    @staticmethod
    def __convertNumberToChromosome(number: float, functionDomain: Tuple[float, float], chromosomeSize: int) -> str:
        """
        Convert value BUT it will have some marginal error to it (e.g. 9 will not convert to 9 in bytes)

        :param number: Number we want to convert
        :return: Chromosome represented in binary
        """
        (a, b) = functionDomain
        chromosome = bin(int((number - a) / (b - a) * (2 ** chromosomeSize - 1)))
        return chromosome

    @staticmethod
    def __calculateChromosomeSize(chromosomePrecision: int, functionDomain: Tuple[float, float]) -> int:
        """
        Calculate chromosome length with given precision.

        :param chromosomePrecision: Number of precision
        :return: Chromosome length
        """
        (a, b) = functionDomain

        chromosomeSize = math.ceil(math.log2((b - a) * 10 ** chromosomePrecision) + math.log2(1))
        return chromosomeSize
