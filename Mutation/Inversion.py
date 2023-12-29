from Core.Chromosome import Chromosome
from random import uniform, randint


class Inversion:
    """
    Class which represents an attempt of inversion occurence on single chromosome.
    """

    def __init__(self, chance: float):
        if chance < 0 or chance > 1:
            raise ValueError("Chance of inversion can't go below 0 and over 100 (percent).")

        self.__chance = chance

    def inversion(self, chromosome: Chromosome):
        """
        Try to inverse a part of single chromosome according to the chance given in the constructor.

        :return: Start and end indexes of inversion (if inversion occurred) or an information that it didn't occur.
        """
        isInversionExecuted = uniform(0, 1)

        if isInversionExecuted <= self.__chance:
            chromosomeLength = chromosome.getChromosomeSize()
            pointStartRandomIndex = randint(0, chromosomeLength - 1)
            pointEndRandomIndex = randint(0, chromosomeLength - 1)

            while pointEndRandomIndex == pointStartRandomIndex:
                pointEndRandomIndex = randint(0, chromosomeLength - 1)

            if pointEndRandomIndex < pointStartRandomIndex:
                temp = pointStartRandomIndex
                pointStartRandomIndex = pointEndRandomIndex
                pointEndRandomIndex = temp

            chromosomeCopy = list(chromosome.getChromosome())
            chromosomeInversedPart = (chromosomeCopy[pointStartRandomIndex:pointEndRandomIndex + 1])[::-1]
            chromosomeCopy[pointStartRandomIndex:pointEndRandomIndex + 1] = chromosomeInversedPart

            updatedChromosome = ''.join(chromosomeCopy)
            chromosome.updateChromosome(updatedChromosome)

            return [pointStartRandomIndex, pointEndRandomIndex]

        else:
            return "Inversion did not occur"
