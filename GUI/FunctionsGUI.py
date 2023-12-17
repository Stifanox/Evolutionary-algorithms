from tkinter import *
from tkinter import ttk
from DropdownGUI import DropdownGUI
from typing import List


class FunctionGUI(DropdownGUI):

    def __init__(self, value: StringVar, root: Tk, options: List[str]):
        super().__init__(value, root, options)

    def _renderOptions(self, root: Tk):
        super(FunctionGUI, self)._renderOptions(root)

    def _changeFrame(self, var, index, mode):
        super(FunctionGUI, self)._changeFrame(var, index, mode)
        self._argumentValue.set(1)
        label = ttk.Label(self._innerFrame, text=f"Dimension of function {self._value.get()}")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._argumentValue, width=35)
        entry.pack()
