from tkinter import *
from CrossoverGUI import CrossoverGUI
from MutationGUI import MutationGUI
from FunctionsGUI import FunctionGUI
from ElitismGUI import ElitismGUI

mutationOptions = ["TwoPointMutation", "SinglePointMutation", "EdgeMutation"]
crossoverOptions = ["KPointCrossover", "ShuffleCrossover", "DiscreteCrossover", "UniformCrossover"]
functionOptions = ["Hypersphere", "Hyperellipsoid", "Schwefel", "Ackley", "Michalewicz", "Rastrigin", "Rosenbrock",
                   "De Jong 3", "De Jong 5", "Martin and Gaddy", "Griewank", "Easom", "Goldstein and Price",
                   "Picheny, Goldstein and Price", "Styblinski and Tang", "Mc Cormick", "Rana", "Egg Holder", "Keane",
                   "Schaffer 2", "Himmelblau", "Pits and Holes"]
elitismOptions = ["Number", "Percent"]


class ApplicationGUI(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.__crossoverType = StringVar(self)
        self.__selectionType = StringVar(self)
        self.__mutationType = StringVar(self)
        self.__functionType = StringVar(self)
        self.__elitismType = StringVar(self)
        self.__useInversion = BooleanVar(self)
        self.__specimenCount = IntVar(self)
        self.__epochCount = IntVar(self)
        self.__showChart = BooleanVar(self)
        self.__toMaximize = BooleanVar(self)

        self.renderElements()

    def renderElements(self):
        CrossoverGUI(self.__crossoverType, self, crossoverOptions)
        MutationGUI(self.__mutationType, self, mutationOptions)
        FunctionGUI(self.__functionType, self, functionOptions)
        ElitismGUI(self.__elitismType, self, elitismOptions)


ApplicationGUI().mainloop()
