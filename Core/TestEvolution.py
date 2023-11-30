import benchmark_functions as bf
from Core.FitnessFunction import FitnessFunction
from Core.EvolutionManager import EvolutionManager
from Core.Utils import initRandomPopulation


# TODO: implement this test function for others
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

    # Set first population (random). If you call this method again later, the current population will be overriden
    evolutionaryManager.setFirstPopulation(initRandomPopulation(100, 6, fitnessFunction))

    # Snapshot is the current state
    # Even tho the snapshot is new object if you modify the insides of population i.e. change chromosome value,
    # this will affect the real chromosome in the evolutionManager, so pls don't do it :)
    snapshot = evolutionaryManager.getEpochSnapshot()

    # You can print all things about evolution (almost)
    print(snapshot.currentPopulation)

    # Snapshot can be printed by itself, the output won't be pretty, but for debug is good enough
    print(snapshot)
