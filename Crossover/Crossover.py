from typing import *
from Core.Speciman import Specimen

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
        return tuple([a, b])


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