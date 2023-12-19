from Core.EvolutionState import EvolutionState
import math

def getBestValue(state : EvolutionState, maximize: bool) -> float:
    crrBestValue = state.fitnessFuntion.calculateValue(state.currentPopulation[0])

    if maximize:
        for specimen in state.currentPopulation:
            crrValue = state.fitnessFuntion.calculateValue(specimen)
            if crrValue > crrBestValue:
                crrBestValue = crrValue
    else:
        for specimen in state.currentPopulation:
            crrValue = state.fitnessFuntion.calculateValue(specimen)
            if crrValue < crrBestValue:
                crrBestValue = crrValue

    return crrBestValue

def getAverageValue(state : EvolutionState) -> float:
    sumValue = 0

    for specimen in state.currentPopulation:
        sumValue += state.fitnessFuntion.calculateValue(specimen)

    return sumValue / len(state.currentPopulation)

def getStandardDeviationValue(state : EvolutionState) -> float:
    avgValue = getAverageValue(state)
    newSum = 0

    for specimen in state.currentPopulation:
        crrValue = state.fitnessFuntion.calculateValue(specimen)
        newSum += (crrValue - avgValue) ** 2

    return math.sqrt(newSum / len(state.currentPopulation))