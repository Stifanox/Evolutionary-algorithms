import random
from abc import ABC
from typing import *
from copy import deepcopy
from Core.BinaryRepresentation.SpecimenBinary import SpecimenBinary


class CrossoverType(ABC):
    """
    Classes inheriting from this class represent a single method of crossover.
    """

    def mix(self, a : SpecimenBinary, b : SpecimenBinary) -> Tuple[SpecimenBinary, SpecimenBinary]:
        pass


class KPointCrossover(CrossoverType):
    """
    Implements k-point crossover.
    """

    def __init__(self, pointCount : int):
        """
        param: pointCount : int ; Number of "splits" in a single chromosome
        """
        if pointCount <= 0:
            raise ValueError("pointCount must be positive integer")
        self.pointCount = pointCount

    def mix(self, a : SpecimenBinary, b : SpecimenBinary) -> Tuple[SpecimenBinary, SpecimenBinary]:
        """
        Generates two children from two parents.

        :param: a : Specimen ; Parent A.
        :param: b : Specimen ; Parent B.
        :return: Tuple of two, newly generated specimens.
        """
        setA = a.getChromosomes()
        setB = b.getChromosomes()

        chromosomeCount = len(setA)
        if chromosomeCount != len(setB):
            raise RuntimeError("specimens have different number of chromosomes")

        copyA = deepcopy(a)
        copyB = deepcopy(b)

        for i in range(chromosomeCount):
            chA = setA[i].getChromosomeBinaryValue()
            chB = setB[i].getChromosomeBinaryValue()

            chromosomeSize = len(chA)
            if chromosomeSize != len(chB):
                raise RuntimeError("specimen's chromosomes have different length")

            points = [0]
            for j in range(self.pointCount):
                while True:
                    n = random.randrange(0, chromosomeSize)
                    if n not in points:
                        points.append(n)
                        break

            points.append(chromosomeSize)
            points.sort()

            newChA = []
            newChB = []
            swap = False

            for j in range(self.pointCount + 1):
                for k in range(points[j], points[j + 1]):
                    if swap == False:
                        newChA.append(chA[k])
                        newChB.append(chB[k])
                    else:
                        newChA.append(chB[k])
                        newChB.append(chA[k])
                swap = not swap

            copyA.getChromosomes()[i].updateChromosome(''.join(newChA))
            copyB.getChromosomes()[i].updateChromosome(''.join(newChB))

        return tuple([copyA, copyB])


class ShuffleCrossover(CrossoverType):
    """
    Implements shuffle crossover.
    """

    def __init__(self):
        pass

    def mix(self, a : SpecimenBinary, b : SpecimenBinary) -> Tuple[SpecimenBinary, SpecimenBinary]:
        """
        Generates two children from two parents.

        :param: a : Specimen ; Parent A.
        :param: b : Specimen ; Parent B.
        :return: Tuple of two, newly generated specimens.
        """
        setA = a.getChromosomes()
        setB = b.getChromosomes()

        chromosomeCount = len(setA)
        if chromosomeCount != len(setB):
            raise RuntimeError("specimens have different number of chromosomes")

        copyA = deepcopy(a)
        copyB = deepcopy(b)

        for i in range(chromosomeCount):
            chA = list(setA[i].getChromosomeBinaryValue())
            chB = list(setB[i].getChromosomeBinaryValue())

            chromosomeSize = len(chA)
            if chromosomeSize != len(chB):
                raise RuntimeError("specimen's chromosomes have different length")

            splitPoint = random.randrange(1, chromosomeSize - 1)

            chApart1 = chA[:splitPoint]
            chBpart1 = chB[:splitPoint]
            chApart2 = chA[splitPoint:]
            chBpart2 = chB[splitPoint:]

            random.shuffle(chApart1)
            random.shuffle(chBpart1)
            random.shuffle(chApart2)
            random.shuffle(chBpart2)

            copyA.getChromosomes()[i].updateChromosome(''.join(chApart1) + ''.join(chApart2))
            copyB.getChromosomes()[i].updateChromosome(''.join(chBpart1) + ''.join(chBpart2))

        kpoint = KPointCrossover(1)
        return kpoint.mix(copyA, copyB)


class DiscreteCrossover(CrossoverType):
    """
    Implements discrete crossover.
    """

    def __init__(self, threshold : float):
        """
        param: threshold : float ; Value within [0, 1]. The higher the value, the greater the chance of swapping a single gene.
        """
        if threshold < 0.0 or threshold > 1.0:
            raise ValueError("threshold must be within [0, 1]")
        self.threshold = threshold

    def mix(self, a : SpecimenBinary, b : SpecimenBinary) -> Tuple[SpecimenBinary, SpecimenBinary]:
        """
        Generates two children from two parents.

        :param: a : Specimen ; Parent A.
        :param: b : Specimen ; Parent B.
        :return: Tuple of two, newly generated specimens.
        """
        setA = a.getChromosomes()
        setB = b.getChromosomes()

        chromosomeCount = len(setA)
        if chromosomeCount != len(setB):
            raise RuntimeError("specimens have different number of chromosomes")

        copyA = deepcopy(a)
        copyB = deepcopy(b)

        for i in range(chromosomeCount):
            chA = setA[i].getChromosomeBinaryValue()
            chB = setB[i].getChromosomeBinaryValue()

            chromosomeSize = len(chA)
            if chromosomeSize != len(chB):
                raise RuntimeError("specimen's chromosomes have different length")

            newChA = []
            newChB = []
            for j in range(chromosomeSize):
                if random.random() >= self.threshold:
                    newChA.append(chA[j])
                    newChB.append(chB[j])
                else:
                    newChA.append(chB[j])
                    newChB.append(chA[j])

            copyA.getChromosomes()[i].updateChromosome(''.join(newChA))
            copyB.getChromosomes()[i].updateChromosome(''.join(newChB))

        return tuple([copyA, copyB])


class UniformCrossover(CrossoverType):
    """
    Implements uniform crossover.
    """

    def __init__(self):
        pass

    def mix(self, a : SpecimenBinary, b : SpecimenBinary) -> Tuple[SpecimenBinary, SpecimenBinary]:
        """
        Generates two children from two parents.

        :param: a : Specimen ; Parent A.
        :param: b : Specimen ; Parent B.
        :return: Tuple of two, newly generated specimens.
        """
        discrete = DiscreteCrossover(0.5)
        return discrete.mix(a, b)
