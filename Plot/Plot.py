from Core.EvolutionManager import EvolutionManager
from Plot.PlotUtils import *
import matplotlib.pyplot as plt
from enum import Enum
import numpy as np
from typing import *

class PlotLayout(Enum):
    ONE_LARGE = 1,
    VERTICAL = 2,
    HORIZONTAL = 3

class Plot:
    def __init__(self, manager: EvolutionManager, layout: PlotLayout, maximize: bool, scale: float):
        """
        :param: manager ; Reference to the EvolutionManager object.
        :param: layout ; Selected layout (how plots should be arranged - see 'PlotLayout' enum).
        :param: maximize ; If true, it finds maximum 'Best specimen' value, otherwise minimum.
        :param: scale ; Floating point scale of rendered plots. By default, it should be set to 1.
        """

        self.manager = manager
        self.maximize = maximize
        self.scale = scale

        hspaceVar = 0
        topVar = 1

        match layout:
            case PlotLayout.ONE_LARGE:
                self.xsize, self.ysize = 6 * self.scale, 6 * self.scale
                self.fig = plt.figure(figsize = (self.xsize, self.ysize))
                self.bstAx = plt.subplot2grid((3, 2), (0, 0), colspan = 2, rowspan = 2)
                self.avgAx = plt.subplot2grid((3, 2), (2, 0))
                self.sdvAx = plt.subplot2grid((3, 2), (2, 1))
                hspaceVar = 0.5
                topVar = 0.95

            case PlotLayout.HORIZONTAL:
                self.xsize, self.ysize = 9 * self.scale, 3 * self.scale
                self.fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize = (self.xsize, self.ysize))
                self.bstAx, self.avgAx, self.sdvAx = ax.flatten()
                topVar = 0.9

            case PlotLayout.VERTICAL:
                self.xsize, self.ysize = 3 * self.scale, 9 * self.scale
                self.fig, ax = plt.subplots(nrows = 3, ncols = 1, figsize = (self.xsize, self.ysize))
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

    def getFigure(self) -> plt.Figure:
        """
        :return: 'Figure' object containing plots.
        """
        return self.fig

    def getTargetResolution(self) -> Tuple[int, int]:
        """
        :return: Target resolution in pixels (note: if user resizes the window, the values do not change).
        """
        return tuple([int(self.xsize * 100), int(self.ysize * 100)])

    def refreshData(self):
        """
        Gathers and saves data internally based on previously set 'manager' object reference.
        It should be called after each epoch (to prevent missing data points).
        """
        state = self.manager.getEpochSnapshot()
        self.xEpoch.append(state.currentEpoch)
        self.yBest.append(getBestValue(state, self.maximize))
        self.yAverage.append(getAverageValue(state))
        self.yStdDev.append(getStandardDeviationValue(state))

    def redraw(self):
        """
        Updates plots based on previously stored data by the 'refreshData()' method.
        It should be called after 'refreshData()', with some interval (e.g. every 'n' number of iterations).
        """
        self.bstAx.clear()
        self.avgAx.clear()
        self.sdvAx.clear()

        self.bstAx.set_title("Best specimen")
        self.avgAx.set_title("Average")
        self.sdvAx.set_title("Standard deviation")

        self.bstAx.plot(self.xEpoch, self.yBest)
        self.avgAx.plot(self.xEpoch, self.yAverage)
        self.sdvAx.plot(self.xEpoch, self.yStdDev)