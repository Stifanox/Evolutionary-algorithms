from tkinter import IntVar, Frame

from GUI.Components.Base.EntryGUI import EntryGUI


class SpecimenCountGUI(EntryGUI):
    def __init__(self, state: IntVar, root: Frame, label: str):
        super().__init__(state, root, label)

    def _renderCheckbox(self):
        super(SpecimenCountGUI, self)._renderCheckbox()
        
    