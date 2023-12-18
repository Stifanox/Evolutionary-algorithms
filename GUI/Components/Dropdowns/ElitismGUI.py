from tkinter import *
from tkinter import ttk
from GUI.Components.Base.DropdownGUI import DropdownGUI
from typing import List

from GUI.VariablesGUI import DropdownVariable


class ElitismGUI(DropdownGUI):

    def __init__(self, state: DropdownVariable, root: Frame, options: List[str]):
        super().__init__(state, root, options)

    def _renderOptions(self, root: Frame):
        super(ElitismGUI, self)._renderOptions(root)

    def _changeFrame(self, var, index, mode):
        super(ElitismGUI, self)._changeFrame(var, index, mode)
        label = ttk.Label(self._innerFrame, text=f"Elitism by {self._state.typeName.get()}")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        entry.pack()
