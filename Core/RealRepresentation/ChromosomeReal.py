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

    @staticmethod
    def calculateFunctionsDomainsIntersection(first: Tuple[float, float], second: Tuple[float, float]) -> Tuple[float, float]:
        """
        Calculates new chromosome domain from two chromosomes.
        :param first: Tuple[float, float] ; First chromosome.
        :param second: Tuple[float, float] ; Second chromosome.
        :return: Tuple[float, float] ; New chromosome domain from two chromosomes (max(a,b), min(A,B)), where <a,A> and <b,B> are domains for first and second chromosome respectively.
        :raises ValueError: If domains do not intersect.
        """
        a, A = first
        b, B = second
        new_range = (max(a, b), min(A, B))
        if new_range[0] > new_range[1]:
            raise ValueError("Domains do not intersect")

        return new_range

    @staticmethod
    def clampNumberToDomain(number: float, domain: Tuple[float, float]) -> float:
        """
        Clamps number to the domain. If number is smaller than domain[0], domain[0] is returned. If number is bigger than domain[1], domain[1] is returned.
        If the number is in the domain, it is returned unchanged.
        :param number: float Number to clamp.
        :param domain: Tuple[float, float] Domain to clamp to.
        :return: float ; Clamped number.
        """
        match number:
            case _ if number < domain[0]:
                return domain[0]
            case _ if number > domain[1]:
                return domain[1]
            case _:
                return number

    def __float__(self):
        return self.getChromosome()
