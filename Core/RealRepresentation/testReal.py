from typing import *
from Core.RealRepresentation.SpecimenReal import SpecimenReal
from Core.FitnessFunction import FitnessFunction
from Core.RealRepresentation.ChromosomeReal import ChromosomeReal
import random


def initRandomRealPopulation(populationSize: int, fitnessFunction: FitnessFunction) -> \
        List[SpecimenReal]:
    """
    Creates random population for first population.

    :param populationSize: How many specimen to create.
    :param fitnessFunction: Fitness function.
    :return: List of specimens randomly generated.
    """
    functionDomain = fitnessFunction.getFunctionDomain()
    functionDimension = fitnessFunction.getFunctionDimension()

    population = [SpecimenReal(
        [ChromosomeReal(random.uniform(functionDomain[x][0], functionDomain[x][1]), functionDomain[x]) for
         x in range(functionDimension)], functionDimension) for _ in range(populationSize)]

    return population


def calculate(args: Collection[float]) -> float:
    return args[0] ** 2 + args[1] ** 2


fitness = FitnessFunction(2, [(-10, 10), (-10, 10)], calculate)
population = initRandomRealPopulation(100, fitness)

population[0].updateChromosomes(1,ChromosomeReal(2,(-10,10)))