import numpy as np
import re
# from Core.FitnessFunction import FitnessFunction
from Core.EvolutionManager import EvolutionManager
import random
from Core.Tests.ChromosomeTest import ChromosomeTest
from Core.TestEvolution import test
from Core.Speciman import Specimen
from Core.Chromosome import Chromosome

# TODO: implement tests for all classes

if __name__ == '__main__':
    specimen = Specimen([Chromosome(-9, 6, (-10, 10))], 1)
    specimen.updateChromosomes([Chromosome(1, 6, (-10, 10))])
    chrom = Chromosome(1, 6, (-10, 10))
    print(specimen.getChromosomes())
    specimen.updateChromosomes(0,chrom)
    print(specimen.getChromosomes())
    chrom.updateChromosome("101")

