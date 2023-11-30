from typing import *

import multimethod

from Core.Chromosome import Chromosome


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
        Replace chromosome for given index.

        :param index: Position of chromosome we want to replace. Position 0 is first chromosome.
        :param chromosome: Chromosome which will be placed in the place of the old one
        :return:None
        """
        self.__chromosomes[index] = chromosome

    @multimethod.overload
    def updateChromosomes(self, chromosomes: Collection[Chromosome]) -> None:
        """
        "Replace all chromosomes in specimen. If provided list length is not equal to dimension of function, this function will throw error.

        :param chromosomes: List of new chromosomes
        :return:None
        """
        if len(chromosomes) != self.__nDimension:
            raise ValueError("The length of array doesn't match the dimension of function")
        self.__chromosomes = [x for x in chromosomes]

    def getSpecimenValue(self):
        """
        Get specimen value (i.e. the value of function for given chromosomes)

        :return: Value of specimen
        """
        return self.__specimenValue

    def getChromosomes(self) -> Tuple[Chromosome, ...]:
        """
        Get list of all chromosome for give specimen

        :return: List of chromosomes
        """
        return tuple(x for x in self.__chromosomes)

    def setSpecimenValue(self, value: float):
        """
        Set value of specimen (i.e. value from function giving the chromosomes)

        :param value: Value from fitness function
        :return: None
        """
        self.__specimenValue = value
