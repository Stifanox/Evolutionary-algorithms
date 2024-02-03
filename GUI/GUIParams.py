import dataclasses
from typing import Tuple


@dataclasses.dataclass
class GUIParams:
    crossoverType: str
    crossoverArgument: float | None
    selectionNumOrPercent: str
    selectionArgument: float
    selectionType: str
    mutationType: str
    mutationProbability: float
    functionType: str
    functionDimension: float
    elitismType: str
    elitismArgument: float
    useInversion: bool
    inversionProbability: float
    specimenCount: int
    domainBound: Tuple[float, float]
    epochCount: int
    showChart: bool
    toMaximize: bool
    chromosomePrecision:int
    blendArgument:float
    isRealRepresentation:bool

