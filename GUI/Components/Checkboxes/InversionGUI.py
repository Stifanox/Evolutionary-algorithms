from tkinter import Frame

from GUI.Components.Base.CheckboxWithEntryGUI import CheckboxWithEntryGUI
from GUI.VariablesGUI import CheckboxVariable


class InversionGUI(CheckboxWithEntryGUI):

    def __init__(self, state: CheckboxVariable, root: Frame, labelCheckbox: str, labelEntry: str):
        super().__init__(state, root, labelCheckbox, labelEntry)

    def _renderCheckbox(self, root: Frame):
        super(InversionGUI, self)._renderCheckbox(root)

    def _displayEntry(self, var, index, mode):
        super(InversionGUI, self)._displayEntry(var, index, mode)
