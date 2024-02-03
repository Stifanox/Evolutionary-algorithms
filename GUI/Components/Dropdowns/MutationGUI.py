from tkinter import *
from tkinter import ttk
from typing import List
from GUI.Components.Base.DropdownGUI import DropdownGUI
from GUI.VariablesGUI import DropdownVariable



class MutationGUI(DropdownGUI):

    def __init__(self, state: DropdownVariable, root: Frame, options: List[str]):
        super().__init__(state, root, options)
        self._optionMenu.bind("<FocusIn>", self.updateCombo)

    def _renderOptions(self, root: Frame):
        super()._renderOptions(root)

    def _changeFrame(self, var, index, mode):
        super()._changeFrame(var, index, mode)

        self.__renderMutation()

    def __renderMutation(self):
        self._state.argumentValue.set(0)
        label = ttk.Label(self._innerFrame, text="Probability (0,1)")
        label.pack()

        entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
        entry.pack()

    def updateCombo(self, event):
        self._optionMenu.configure(values=[x for x in self._options])
