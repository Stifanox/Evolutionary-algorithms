from tkinter import *
from tkinter import ttk
from DropdownGUI import DropdownGUI
from typing import List


class ElitismGUI(DropdownGUI):

    def __init__(self, value: StringVar, root: Tk, options: List[str]):
        super().__init__(value, root, options)

    def _renderOptions(self, root: Tk):
        super(ElitismGUI, self)._renderOptions(root)

    def _changeFrame(self, var, index, mode):
        super(ElitismGUI, self)._changeFrame(var, index, mode)
        label = ttk.Label(self._innerFrame, text=f"Elitism by {self._value.get()}")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._argumentValue, width=35)
        entry.pack()
