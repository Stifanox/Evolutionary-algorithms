from Mutation import Mutation
from Core.Chromosome import Chromosome

c1 = Chromosome(2,1,(-3,3))
print(c1.getChromosome())

mutating = Mutation(100,c1).mutation()

print(c1.getChromosome())