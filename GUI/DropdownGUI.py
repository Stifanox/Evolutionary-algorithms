from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk
from typing import List


# TODO: later instead of packing use grid system
class DropdownGUI(ABC):

    def __init__(self, value: StringVar, root: Tk, options: List[str]):
        self._innerFrame = ttk.Frame()
        self._value = value
        self._options = options
        # This must be here, otherwise the variable goes out of the scope
        self._argumentValue = DoubleVar(value=0)
        self._renderOptions(root)

    @abstractmethod
    def _renderOptions(self, root: Tk):
        frame = ttk.Frame(root)
        frame.pack(pady=(5, 0))
        optionMenu = ttk.Combobox(frame, textvariable=self._value, values=self._options)
        optionMenu.config(state="readonly")
        optionMenu.pack()

        self._value.trace_add("write", self._changeFrame)
        self._innerFrame = ttk.Frame(frame)
        self._value.set(self._options[0])
        self._innerFrame.pack(pady=(5, 0))

    @abstractmethod
    def _changeFrame(self, var, index, mode):
        for widget in self._innerFrame.winfo_children():
            widget.destroy()
