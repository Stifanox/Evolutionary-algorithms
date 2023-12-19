from Core.EvolutionManager import EvolutionManager
from Plot.PlotUtils import *
import matplotlib.pyplot as plt
from enum import Enum
import numpy as np

class PlotLayout(Enum):
    ONE_LARGE = 1,
    VERTICAL = 2,
    HORIZONTAL = 3

class Plot:
    def __init__(self, manager: EvolutionManager, layout: PlotLayout, maximize: bool):
        self.manager = manager
        self.maximize = maximize

        hspaceVar = 0
        topVar = 1

        match layout:
            case PlotLayout.ONE_LARGE:
                self.fig = plt.figure(figsize = (6, 6))
                self.bstAx = plt.subplot2grid((3, 2), (0, 0), colspan = 2, rowspan = 2)
                self.avgAx = plt.subplot2grid((3, 2), (2, 0))
                self.sdvAx = plt.subplot2grid((3, 2), (2, 1))
                hspaceVar = 0.5
                topVar = 0.95

            case PlotLayout.HORIZONTAL:
                self.fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize = (9, 3))
                self.bstAx, self.avgAx, self.sdvAx = ax.flatten()
                topVar = 0.9

            case PlotLayout.VERTICAL:
                self.fig, ax = plt.subplots(nrows = 3, ncols = 1, figsize = (3, 9))
                self.bstAx, self.avgAx, self.sdvAx = ax.flatten()
                hspaceVar = 0.3
                topVar = 0.97

            case _:
                raise ValueError("unknown PlotLayout")

        self.fig.tight_layout()
        self.fig.subplots_adjust(top = topVar, hspace = hspaceVar)

        self.xEpoch = []
        self.yBest = []
        self.yAverage = []
        self.yStdDev = []

    def update(self):
        state = self.manager.getEpochSnapshot()

        self.xEpoch.append(state.currentEpoch)
        self.yBest.append(getBestValue(state, self.maximize))
        self.yAverage.append(getAverageValue(state))
        self.yStdDev.append(getStandardDeviationValue(state))

        self.bstAx.clear()
        self.avgAx.clear()
        self.sdvAx.clear()

        self.bstAx.set_title("Best specimen")
        self.avgAx.set_title("Average")
        self.sdvAx.set_title("Standard deviation")

        self.bstAx.plot(self.xEpoch, self.yBest)
        self.avgAx.plot(self.xEpoch, self.yAverage)
        self.sdvAx.plot(self.xEpoch, self.yStdDev)

        self.fig.show()