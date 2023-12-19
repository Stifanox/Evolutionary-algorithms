from tkinter import *
from tkinter import ttk
from abc import ABC, abstractmethod
from GUI.VariablesGUI import CheckboxVariable


class CheckboxWithEntryGUI(ABC):

    def __init__(self, state: CheckboxVariable, root: Frame, labelCheckbox: str, labelEntry: str):
        self._state = state
        self._labelCheckbox = labelCheckbox
        self._labelEntry = labelEntry
        self._innerFrame = ttk.Frame()
        self._renderCheckbox(root)

    @abstractmethod
    def _renderCheckbox(self, root: Frame):
        frame = ttk.Frame(root)
        self._innerFrame = ttk.Frame(frame)
        checkbox = ttk.Checkbutton(frame, text=self._labelCheckbox, takefocus=0,
                                   variable=self._state.boolean)
        checkbox.pack()
        self._innerFrame.pack()
        frame.pack(pady=(15, 0))
        self._state.boolean.trace_add("write", self._displayEntry)

    @abstractmethod
    def _displayEntry(self, var, index, mode):
        for widget in self._innerFrame.winfo_children():
            widget.destroy()

        self._innerFrame.config(height=1)

        if self._state.boolean.get():
            label = ttk.Label(self._innerFrame, text=self._labelEntry)
            entry = ttk.Entry(self._innerFrame, textvariable=self._state.argumentValue, width=35)
            label.pack()
            entry.pack()
