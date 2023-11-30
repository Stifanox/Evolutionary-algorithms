from typing import *

import multimethod

from Core.Chromosome import Chromosome


# TODO: implement __str__ method
class Specimen:

    def __init__(self, chromosomes: Collection[Chromosome], nDimension: int):
        if nDimension != len(chromosomes):
            raise ValueError("The amount of chromosomes is not identical to dimension of function.")
        self.__nDimension = nDimension
        self.__chromosomes = [x for x in chromosomes]
        self.__specimenValue: float = 0
    @multimethod.overload
    def updateChromosomes(self, index: int, chromosome: Chromosome) -> None:
        """
        One
        :param index:
        :param chromosome:
        :return:
        """
        self.__chromosomes[index] = chromosome
    @multimethod.overload
    def updateChromosomes(self, chromosomes: Collection[Chromosome]) -> None:
        """
        Two
        :param chromosomes:
        :return:
        """
        if len(chromosomes) != self.__nDimension:
            raise ValueError("The length of array doesn't match the dimension of function")
        self.__chromosomes = [x for x in chromosomes]

    def getSpecimenValue(self):
        return self.__specimenValue

    def getChromosomes(self) -> Tuple[Chromosome]:
        return tuple(x for x in self.__chromosomes)

    def setSpecimenValue(self, value: float):
        self.__specimenValue = value
