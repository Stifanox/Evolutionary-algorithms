from tkinter import *
from tkinter import ttk
from GUI.Components.Base.DropdownGUI import DropdownGUI
from typing import List
from GUI.VariablesGUI import DropdownVariable

options = [
    "DiscreteCrossover",
    "UniformCrossover",
    "ShuffleCrossover",
    "KPointCrossover"
]


class CrossoverGUI(DropdownGUI):

    def __init__(self, state: DropdownVariable, root: Frame, optionsValues: List[str], stateForBlend: DoubleVar):
        super().__init__(state, root, optionsValues)
        self._stateForBlend = stateForBlend
        self._optionMenu.bind("<FocusIn>", self.updateCombo)

    def _renderOptions(self, root: Frame):
        super(CrossoverGUI, self)._renderOptions(root)

    def _changeFrame(self, var, index, mode):
        super(CrossoverGUI, self)._changeFrame(var, index, mode)

        if self._state.typeName.get() == "DiscreteCrossover":
            self._renderDiscreteCrossover()
        elif self._state.typeName.get() == "UniformCrossover":
            self._renderUniformCrossover()
        elif self._state.typeName.get() == "ShuffleCrossover":
            self._renderShuffleCrossover()
        elif self._state.typeName.get() == "KPointCrossover":
            self._renderKPointCrossover()
        elif self._state.typeName.get() == "ArithmeticCrossover":
            self._renderArithmeticCrossover()
        elif self._state.typeName.get() == "BlendCrossoverAlfa":
            self._renderBlendCrossoverAlfa()
        elif self._state.typeName.get() == "BlendCrossoverAlfaBeta":
            self._renderBlendCrossoverAlfaBeta()
        elif self._state.typeName.get() == "AverageCrossover":
            self._renderAverageCrossover()
        elif self._state.typeName.get() == "FlatCrossover":
            self._renderFlatCrossover()
        elif self._state.typeName.get() == "LinearCrossover":
            self._renderLinearCrossover()

    def _renderLinearCrossover(self):

        self._state.argumentValue.set(-1)
        label = ttk.Label(self._innerFrame, text="No options for linear crossover")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        entry.config(state="disabled")
        entry.pack()

    def _renderFlatCrossover(self):

        self._state.argumentValue.set(-1)
        label = ttk.Label(self._innerFrame, text="No options for flat crossover")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        entry.config(state="disabled")
        entry.pack()

    def _renderAverageCrossover(self):

        self._state.argumentValue.set(-1)
        label = ttk.Label(self._innerFrame, text="No options for average crossover")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        entry.config(state="disabled")
        entry.pack()

    def _renderBlendCrossoverAlfaBeta(self):
        self._state.argumentValue.set(0)
        self._stateForBlend.set(0)
        label = ttk.Label(self._innerFrame, text="Alfa (0,1)")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        entry.pack()

        labelTwo = ttk.Label(self._innerFrame, text="Beta (0,1)")
        labelTwo.pack()

        entryTwo = ttk.Entry(self._innerFrame, textvariable=self._stateForBlend, width=35)
        entryTwo.pack()

    def _renderBlendCrossoverAlfa(self):
        self._state.argumentValue.set(0)
        label = ttk.Label(self._innerFrame, text="Alfa (0,1)")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        entry.pack()

    def _renderArithmeticCrossover(self):
        self._state.argumentValue.set(0)
        label = ttk.Label(self._innerFrame, text="Threshold k (0,1)")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        entry.pack()

    def _renderDiscreteCrossover(self):
        self._state.argumentValue.set(0)
        label = ttk.Label(self._innerFrame, text="Threshold (0,1)")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        entry.pack()

    def _renderKPointCrossover(self):
        self._state.argumentValue.set(1)
        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        label = ttk.Label(self._innerFrame, text="Count of points to cross")
        label.pack()
        entry.pack()

    def _renderUniformCrossover(self):
        self._state.argumentValue.set(-1)
        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        label = ttk.Label(self._innerFrame, text="No options for uniform crossover")
        entry.config(state="disabled")
        label.pack()
        entry.pack()

    def _renderShuffleCrossover(self):
        self._state.argumentValue.set(-1)
        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        label = ttk.Label(self._innerFrame, text="No options for shuffle crossover")
        entry.config(state="disabled")
        label.pack()
        entry.pack()

    def updateCombo(self, event):
        self._optionMenu.configure(values=[x for x in self._options])
