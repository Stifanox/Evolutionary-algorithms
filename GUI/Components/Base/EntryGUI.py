from tkinter import *
from tkinter import ttk
from abc import ABC, abstractmethod


class EntryGUI(ABC):

    def __init__(self, state: IntVar, root: Frame, label: str):
        self._state = state
        self._label = label
        self._innerFrame = ttk.Frame(root)
        self._renderCheckbox()

    @abstractmethod
    def _renderCheckbox(self):
        label = ttk.Label(self._innerFrame, text=self._label)
        label.pack()
        entry = ttk.Entry(self._innerFrame, textvariable=self._state, width=35)
        entry.pack()
        self._innerFrame.pack(pady=(15, 0))
