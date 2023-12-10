from Mutation import Mutation
from Inversion import Inversion
from Core.Chromosome import Chromosome


c1 = Chromosome(2, 1, (-3, 3))
print(c1.getChromosome())

mutating = Mutation(50, c1).mutation()
print(mutating)
print(c1.getChromosome())


c2 = Chromosome(4, 1, (-6, 6))
print(f"\n{c2.getChromosome()}")

inversing = Inversion(50, c2).inversion()
print(inversing)
print(c2.getChromosome())
