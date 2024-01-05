from Core.BinaryRepresentation.ChromosomeBinary import ChromosomeBinary
from random import uniform, randint
from abc import ABC


class Mutation(ABC):
    """
    Base class representing an attempt of mutation occurrence on a single chromosome.
    """

    def __init__(self, chance: float):
        if chance < 0 or chance > 1:
            raise ValueError("Chance of mutation can't go below 0 and over 100 (percent).")

        self.__chance = chance

    def mutate(self, chromosome: ChromosomeBinary):
        """
        Try to mutate a single chromosome according to the chance given in the constructor.

        :return: Type of mutation (if mutation occurred) or an information that it didn't occur.
        """
        isMutationExecuted = uniform(0, 1)

        if isMutationExecuted <= self.__chance:
            self.performMutation(chromosome)
            return f"{self.__class__.__name__} occurred"
        else:
            return "Mutation did not occur"

    def performMutation(self, chromosome: ChromosomeBinary):
        """
        Placeholder method for performing the actual mutation.
        To be implemented by subclasses.
        """
        pass


class EdgeMutation(Mutation):
    """
    Represents an edge mutation occurrence on a single chromosome.
    """

    def __init__(self, chance: float):
        super().__init__(chance)
        self._Mutation__chance = chance

    def performMutation(self, chromosome: ChromosomeBinary):
        leftOrRight = randint(1, 2)

        chromosomeCopy = list(chromosome.getChromosomeBinaryValue())

        if leftOrRight == 1:
            chromosomeCopy[0] = '1' if chromosomeCopy[0] == '0' else '0'
        else:
            chromosomeCopy[-1] = '1' if chromosomeCopy[-1] == '0' else '0'

        updatedChromosome = ''.join(chromosomeCopy)
        chromosome.updateChromosome(updatedChromosome)


class SinglePointMutation(Mutation):
    """
    Represents a single-point mutation occurrence on a single chromosome.
    """

    def __init__(self, chance: float):
        super().__init__(chance)
        self._Mutation__chance = chance

    def performMutation(self, chromosome: ChromosomeBinary):
        chromosomeLength = chromosome.getChromosomeSize()
        pointRandomIndex = randint(1, chromosomeLength - 2)

        chromosomeCopy = list(chromosome.getChromosomeBinaryValue())

        chromosomeCopy[pointRandomIndex] = '1' if chromosomeCopy[pointRandomIndex] == '0' else '0'

        updatedChromosome = ''.join(chromosomeCopy)
        chromosome.updateChromosome(updatedChromosome)


class TwoPointMutation(Mutation):
    """
    Represents a two-point mutation occurrence on a single chromosome.
    """

    def __init__(self, chance: float):
        super().__init__(chance)
        self._Mutation__chance = chance

    def performMutation(self, chromosome: ChromosomeBinary):
        chromosomeLength = chromosome.getChromosomeSize()
        pointFirstRandomIndex = randint(1, chromosomeLength - 2)
        pointSecondRandomIndex = randint(1, chromosomeLength - 2)

        while pointFirstRandomIndex == pointSecondRandomIndex:
            pointSecondRandomIndex = randint(1, chromosomeLength - 2)

        chromosomeCopy = list(chromosome.getChromosomeBinaryValue())

        chromosomeCopy[pointFirstRandomIndex] = '1' if chromosomeCopy[pointFirstRandomIndex] == '0' else '0'
        chromosomeCopy[pointSecondRandomIndex] = '1' if chromosomeCopy[pointSecondRandomIndex] == '0' else '0'

        updatedChromosome = ''.join(chromosomeCopy)
        chromosome.updateChromosome(updatedChromosome)
