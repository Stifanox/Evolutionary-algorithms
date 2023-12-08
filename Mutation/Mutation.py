from Core.Chromosome import Chromosome
from abc import ABC, abstractmethod
from typing import *
import math


class Mutation(ABC):
    """

    """
    def __init__(self, chance: float):
        self.__chance = chance

    @abstractmethod
    def mutation(self, chromosome: Chromosome):
        pass


class EdgeMutation(Mutation):
    def __init__(self, chance: float):
        super().__init__(chance)

    def mutation(self, chromosome: Chromosome):
        pass


class SinglePointMutation(Mutation):
    def __init__(self, chance: float):
        super().__init__(chance)

    def mutation(self, chromosome: Chromosome):
        pass


class TwoPointMutation(Mutation):
    def __init__(self, chance: float):
        super().__init__(chance)

    def mutation(self, chromosome: Chromosome):
        pass
