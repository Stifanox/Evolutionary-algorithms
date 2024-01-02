from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
from typing import List
from GUI.VariablesGUI import DropdownVariable


class DropdownGUI(ABC):

    def __init__(self, state: DropdownVariable, root: Frame, options: List[str]):
        self._innerFrame = ttk.Frame()
        self._state = state
        self._options = options
        self._renderOptions(root)

    @abstractmethod
    def _renderOptions(self, root: Frame):
        frame = ttk.Frame(root)
        frame.pack(pady=(15, 0))
        optionMenu = ttk.Combobox(frame, textvariable=self._state.typeName, values=self._options)
        optionMenu.config(state="readonly")
        optionMenu.pack()

        self._state.typeName.trace_add("write", self._changeFrame)
        self._innerFrame = ttk.Frame(frame)
        self._state.typeName.set(self._options[0])
        self._innerFrame.pack(pady=(5, 0))

    @abstractmethod
    def _changeFrame(self, var, index, mode):
        for widget in self._innerFrame.winfo_children():
            widget.destroy()
