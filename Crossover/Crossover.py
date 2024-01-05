from Crossover.CrossoverTypes import *

def runCrossover(parents: Collection[SpecimenBinary], crossoverType : CrossoverType, targetSize : int) -> Tuple[SpecimenBinary, ...]:
    """
    Creates a new population (children) from selected population (parents).
    It picks randomly parents and applies crossover, until target size is reached.

    :param parents: Collection[Specimen] ; Any specimen collection, from which generate new specimens.
    :param crossoverType : CrossoverType ; Any object inherited from CrossoverType.
    :param targetSize : int ; Target population count (how many children to generate).
    :return: List of newly generated specimens.
    """
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