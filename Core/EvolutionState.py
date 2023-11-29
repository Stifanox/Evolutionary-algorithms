import json
from typing import *
from Core.Speciman import Specimen
from Core.FitnessFunction import FitnessFunction


class EvolutionState:

    def __init__(self, populationSize: int, currentEpoch: int, currentPopulation: List[Specimen],
                 selectedPopulation: List[Specimen], newPopulation: List[Specimen], fitnessFunction: FitnessFunction):
        self.populationSize = populationSize
        self.currentEpoch = currentEpoch
        self.currentPopulation: Tuple[Specimen] = tuple(x for x in currentPopulation)
        self.selectedPopulation: Tuple[Specimen] = tuple(x for x in selectedPopulation)
        self.newPopulation: Tuple[Specimen] = tuple(x for x in newPopulation)
        self.fitnessFuntion = fitnessFunction

    def __str__(self):
        return json.dumps({
            "populationSize": self.populationSize,
            "currentEpoch": self.currentEpoch,
            "currentPopulation": str(self.currentPopulation),
            "selectedPopulation": str(self.selectedPopulation),
            "newPopulation": str(self.newPopulation),
            "functionDomain": self.fitnessFuntion.getFunctionDomain(),
            "functionDimension": self.fitnessFuntion.getFunctionDimension()
        })