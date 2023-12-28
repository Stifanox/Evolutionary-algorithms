from tkinter import BooleanVar, Frame

from GUI.Components.Base.CheckboxGUI import CheckboxGUI

class ShowChartGUI(CheckboxGUI):

    def __init__(self, state: BooleanVar, root: Frame, label: str):
        super().__init__(state, root, label)

    def _renderCheckbox(self):
        super(ShowChartGUI, self)._renderCheckbox()