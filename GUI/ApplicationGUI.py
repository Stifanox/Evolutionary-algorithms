from tkinter import *
from tkinter import ttk
import matplotlib
from GUI.Components.Dropdowns.CrossoverGUI import CrossoverGUI
from GUI.Components.Dropdowns.MutationGUI import MutationGUI
from GUI.Components.Dropdowns.FunctionsGUI import FunctionGUI
from GUI.Components.Dropdowns.ElitismGUI import ElitismGUI
from GUI.VariablesGUI import DropdownVariable, CheckboxVariable
from GUI.Components.Checkboxes.InversionGUI import InversionGUI
from GUI.Components.Checkboxes.MaximizeGUI import MaximizeGUI
from GUI.Components.Entires.SpecimenCountGUI import SpecimenCountGUI
from GUI.Components.Entires.DomainGUI import DomainGUI
from GUI.Components.Entires.EpochCountGUI import EpochCountGUI
from GUI.Components.Checkboxes.ShowChartGUI import ShowChartGUI
from GUI.Components.Dropdowns.SelectionNumOrPercentGUI import SelectionNumOrPercentGUI
from GUI.Components.Dropdowns.SelectionTypeGUI import SelectionTypeGUI
from typing import Callable

mutationOptions = ["TwoPointMutation", "SinglePointMutation", "EdgeMutation"]
crossoverOptions = ["KPointCrossover", "ShuffleCrossover", "DiscreteCrossover", "UniformCrossover"]
functionOptions = ["Hypersphere", "Hyperellipsoid", "Schwefel", "Ackley", "Michalewicz", "Rastrigin", "Rosenbrock",
                   "De Jong 3", "De Jong 5", "Martin and Gaddy", "Griewank", "Easom", "Goldstein and Price",
                   "Picheny, Goldstein and Price", "Styblinski and Tang", "Mc Cormick", "Rana", "Egg Holder", "Keane",
                   "Schaffer 2", "Himmelblau", "Pits and Holes"]
numOrPercentOptions = ["Number", "Percent"]
selectionOptions = ["Top", "Roulette", "Tournament"]

matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)


class ApplicationGUI(Tk):

    def __init__(self, startEvolutionFunc: Callable):
        super().__init__()
        self.geometry("400x1000")
        self.__startEvolutionFunc = startEvolutionFunc
        self.__leftFrame = ttk.Frame()
        self.__crossoverType = DropdownVariable(StringVar(self), DoubleVar(self, value=0))
        self.__selectionType = DropdownVariable(StringVar(self), DoubleVar(self, value=0))
        self.__mutationType = DropdownVariable(StringVar(self), DoubleVar(self, value=0))
        self.__functionType = DropdownVariable(StringVar(self), DoubleVar(self, value=0))
        self.__elitismType = DropdownVariable(StringVar(self), DoubleVar(self, value=0))

        self.__useInversion = CheckboxVariable(BooleanVar(self), DoubleVar(self, value=0))
        self.__specimenCount = DoubleVar(self, value=0)
        self.__domainLowerBound = DoubleVar(self, value=0)
        self.__domainUpperBound = DoubleVar(self, value=10)
        self.__epochCount = IntVar(self, value=0)
        self.__selectionOption = DropdownVariable(StringVar(self), DoubleVar(self, value=0))
        self.__showChart = BooleanVar(self)
        self.__toMaximize = BooleanVar(self)

        self.renderElements()
        self.__leftFrame.grid(row=0, column=0, padx=(50, 0))

    def renderElements(self):
        CrossoverGUI(self.__crossoverType, self.__leftFrame, crossoverOptions)
        MutationGUI(self.__mutationType, self.__leftFrame, mutationOptions)
        FunctionGUI(self.__functionType, self.__leftFrame, functionOptions)
        ElitismGUI(self.__elitismType, self.__leftFrame, numOrPercentOptions)
        InversionGUI(self.__useInversion, self.__leftFrame, "Use inversion", "Probability (0,1)")
        MaximizeGUI(self.__toMaximize, self.__leftFrame, "Maximize value")
        SpecimenCountGUI(self.__specimenCount, self.__leftFrame, "Count of specimens")
        DomainGUI(self.__domainLowerBound, self.__leftFrame, "Lower bound of the domain")
        DomainGUI(self.__domainUpperBound, self.__leftFrame, "Upper bound of the domain")
        EpochCountGUI(self.__epochCount, self.__leftFrame, "Count of epochs")
        SelectionNumOrPercentGUI(self.__selectionType, self.__leftFrame, numOrPercentOptions)
        SelectionTypeGUI(self.__selectionOption, self.__leftFrame, selectionOptions)
        ShowChartGUI(self.__showChart, self.__leftFrame, "Show chart")
        ttk.Button(self.__leftFrame, command=self.__startEvolutionFunc, text="Start evolution").pack()

    def getParameters(self):
        parameters = {
            'crossoverType': self.__crossoverType.typeName.get(),
            'crossoverArgument': self.__crossoverType.argumentValue.get() if self.__crossoverType.argumentValue.get() != -1 else None,
            'selectionNumOrPercent': self.__selectionType.typeName.get(),
            'selectionArgument': self.__selectionType.argumentValue.get(),
            'selectionType': self.__selectionOption.typeName.get(),
            'mutationType': self.__mutationType.typeName.get(),
            'mutationProbability': self.__mutationType.argumentValue.get(),
            'functionType': self.__functionType.typeName.get(),
            'functionDimension': self.__functionType.argumentValue.get(),
            'elitismType': self.__elitismType.typeName.get(),
            'elitismArgument': self.__elitismType.argumentValue.get(),
            'useInversion': self.__useInversion.boolean.get(),
            'inversionProbability': self.__useInversion.argumentValue.get(),
            'specimenCount': self.__specimenCount.get(),
            'domainLowerBound': self.__domainLowerBound.get(),
            'domainUpperBound': self.__domainUpperBound.get(),
            'epochCount': self.__epochCount.get(),
            'showChart': self.__showChart.get(),
            'toMaximize': self.__toMaximize.get()
        }
        return parameters

    def renderPlot(self):
        data = {
            'Python': 11.27,
            'C': 11.16,
            'Java': 10.46,
            'C++': 7.5,
            'C#': 5.26
        }
        languages = data.keys()
        popularity = data.values()
        figure = Figure(figsize=(5, 5), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(languages, popularity)

        figure_canvas.get_tk_widget().grid(row=0, column=1, padx=(50, 0), pady=(50, 0))
