from Crossover.CrossoverTypes import *

def runCrossover(parents: Collection[Specimen], crossoverType : CrossoverType, targetSize : int) -> Tuple[Specimen, ...]:
    numberOfParents = len(parents)
    newSpecimens = []

    while len(newSpecimens) < targetSize:
        xIndex = random.randrange(0, numberOfParents)
        yIndex = random.randrange(0, numberOfParents)

        while xIndex == yIndex:
            yIndex = random.randrange(0, numberOfParents)

        a, b = crossoverType.mix(parents[xIndex], parents[yIndex])
        newSpecimens.append(a)

        if len(newSpecimens) < targetSize:
            newSpecimens.append(b)

    return newSpecimens