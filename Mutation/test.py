from Mutation import *
from Inversion import Inversion
from Core.BinaryRepresentation.ChromosomeBinary import ChromosomeBinary


c1 = ChromosomeBinary(2, 1, (-3, 3))
print(c1.getChromosome())

mutating = TwoPointMutation(75).mutate(c1)
print(mutating)
print(c1.getChromosome())
mutating = SinglePointMutation(75).mutate(c1)
print(mutating)
print(c1.getChromosome())
mutating = EdgeMutation(75).mutate(c1)
print(mutating)
print(c1.getChromosome())


c2 = ChromosomeBinary(4, 1, (-6, 6))
print(f"\n{c2.getChromosome()}")

inversing = Inversion(50, c2).inversion()
print(inversing)
print(c2.getChromosome())
