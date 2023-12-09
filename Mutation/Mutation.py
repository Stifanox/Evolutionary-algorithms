from Core.Chromosome import Chromosome
from random import uniform, randint
from typing import *
import math


class Mutation:
    """

    """
    def __init__(self, chance: float, chromosome: Chromosome):
        self.__chance = chance
        self.__chromosome = chromosome

    def mutation(self):
        isMutationExecuted = uniform(0, 100)

        if isMutationExecuted <= self.__chance:
            whichMutation = randint(1, 3)

            def EdgeMutation():
                leftOrRight = randint(1, 2)

                if leftOrRight == 1:
                    chromosomeCopy = list(self.__chromosome.getChromosome())

                    if chromosomeCopy[0] == '0':
                        chromosomeCopy[0] = '1'
                    else:
                        chromosomeCopy[0] = '0'

                    updatedChromosome = ''.join(chromosomeCopy)
                    self.__chromosome.updateChromosome(updatedChromosome)
                else:
                    chromosomeCopy = list(self.__chromosome.getChromosome())

                    if chromosomeCopy[-1] == '0':
                        chromosomeCopy[-1] = '1'
                    else:
                        chromosomeCopy[-1] = '0'

                    updatedChromosome = ''.join(chromosomeCopy)
                    self.__chromosome.updateChromosome(updatedChromosome)

            def SinglePointMutation():
                chromosomeLength = self.__chromosome.getChromosomeSize()
                pointRandomIndex = randint(1, chromosomeLength-2)

                chromosomeCopy = list(self.__chromosome.getChromosome())
                if chromosomeCopy[pointRandomIndex] == '0':
                    chromosomeCopy[pointRandomIndex] = '1'
                else:
                    chromosomeCopy[pointRandomIndex] = '0'

                updatedChromosome = ''.join(chromosomeCopy)
                self.__chromosome.updateChromosome(updatedChromosome)

            def TwoPointMutation():
                chromosomeLength = self.__chromosome.getChromosomeSize()
                pointFirstRandomIndex = randint(1, chromosomeLength - 2)
                pointSecondRandomIndex = randint(1, chromosomeLength - 2)

                chromosomeCopy = list(self.__chromosome.getChromosome())
                if chromosomeCopy[pointFirstRandomIndex] == '0':
                    chromosomeCopy[pointFirstRandomIndex] = '1'
                else:
                    chromosomeCopy[pointFirstRandomIndex] = '0'

                if chromosomeCopy[pointSecondRandomIndex] == '0':
                    chromosomeCopy[pointSecondRandomIndex] = '1'
                else:
                    chromosomeCopy[pointSecondRandomIndex] = '0'

                updatedChromosome = ''.join(chromosomeCopy)
                self.__chromosome.updateChromosome(updatedChromosome)

            optionDict = {
                1: EdgeMutation,
                2: SinglePointMutation,
                3: TwoPointMutation
            }

            optionDict.get(whichMutation)()

        else:
            pass
