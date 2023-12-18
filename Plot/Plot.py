from Core.EvolutionManager import EvolutionManager
import matplotlib.pyplot as plt
from enum import Enum
import numpy as np

class PlotLayout(Enum):
    ONE_LARGE = 1,
    VERTICAL = 2,
    HORIZONTAL = 3

class Plot:
    def reset(self, layout: PlotLayout):
        self.layout = layout
        match layout:
            case PlotLayout.ONE_LARGE:
                self.fig = plt.figure(figsize = (6, 6))
                self.minAx = plt.subplot2grid((3, 2), (0, 0), colspan = 2, rowspan = 2)
                self.avgAx = plt.subplot2grid((3, 2), (2, 0))
                self.sdvAx = plt.subplot2grid((3, 2), (2, 1))

            case PlotLayout.VERTICAL:
                self.fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(9, 3))
                self.minAx, self.avgAx, self.sdvAx = ax.flatten()

            case PlotLayout.HORIZONTAL:
                self.fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(3, 9))
                self.minAx, self.avgAx, self.sdvAx = ax.flatten()

        self.fig.tight_layout()

    def __init__(self, manager: EvolutionManager, layout: PlotLayout):
        self.manager = manager
        self.reset(layout)
        self.fig.show()
        self.fig.waitforbuttonpress()