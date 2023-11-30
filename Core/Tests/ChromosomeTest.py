from Core.Chromosome import Chromosome
from typing import *
import random


class ChromosomeTest:

    def __init__(self, value: str | float, precision: int, functionDomain: Tuple[float, float]):
        self.__value = value
        self.__precision = precision
        self.__functionDomain = functionDomain
        self.__chromosome = Chromosome(value, precision, functionDomain)

    def testChromosomeValue(self):
        assert self.__value - 0.001 < self.__chromosome.getChromosomeNumericValue() < self.__value + 0.001

    def changeChromosomeValueAndCheckItsValue(self, newVal: int):
        # strBuilder = ['0','1']
        # ''.join([random.choice(strBuilder) for _ in range(25)])

        self.__chromosome.updateChromosome(newVal)
        self.__value = newVal
        self.testChromosomeValue()

    def testChromosomeString(self):
        pass