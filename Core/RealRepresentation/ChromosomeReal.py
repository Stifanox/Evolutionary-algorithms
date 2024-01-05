from typing import Tuple

from Core.Chromosome import Chromosome


class ChromosomeReal(Chromosome):

    def __init__(self, chromosome: float, functionDomain: Tuple[float, float]):
        super().__init__(chromosome, functionDomain)

    def getChromosome(self) -> float:
        return super().getChromosome()

    def getFunctionDomain(self) -> tuple[float, float]:
        return super().getFunctionDomain()

    def updateChromosome(self, chromosome: float):
        super().updateChromosome(chromosome)

    def _checkIfNumberIsInDomain(self, chromosome: float):
        return super()._checkIfNumberIsInDomain(chromosome)
