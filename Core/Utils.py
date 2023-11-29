import random
from Core.FitnessFunction import FitnessFunction
from Core.Speciman import Specimen
from Core.Chromosome import Chromosome
from typing import *


def initRandomPopulation(populationSize: int, chromosomePrecision: int, fitnessFunction: FitnessFunction) -> \
        List[Specimen]:
    functionDomain = fitnessFunction.getFunctionDomain()
    functionDimension = fitnessFunction.getFunctionDimension()

    population = [Specimen(
        [Chromosome(random.uniform(functionDomain[x][0], functionDomain[x][1]), chromosomePrecision, functionDomain[x]) for
         x in range(functionDimension)], functionDimension) for _ in range(populationSize)]

    return population
