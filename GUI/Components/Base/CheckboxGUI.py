from tkinter import *
from tkinter import ttk
from abc import ABC, abstractmethod


class CheckboxGUI(ABC):

    def __init__(self, state: BooleanVar, root: Frame, label: str):
        self._state = state
        self._label = label
        self._innerFrame = ttk.Frame(root)
        self._renderCheckbox()

    @abstractmethod
    def _renderCheckbox(self):
        checkbox = ttk.Checkbutton(self._innerFrame, text=self._label, takefocus=0, variable=self._state)
        checkbox.grid(row=0, column=0)
        self._innerFrame.pack(pady=(15, 0))


