import random
from typing import *
from copy import deepcopy
from Core.Speciman import Specimen
from Core.Chromosome import Chromosome

class CrossoverType:
    def mix(self, a : Specimen, b : Specimen) -> Tuple[Specimen, Specimen]:
        print("Unknown crossover type")
        return tuple([a, b])


class KPointCrossover(CrossoverType):
    def __init__(self, pointCount : int):
        if pointCount <= 0:
            raise ValueError("pointCount must be positive integer")
        self.pointCount = pointCount

    def mix(self, a : Specimen, b : Specimen) -> Tuple[Specimen, Specimen]:
        setA = a.getChromosomes()
        setB = b.getChromosomes()

        chromosomeCount = len(setA)
        if chromosomeCount != len(setB):
            raise RuntimeError("specimens have different number of chromosomes")

        copyA = deepcopy(a)
        copyB = deepcopy(b)

        for i in range(chromosomeCount):
            chA = setA[i].getChromosome()
            chB = setB[i].getChromosome()

            chromosomeSize = len(chA)
            if chromosomeSize != len(chB):
                raise RuntimeError("specimen's chromosomes have different length")

            points = [0]
            for j in range(self.pointCount):
                points.append(random.randrange(0, chromosomeSize))

            points.append(chromosomeSize)
            points.sort()

            mask = []
            swap = False

            for j in range(self.pointCount + 1):
                for k in range(points[j], points[j + 1]):
                    mask.append(swap)
                swap = not swap

            newChA = []
            newChB = []

            for j in range(chromosomeSize):
                if mask[j] == False:
                    newChA.append(chA[j])
                    newChB.append(chB[j])
                else:
                    newChA.append(chB[j])
                    newChB.append(chA[j])

            copyA.getChromosomes()[i].updateChromosome(''.join(newChA))
            copyB.getChromosomes()[i].updateChromosome(''.join(newChB))

        return tuple([copyA, copyB])


class ShuffleCrossover(CrossoverType):
    def __init__(self):
        pass
    
    def mix(self, a : Specimen, b : Specimen) -> Tuple[Specimen, Specimen]:
        return tuple([a, b])


class DiscreteCrossover(CrossoverType):
    def __init__(self, threshold : float):
        if threshold < 0.0 or threshold > 1.0:
            raise ValueError("threshold must be within [0, 1]")
        self.threshold = threshold
        
    def mix(self, a : Specimen, b : Specimen) -> Tuple[Specimen, Specimen]:
        return tuple([a, b])


class UniformCrossover(CrossoverType):
    def __init__(self):
        pass
    
    def mix(self, a : Specimen, b : Specimen) -> Tuple[Specimen, Specimen]:
        return tuple([a, b])