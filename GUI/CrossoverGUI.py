from tkinter import *
from tkinter import ttk

options = [
    "DiscreteCrossover",
    "UniformCrossover",
    "ShuffleCrossover",
    "KPointCrossover"
]


# TODO: Retrieve values for kpoints and threshold
class CrossoverGUI:

    def __init__(self, value: StringVar, root: Tk):
        self.__innerFrame = ttk.Frame()
        self.__value = value
        # This must be here, otherwise the variable goes out of the scope
        self.__argumentValue = DoubleVar(value=0)
        self.__renderOptions(root)

    def __renderOptions(self, root: Tk):
        frame = ttk.Frame(root, padding=20)
        frame.pack()
        optionMenu = ttk.OptionMenu(frame, self.__value, options[0], *[name for name in options])
        optionMenu.pack()

        self.__value.trace_add("write", self.__changeFrame)
        self.__innerFrame = ttk.Frame(frame, padding=10)
        self.__value.set(options[0])
        self.__innerFrame.pack()

    def __changeFrame(self, var, index, mode):
        for widget in self.__innerFrame.winfo_children():
            widget.destroy()

        if self.__value.get() == "DiscreteCrossover":
            self.__renderDiscreteCrossover()
            print()
        elif self.__value.get() == "UniformCrossover":
            pass
        elif self.__value.get() == "ShuffleCrossover":
            pass
        elif self.__value.get() == "KPointCrossover":
            self.__renderKPointCrossover()

    def __renderDiscreteCrossover(self):
        self.__argumentValue.set(0)
        label = ttk.Label(self.__innerFrame, text="Threshold (0,1)")
        label.pack()

        entry = ttk.Entry(self.__innerFrame, textvariable=self.__argumentValue, width=35)
        entry.pack()

    def __renderKPointCrossover(self):
        self.__argumentValue.set(0)
        entry = ttk.Entry(self.__innerFrame, textvariable=self.__argumentValue, width=35)
        label = ttk.Label(self.__innerFrame, text="Threshold (0,1)")
        label.pack()
        entry.pack()
