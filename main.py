import numpy as np
from Core.FitnessFunction import FitnessFunction

if __name__ == '__main__':
    test = EvolutionData.EvolutionData(10, 3, [(1, 2)], FitnessFunction(1, lambda x: x + 1))
    #
    # test.updateNewPopulation([])

    x= np.array([1,2,3])
    y = np.array([4,5,6,7])
    x = y
    y = np.array([])
    print(x,y)
    pass
