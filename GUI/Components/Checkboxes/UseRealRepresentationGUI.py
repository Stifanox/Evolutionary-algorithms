from GUI.Components.Base.CheckboxGUI import CheckboxGUI
from tkinter import BooleanVar, Frame
from typing import List

mutationBinaryOptions = ["TwoPointMutation", "SinglePointMutation", "EdgeMutation"]
mutationRealOptions = ["UniformMutation", "GaussMutation"]

crossoverBinaryOptions = ["KPointCrossover", "ShuffleCrossover", "DiscreteCrossover", "UniformCrossover"]
crossoverRealOptions = ["ArithmeticCrossover", "BlendCrossoverAlfa", "BlendCrossoverAlfaBeta", "AverageCrossover","FlatCrossover","LinearCrossover"]

class UseRealRepresentationGUI(CheckboxGUI):
    def __init__(self, state: BooleanVar, root: Frame, label: str, mutationList: List[str], crossoverList:List[str]):
        super().__init__(state, root, label)
        self._mutationList = mutationList
        self._crossoverList = crossoverList
        self._state.trace_add("write", self.__changeData)

    def _renderCheckbox(self):
        super(UseRealRepresentationGUI, self)._renderCheckbox()

    def __changeData(self, var, index, mode):
        mutationUsed = []
        crossoverUsed = []

        if self._state.get():
            mutationUsed = mutationRealOptions
            crossoverUsed = crossoverRealOptions
        else:
            mutationUsed = mutationBinaryOptions
            crossoverUsed = crossoverBinaryOptions

        self._mutationList.clear()
        self._crossoverList.clear()

        self._mutationList.extend(mutationUsed)
        self._crossoverList.extend(crossoverUsed)
