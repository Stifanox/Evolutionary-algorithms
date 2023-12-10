from Core.Chromosome import Chromosome
from random import uniform, randint


class Mutation:
    """
    Class which represents an attempt of mutation occurence on single chromosome.
    """

    def __init__(self, chance: float, chromosome: Chromosome):
        if chance < 0 or chance > 100:
            raise ValueError("Chance of mutation can't go below 0 and over 100 (percent).")

        self.__chance = chance
        self.__chromosome = chromosome

    def mutation(self):
        """
        Try to mutate a single chromosome according to the chance given in the constructor.
        Type of mutation is drawed with probability of 1/3.

        :return: Type of mutation (if mutation occurred) or an information that it didn't occur.
        """
        isMutationExecuted = uniform(0, 100)

        if isMutationExecuted <= self.__chance:
            whichMutation = randint(1, 3)

            def edgeMutation() -> None:
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

            def singlePointMutation() -> None:
                chromosomeLength = self.__chromosome.getChromosomeSize()
                pointRandomIndex = randint(1, chromosomeLength - 2)

                chromosomeCopy = list(self.__chromosome.getChromosome())
                if chromosomeCopy[pointRandomIndex] == '0':
                    chromosomeCopy[pointRandomIndex] = '1'
                else:
                    chromosomeCopy[pointRandomIndex] = '0'

                updatedChromosome = ''.join(chromosomeCopy)
                self.__chromosome.updateChromosome(updatedChromosome)

            def twoPointMutation() -> None:
                chromosomeLength = self.__chromosome.getChromosomeSize()
                pointFirstRandomIndex = randint(1, chromosomeLength - 2)
                pointSecondRandomIndex = randint(1, chromosomeLength - 2)

                while pointFirstRandomIndex == pointSecondRandomIndex:
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
                1: edgeMutation,
                2: singlePointMutation,
                3: twoPointMutation
            }

            optionDict.get(whichMutation)()

            return optionDict[whichMutation].__name__ + " occurred"

        else:
            return "Mutation did not occur"
