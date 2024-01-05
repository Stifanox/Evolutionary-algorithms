from typing import *

from Core.Specimen import Specimen
from Core.RealRepresentation.ChromosomeReal import ChromosomeReal
import multimethod

class SpecimenReal(Specimen):

    def __init__(self, chromosomes: Collection[ChromosomeReal], nDimension: int):
        super().__init__(chromosomes, nDimension)

    @multimethod.overload
    def updateChromosomes(self, index: int, chromosome: ChromosomeReal) -> None:
        super().updateChromosomes(index, chromosome)

    @multimethod.overload
    def updateChromosomes(self, chromosomes: Collection[ChromosomeReal]) -> None:
        super().updateChromosomes(chromosomes)

    def getSpecimenValue(self):
        return super().getSpecimenValue()

    def getChromosomes(self) -> Tuple[ChromosomeReal, ...]:
        return super().getChromosomes()

    def setSpecimenValue(self, value: float):
        super().setSpecimenValue(value)
