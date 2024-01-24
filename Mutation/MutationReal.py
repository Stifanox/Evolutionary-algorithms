from Core.RealRepresentation.ChromosomeReal import ChromosomeReal
from abc import ABC
import random
import numpy

class MutationReal(ABC):
    """
    Base class representing an attempt of mutation occurrence on a single chromosome.
    """

    def __init__(self, chance: float):
        if chance < 0 or chance > 1:
            raise ValueError("Chance of mutation can't go below 0 and over 100 (percent).")

        self.__chance = chance

    def mutate(self, chromosome: ChromosomeReal):
        """
        Try to mutate a single chromosome according to the chance given in the constructor.

        :return: Type of mutation (if mutation occurred) or an information that it didn't occur.
        """
        isMutationExecuted = random.uniform(0, 1)

        if isMutationExecuted <= self.__chance:
            self.performMutation(chromosome)
            return f"{self.__class__.__name__} occurred"
        else:
            return "Mutation did not occur"

    def performMutation(self, chromosome: ChromosomeReal):
        """
        Placeholder method for performing the actual mutation.
        To be implemented by subclasses.
        """
        pass

class UniformMutationReal(MutationReal):
    """
    Represents a uniform mutation occurrence on a single chromosome with real representation.
    """

    def __init__(self, chance: float):
        super().__init__(chance)

    def performMutation(self, chromosome: ChromosomeReal):
        a, b = chromosome.getFunctionDomain()
        newValue = a + (b - a) * random.random()
        chromosome.updateChromosome(newValue)

class GaussMutationReal(MutationReal):
    """
    Represents a Gauss mutation occurrence on a single chromosome with real representation.
    """

    def __init__(self, chance: float):
        super().__init__(chance)

    def performMutation(self, chromosome: ChromosomeReal):
        a, b = chromosome.getFunctionDomain()
        oldValue = chromosome.getChromosome()
        newValue = oldValue + numpy.random.normal(0, 1)

        if newValue < a:
            newValue = a
        elif newValue > b:
            newValue = b

        chromosome.updateChromosome(newValue)