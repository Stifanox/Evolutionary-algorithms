from Core.Chromosome import Chromosome
from random import uniform, randint


# TODO: Add documentation
class Inversion:
    def __init__(self, chance: float, chromosome: Chromosome):
        self.__chance = chance
        self.__chromosome = chromosome

    def inversion(self):
        isInversionExecuted = uniform(0, 100)

        if isInversionExecuted <= self.__chance:
            chromosomeLength = self.__chromosome.getChromosomeSize()
            pointStartRandomIndex = randint(0, chromosomeLength - 1)
            # TODO: Ask if I should get EndRandomIndex like that or by randint(pointStartRandomIndex, chromosomeLength - 1)
            pointEndRandomIndex = pointStartRandomIndex

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
