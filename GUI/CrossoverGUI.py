from tkinter import *
from tkinter import ttk
from DropdownGUI import DropdownGUI
from typing import List

options = [
    "DiscreteCrossover",
    "UniformCrossover",
    "ShuffleCrossover",
    "KPointCrossover"
]


# TODO: Retrieve values for kpoints and threshold
class CrossoverGUI(DropdownGUI):

    def _init_(self, value: StringVar, root: Tk, options: List[str]):
        super(CrossoverGUI, self)._init_(value, root, options)

    def _renderOptions(self, root: Tk):
        super(CrossoverGUI, self)._renderOptions(root)

    def _changeFrame(self, var, index, mode):
        super(CrossoverGUI, self)._changeFrame(var, index, mode)

        if self._value.get() == "DiscreteCrossover":
            self._renderDiscreteCrossover()
        elif self._value.get() == "UniformCrossover":
            self._renderUniformCrossover()
        elif self._value.get() == "ShuffleCrossover":
            self._renderShuffleCrossover()
        elif self._value.get() == "KPointCrossover":
            self._renderKPointCrossover()

    def _renderDiscreteCrossover(self):
        self._argumentValue.set(0)
        label = ttk.Label(self._innerFrame, text="Threshold (0,1)")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._argumentValue, width=35)
        entry.pack()

    def _renderKPointCrossover(self):
        self._argumentValue.set(0)
        entry = ttk.Entry(self._innerFrame, textvariable=self._argumentValue, width=35)
        label = ttk.Label(self._innerFrame, text="Count of points to cross")
        label.pack()
        entry.pack()

    def _renderUniformCrossover(self):
        self._argumentValue.set(None)
        entry = ttk.Entry(self._innerFrame, textvariable=self._argumentValue, width=35)
        label = ttk.Label(self._innerFrame, text="No options for uniform crossover")
        entry.config(state="disabled")
        label.pack()
        entry.pack()

    def _renderShuffleCrossover(self):
        self._argumentValue.set(None)
        entry = ttk.Entry(self._innerFrame, textvariable=self._argumentValue, width=35)
        label = ttk.Label(self._innerFrame, text="No options for shuffle crossover")
        entry.config(state="disabled")
        label.pack()
        entry.pack()