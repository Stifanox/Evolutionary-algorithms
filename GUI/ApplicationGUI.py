from tkinter import *
from tkinter import ttk
from GUI.Components.Dropdowns.CrossoverGUI import CrossoverGUI
from GUI.Components.Dropdowns.MutationGUI import MutationGUI
from GUI.Components.Dropdowns.FunctionsGUI import FunctionGUI
from GUI.Components.Dropdowns.ElitismGUI import ElitismGUI
from GUI.VariablesGUI import DropdownVariable, CheckboxVariable
from GUI.Components.Checkboxes.InversionGUI import InversionGUI
from GUI.Components.Checkboxes.MaximizeGUI import MaximizeGUI
from GUI.Components.Entires.SpecimenCountGUI import SpecimenCountGUI

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
        self.geometry("500x600")
        self.__leftFrame = ttk.Frame()
        self.__crossoverType = DropdownVariable(StringVar(self), DoubleVar(self, value=0))
        self.__selectionType = DropdownVariable(StringVar(self), DoubleVar(self, value=0))
        self.__mutationType = DropdownVariable(StringVar(self), DoubleVar(self, value=0))
        self.__functionType = DropdownVariable(StringVar(self), DoubleVar(self, value=0))
        self.__elitismType = DropdownVariable(StringVar(self), DoubleVar(self, value=0))

        self.__useInversion = CheckboxVariable(BooleanVar(self), DoubleVar(self, value=0))
        self.__specimenCount = IntVar(self, value=0)
        self.__epochCount = IntVar(self, value=0)
        self.__showChart = BooleanVar(self)
        self.__toMaximize = BooleanVar(self)

        self.renderElements()
        self.__leftFrame.grid(row=0, column=0, padx=(50, 0))

    def renderElements(self):
        CrossoverGUI(self.__crossoverType, self.__leftFrame, crossoverOptions)
        MutationGUI(self.__mutationType, self.__leftFrame, mutationOptions)
        FunctionGUI(self.__functionType, self.__leftFrame, functionOptions)
        ElitismGUI(self.__elitismType, self.__leftFrame, elitismOptions)
        InversionGUI(self.__useInversion, self.__leftFrame, "Use inversion", "Probability (0,1)")
        MaximizeGUI(self.__toMaximize, self.__leftFrame, "Maximize value")
        SpecimenCountGUI(self.__specimenCount, self.__leftFrame, "Count of specimens")


ApplicationGUI().mainloop()
