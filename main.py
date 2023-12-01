from Core.EvolutionManager import EvolutionManager
import benchmark_functions as bf
from Core.Speciman import Specimen
from Core.Chromosome import Chromosome
from Core.FitnessFunction import FitnessFunction
from Core.Utils import initRandomPopulation
from Elitism.Elitism import Elitism


def functionToCalculate():
    return bf.Hypersphere()


if __name__ == '__main__':
    chromosome = Chromosome(0, 7, (-10, 10))
    chromosomeTwo = Chromosome(1, 7, (-20, 20))
    specimen = Specimen([chromosome, chromosomeTwo], 2)
    fitnessFunction = FitnessFunction(2, [(-10, 10), (-20, 20)], functionToCalculate())
    evolutionManager = EvolutionManager(10, 10, fitnessFunction)
    evolutionManager.setFirstPopulation(initRandomPopulation(10, 7, fitnessFunction))

    evolutionSnapshot = evolutionManager.getEpochSnapshot()
    currentPopulation = evolutionSnapshot.currentPopulation
    for specimenInLoop in currentPopulation:
        specimenInLoop.setSpecimenValue(evolutionSnapshot.fitnessFuntion.calculateValue(specimenInLoop))

    Elitism.selectEliteSpecimensPercent(0.41, False, evolutionManager)

