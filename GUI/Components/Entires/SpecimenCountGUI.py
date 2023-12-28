from tkinter import DoubleVar, Frame

from GUI.Components.Base.EntryGUI import EntryGUI


class SpecimenCountGUI(EntryGUI):
    def __init__(self, state: DoubleVar, root: Frame, label: str):
        super().__init__(state, root, label)

    def _renderCheckbox(self):
        super(SpecimenCountGUI, self)._renderCheckbox()
        
    