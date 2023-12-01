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
    def __init__(self):
        pass
    
    def mix(self, a : Specimen, b : Specimen) -> Tuple[Specimen, Specimen]:
        setA = a.getChromosomes()
        setB = b.getChromosomes()

        chromosomeCount = len(setA)
        if chromosomeCount != len(setB):
            raise RuntimeError("specimens have different number of chromosomes")

        copyA = deepcopy(a)
        copyB = deepcopy(b)

        for i in range(chromosomeCount):
            chA = list(setA[i].getChromosome())
            chB = list(setB[i].getChromosome())

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