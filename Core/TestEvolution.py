import benchmark_functions as bf
from Core.FitnessFunction import FitnessFunction
from Core.EvolutionManager import EvolutionManager
from Core.Utils import initRandomPopulation

#TODO: implement this test function for others
def test():
    # This file is to show how core operates

    # This can be any function, here we use out of the fox from library
    functionThatWillBeCalculated = bf.Hypersphere(2)
    # The domain of function

    functionDomainForX = (-10, 10)
    functionDomainForY = (-20, 20)

    # Two is the dimension of function (f(x,y))
    fitnessFunction = FitnessFunction(2, [functionDomainForX, functionDomainForY], functionThatWillBeCalculated)

    # Size of population | how many epoch will there be | domains for x and y variable respectively | fitness function
    evolutionaryManager = EvolutionManager(100, 100, fitnessFunction)

    # Set first population (random)
    evolutionaryManager.setFirstPopulation(initRandomPopulation(100, 6, fitnessFunction))

    print(evolutionaryManager.getEpochSnapshot())
