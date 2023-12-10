from Core.Chromosome import Chromosome
from random import uniform, randint


class Inversion:
    """
    Class which represents an attempt of inversion occurence on single chromosome.
    """

    def __init__(self, chance: float, chromosome: Chromosome):
        if chance < 0 or chance > 100:
            raise ValueError("Chance of inversion can't go below 0 and over 100 (percent).")

        self.__chance = chance
        self.__chromosome = chromosome

    def inversion(self):
        """
        Try to inverse a part of single chromosome according to the chance given in the constructor.

        :return: Start and end indexes of inversion (if inversion occurred) or an information that it didn't occur.
        """
        isInversionExecuted = uniform(0, 100)

        if isInversionExecuted <= self.__chance:
            chromosomeLength = self.__chromosome.getChromosomeSize()
            pointStartRandomIndex = randint(0, chromosomeLength - 1)
            pointEndRandomIndex = randint(0, chromosomeLength - 1)

            while pointEndRandomIndex == pointStartRandomIndex:
                pointEndRandomIndex = randint(0, chromosomeLength - 1)

            if pointEndRandomIndex < pointStartRandomIndex:
                temp = pointStartRandomIndex
                pointStartRandomIndex = pointEndRandomIndex
                pointEndRandomIndex = temp

            chromosomeCopy = list(self.__chromosome.getChromosome())
            chromosomeInversedPart = (chromosomeCopy[pointStartRandomIndex:pointEndRandomIndex + 1])[::-1]
            chromosomeCopy[pointStartRandomIndex:pointEndRandomIndex + 1] = chromosomeInversedPart

            updatedChromosome = ''.join(chromosomeCopy)
            self.__chromosome.updateChromosome(updatedChromosome)

            return [pointStartRandomIndex, pointEndRandomIndex]

        else:
            return "Inversion did not occur"
