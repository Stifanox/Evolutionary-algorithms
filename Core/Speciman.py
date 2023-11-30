from typing import *

import multimethod

from Core.Chromosome import Chromosome


# TODO: implement __str__ method
class Specimen:

    def __init__(self, chromosomes: Collection[Chromosome], nDimension: int):
        if nDimension != len(chromosomes):
            raise ValueError("The amount of chromosomes is not identical to dimension of function.")
        self.__chromosomes = [x for x in chromosomes]
        self.__specimenValue = 0
    @multimethod.overload
    def updateChromosomes(self, index: int, chromosome: Chromosome) -> None:
        self.__chromosomes[index] = chromosome
    @multimethod.overload
    def updateChromosomes(self, chromosomes: Collection[Chromosome]) -> None:
        self.__chromosomes = [x for x in chromosomes]

    def getSpecimenValue(self):
        return self.__specimenValue

    def getChromosomes(self) -> Tuple[Chromosome]:
        return tuple(x for x in self.__chromosomes)
