import random
from Core.FitnessFunction import FitnessFunction
from Core.BinaryRepresentation.SpecimenBinary import SpecimenBinary
from Core.BinaryRepresentation.ChromosomeBinaryFactory import ChromosomeBinaryFactory
from typing import *


def initRandomBinaryPopulation(populationSize: int, chromosomePrecision: int, fitnessFunction: FitnessFunction) -> \
        List[SpecimenBinary]:
    """
    Creates random population for first population.

    :param populationSize: How many specimen to create.
    :param chromosomePrecision: Precision for each chromosome.
    :param fitnessFunction: Fitness function.
    :return: List of specimens randomly generated.
    """
    functionDomain = fitnessFunction.getFunctionDomain()
    functionDimension = fitnessFunction.getFunctionDimension()

    population = [SpecimenBinary(
        [ChromosomeBinaryFactory.fromFloat(random.uniform(functionDomain[x][0], functionDomain[x][1]), chromosomePrecision, functionDomain[x]) for
         x in range(functionDimension)], functionDimension) for _ in range(populationSize)]

    return population
