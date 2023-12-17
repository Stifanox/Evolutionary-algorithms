from tkinter import *
from tkinter import ttk
from typing import List
from DropdownGUI import DropdownGUI


class MutationGUI(DropdownGUI):

    def __init__(self, value: StringVar, root: Tk, options: List[str]):
        super().__init__(value, root, options)

    def _renderOptions(self, root: Tk):
        super()._renderOptions(root)

    def _changeFrame(self, var, index, mode):
        super()._changeFrame(var, index, mode)

        self.__renderMutation()
        # if super()._value.get() == "EdgeMutation":
        #     pass
        # elif super()._value.get() == "SinglePointMutation":
        #     pass
        # elif super()._value.get() == "TwoPointMutation":
        #     pass

    def __renderMutation(self):
        self._argumentValue.set(0)
        label = ttk.Label(self._innerFrame, text="Probability (0,1)")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._argumentValue, width=35)
        entry.pack()
