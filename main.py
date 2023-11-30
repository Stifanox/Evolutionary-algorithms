from Core.EvolutionManager import EvolutionManager
import benchmark_functions as bf
from Core.Speciman import Specimen
from Core.Chromosome import Chromosome
from Core.FitnessFunction import FitnessFunction
from Core.Utils import initRandomPopulation


def functionToCalculate():
    return bf.Hypersphere()


if __name__ == '__main__':
    chromosome = Chromosome(0, 7, (-10, 10))
    chromosomeTwo = Chromosome(1, 7, (-20, 20))
    specimen = Specimen([chromosome, chromosomeTwo], 2)
    fitnessFunction = FitnessFunction(2, [(-10, 10), (-20, 20)], functionToCalculate())
    evolutionManager = EvolutionManager(10, 10, fitnessFunction)
    evolutionManager.setFirstPopulation(initRandomPopulation(10, 7, fitnessFunction))

    evoSnapshot = evolutionManager.getEpochSnapshot()

    evolutionManager.updateSelectedPopulation([evoSnapshot.currentPopulation[0], evoSnapshot.currentPopulation[1]])

    arr = [x for x in evoSnapshot.currentPopulation]
    arr.extend([evoSnapshot.currentPopulation[1]])
    evolutionManager.updateNewPopulation(arr)

    for i in range(11):
        evolutionManager.updateEpoch()

    print(evolutionManager.getEpochSnapshot())
