import numpy as np
import re
# from Core.FitnessFunction import FitnessFunction
from Core.EvolutionManager import EvolutionManager

if __name__ == '__main__':
    # test = EvolutionManager(10, 3, [(1, 2)], FitnessFunction(1, lambda x: x + 1))
    #
    # test.updateNewPopulation([])
    if re.search("^[01]+$", "1111010100010101010") is None:
        print("Wrong value")
    else:
        print("Good value")
    print(type(1))
    # x= np.array([1,2,3])
    # y = np.array([4,5,6,7])
    # x = y
    # y = np.array([])
    # print(x,y)
    pass
