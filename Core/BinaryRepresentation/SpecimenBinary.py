from typing import *

from Core.BinaryRepresentation.ChromosomeBinary import ChromosomeBinary
from Core.Specimen import Specimen
import multimethod


class SpecimenBinary(Specimen):

    def __init__(self, chromosomes: Collection[ChromosomeBinary], nDimension: int):
        super(SpecimenBinary, self).__init__(chromosomes, nDimension)

    @multimethod.overload
    def updateChromosomes(self, index: int, chromosome: ChromosomeBinary) -> None:
        super().updateChromosomes(index, chromosome)

    @multimethod.overload
    def updateChromosomes(self, chromosomes: Collection[ChromosomeBinary]) -> None:
        super().updateChromosomes(chromosomes)

    def getSpecimenValue(self):
        return super().getSpecimenValue()

    def getChromosomes(self) -> Tuple[ChromosomeBinary, ...]:
        return super().getChromosomes()

    def setSpecimenValue(self, value: float):
        super().setSpecimenValue(value)
