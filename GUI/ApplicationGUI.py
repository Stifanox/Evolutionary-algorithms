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
from GUI.Components.Entires.ChromosomePrecisionGUI import ChromosomePrecisionGUI
from typing import Callable
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)
from GUI.GUIParams import GUIParams

mutationOptions = ["TwoPointMutation", "SinglePointMutation", "EdgeMutation"]
crossoverOptions = ["KPointCrossover", "ShuffleCrossover", "DiscreteCrossover", "UniformCrossover"]
functionOptions = ["Hypersphere", "Hyperellipsoid", "Schwefel", "Ackley", "Michalewicz", "Rastrigin", "Rosenbrock",
                   "De Jong 3", "De Jong 5", "Martin And Gaddy", "Griewank", "Easom", "Goldstein and Price",
                   "Picheny, Goldstein And Price", "Styblinski And Tang", "Mc Cormick", "Rana", "Egg Holder", "Keane",
                   "Schaffer 2", "Himmelblau", "Pits And Holes"]
numOrPercentOptions = ["Number", "Percent"]
selectionOptions = ["Top", "Roulette", "Tournament"]

matplotlib.use("TkAgg")


class ApplicationGUI(Tk):

    def __init__(self, startEvolutionFunc: Callable):
        super().__init__()
        self.geometry("400x1000")
        self.__startEvolutionFunc = startEvolutionFunc
        self.__leftFrame = ttk.Frame()
        self.__crossoverType = DropdownVariable(StringVar(self), DoubleVar(self, value=2))
        self.__selectionType = DropdownVariable(StringVar(self), DoubleVar(self, value=5))
        self.__mutationType = DropdownVariable(StringVar(self), DoubleVar(self, value=0.2))
        self.__functionType = DropdownVariable(StringVar(self), DoubleVar(self, value=0))
        self.__elitismType = DropdownVariable(StringVar(self), DoubleVar(self, value=1))

        self.__useInversion = CheckboxVariable(BooleanVar(self), DoubleVar(self, value=0))
        self.__specimenCount = DoubleVar(self, value=100)
        self.__domainLowerBound = DoubleVar(self, value=-10)
        self.__domainUpperBound = DoubleVar(self, value=10)
        self.__epochCount = IntVar(self, value=100)
        self.__chromosomePrecision = IntVar(self, value=6)
        self.__selectionOption = DropdownVariable(StringVar(self), DoubleVar(self, value=0))
        self.__showChart = BooleanVar(self)
        self.__toMaximize = BooleanVar(self)

        self.renderElements()
        self.__leftFrame.grid(row=0, column=0, padx=(50, 0))

    def renderElements(self):
        ChromosomePrecisionGUI(self.__chromosomePrecision, self.__leftFrame, "Chromosome Precision")
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
        ShowChartGUI(self.__showChart, self.__leftFrame, "Show chart (will slow down simulation)")
        ttk.Button(self.__leftFrame, command=self.__startEvolutionFunc, text="Start evolution").pack()

    def getParameters(self):
        parameters = GUIParams(
            self.__crossoverType.typeName.get(),
            self.__crossoverType.argumentValue.get() if self.__crossoverType.argumentValue.get() != -1 else None,
            self.__selectionType.typeName.get(),
            self.__selectionType.argumentValue.get(),
            self.__selectionOption.typeName.get(),
            self.__mutationType.typeName.get(),
            self.__mutationType.argumentValue.get(),
            self.__functionType.typeName.get(),
            self.__functionType.argumentValue.get(),
            self.__elitismType.typeName.get(),
            self.__elitismType.argumentValue.get(),
            self.__useInversion.boolean.get(),
            self.__useInversion.argumentValue.get(),
            int(self.__specimenCount.get()),
            (self.__domainLowerBound.get(), self.__domainUpperBound.get()),
            self.__epochCount.get(),
            self.__showChart.get(),
            self.__toMaximize.get(),
            self.__chromosomePrecision.get()
        )
        return parameters

    def renderPlot(self, figure: Figure):
        # create FigureCanvasTkAgg object
        self.geometry("1000x1000")
        figure_canvas = FigureCanvasTkAgg(figure, self)
        figure_canvas.get_tk_widget().grid(row=0, column=1, padx=(50, 0), pady=(50, 0))

    def showResult(self,time:float):
        newWindow = Toplevel(self)
        newWindow.geometry("300x100")
        ttk.Label(newWindow, text=f"Time of simulation = {time}").pack()

