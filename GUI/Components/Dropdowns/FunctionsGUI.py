from tkinter import *
from tkinter import ttk
from GUI.Components.Base.DropdownGUI import DropdownGUI
from typing import List

from GUI.VariablesGUI import DropdownVariable


class FunctionGUI(DropdownGUI):

    def __init__(self, state: DropdownVariable, root: Frame, options: List[str]):
        super().__init__(state, root, options)

    def _renderOptions(self, root: Frame):
        super(FunctionGUI, self)._renderOptions(root)

    def _changeFrame(self, var, index, mode):
        super(FunctionGUI, self)._changeFrame(var, index, mode)
        self._state.argumentValue.set(1)
        label = ttk.Label(self._innerFrame, text=f"Dimension of function {self._state.typeName.get()}")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        entry.pack()
