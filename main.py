from random import shuffle
from Core.EvolutionManager import EvolutionManager
import benchmark_functions as bf
from Core.Speciman import Specimen
from Core.Chromosome import Chromosome
from Core.FitnessFunction import FitnessFunction
from Core.Utils import initRandomPopulation
from Crossover.CrossoverTypes import *
from Crossover.Crossover import *

def printSpecimens(specimens : Collection[Specimen]):
    print("  Index  Chromosome A                Chromosome B")
    index = 0
    for specimen in specimens:
        a, b = specimen.getChromosomes()
        print("  {0:>5}  {1:26}  {2:9}".format(index, a.getChromosome(), b.getChromosome()))
        index += 1


if __name__ == '__main__':
    specimen1chromosomeA = Chromosome("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 7, (-2, 2))
    specimen1chromosomeB = Chromosome("123456789", 2, (-1.5, 1.5))
    specimen2chromosomeA = Chromosome("abcdefghijklmnopqrstuvwxyz", 7, (-2, 2))
    specimen2chromosomeB = Chromosome("987654321", 2, (-1.5, 1.5))
    rootSpecimens = [ Specimen([ specimen1chromosomeA, specimen1chromosomeB ], 2), Specimen([ specimen2chromosomeA, specimen2chromosomeB ], 2) ]

    target = 6
    p1kpoint1 = runCrossover(rootSpecimens, KPointCrossover(1), target)
    p1kpoint4 = runCrossover(rootSpecimens, KPointCrossover(4), target)
    p1shuffle = runCrossover(rootSpecimens, ShuffleCrossover(), target)
    p1disc015 = runCrossover(rootSpecimens, DiscreteCrossover(0.15), target)
    p1uniform = runCrossover(rootSpecimens, UniformCrossover(), target)

    p2e1 = runCrossover(rootSpecimens, KPointCrossover(1), 6)
    p2e2 = runCrossover(p2e1, KPointCrossover(3), 11)
    p2e3 = runCrossover(p2e2, UniformCrossover(), 15)
    p2e4 = runCrossover(p2e3, DiscreteCrossover(0.3), 10)
    p2e5 = runCrossover(p2e4, ShuffleCrossover(), 12)

    print("  At the beginning (epoch: 0) we have two specimens WITHOUT mixed up chromosomes:")
    print()
    printSpecimens(rootSpecimens)

    print()
    print("  ------------------------ PART 1: Different crossover algorithms ------------------------")
    print(f"  Description: From 2 parents, we generate {target} children using different crossover types")
    print()

    print("  KPointCrossover(1)")
    printSpecimens(p1kpoint1)
    print()

    print("  KPointCrossover(4)")
    printSpecimens(p1kpoint4)
    print()

    print("  ShuffleCrossover()")
    printSpecimens(p1shuffle)
    print()

    print("  DiscreteCrossover(0.15)")
    printSpecimens(p1disc015)
    print()

    print("  UniformCrossover()")
    printSpecimens(p1uniform)
    print()

    print()
    print("  ------------------------- PART 2: Multi-generational evolution -------------------------")
    print("  Description: Children are generated iteratively (epoch value is rising)")
    print()

    print("  p2e1 = runCrossover(rootSpecimens, KPointCrossover(1), 6)")
    printSpecimens(p2e1)
    print()

    print("  p2e2 = runCrossover(p2e1, KPointCrossover(3), 11)")
    printSpecimens(p2e2)
    print()

    print("  p2e3 = runCrossover(p2e2, UniformCrossover(), 15)")
    printSpecimens(p2e3)
    print()

    print("  p2e4 = runCrossover(p2e3, DiscreteCrossover(0.3), 10)")
    printSpecimens(p2e4)
    print()

    print("  p2e5 = runCrossover(p2e4, ShuffleCrossover(), 12)")
    printSpecimens(p2e5)
    print()
