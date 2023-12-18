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


# TODO: Retrieve values for kpoints and threshold
class CrossoverGUI(DropdownGUI):

    def __init__(self, state: DropdownVariable, root: Frame, options: List[str]):
        super().__init__(state, root, options)

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

    def _renderDiscreteCrossover(self):
        self._state.argumentValue.set(0)
        label = ttk.Label(self._innerFrame, text="Threshold (0,1)")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        entry.pack()

    def _renderKPointCrossover(self):
        self._state.argumentValue.set(0)
        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        label = ttk.Label(self._innerFrame, text="Count of points to cross")
        label.pack()
        entry.pack()

    def _renderUniformCrossover(self):
        self._state.argumentValue.set(None)
        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        label = ttk.Label(self._innerFrame, text="No options for uniform crossover")
        entry.config(state="disabled")
        label.pack()
        entry.pack()

    def _renderShuffleCrossover(self):
        self._state.argumentValue.set(None)
        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        label = ttk.Label(self._innerFrame, text="No options for shuffle crossover")
        entry.config(state="disabled")
        label.pack()
        entry.pack()
