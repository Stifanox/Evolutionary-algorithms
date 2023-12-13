from tkinter import *
from CrossoverGUI import CrossoverGUI


class ApplicationGUI(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.__crossoverType = StringVar(self)
        self.__selectionType = StringVar(self)
        self.__mutationType = StringVar(self)
        self.__functionType = StringVar(self)
        self.__useElitism = BooleanVar(self)
        self.__useInversion = BooleanVar(self)
        self.__specimenCount = IntVar(self)
        self.__epochCount = IntVar(self)
        self.__showChart = BooleanVar(self)

        self.renderElements()

    def renderElements(self):
        CrossoverGUI(self.__crossoverType, self)


ApplicationGUI().mainloop()
