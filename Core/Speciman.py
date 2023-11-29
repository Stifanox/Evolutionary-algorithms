from typing import *
from Core.Chromosome import Chromosome
from multimethod import multimethod

#TODO: change multimethod to singledispach (as in chromosome)
#TODO: implement __str__ methode
class Specimen:

    def __init__(self, chromosomes: Collection[Chromosome], nDimension: int):
        if nDimension != len(chromosomes):
            raise ValueError("The amount of chromosomes is not identical to dimension of function.")
        self.__chromosomes = [x for x in chromosomes]
        self.__specimenValue = 0

    @multimethod
    def updateChromosomes(self, index: int, chromosome: Chromosome) -> None:
        self.__chromosomes[index] = chromosome

    @multimethod
    def updateChromosomes(self, chromosomes: Collection[Chromosome]) -> None:
        self.__chromosomes = [x for x in chromosomes]

    def getSpecimenValue(self):
        return self.__specimenValue

    def getChromosomes(self) -> Tuple[Chromosome]:
        return tuple(x for x in self.__chromosomes)
