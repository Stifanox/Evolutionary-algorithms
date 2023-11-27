from typing import *


class FitnessFunction:

    def __init__(self, nDimension: int, fitnessFunction: Callable[[Collection[float | int]], float]):
        self.nDimension = nDimension
        self.fitnessFunction = fitnessFunction

