from tkinter import BooleanVar, Frame

from GUI.Components.Base.CheckboxGUI import CheckboxGUI


class MaximizeGUI(CheckboxGUI):

    def __init__(self, state: BooleanVar, root: Frame, label: str):
        super().__init__(state, root, label)

    def _renderCheckbox(self):
        super(MaximizeGUI, self)._renderCheckbox()

