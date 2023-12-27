from datetime import datetime
from enum import Enum

from Core.EvolutionManager import EvolutionManager
from Plot.PlotUtils import getBestValue, getAverageValue, getStandardDeviationValue


class FileExportVariant(Enum):
    Best = 1,
    Average = 2,
    StandardDeviation = 3


class FileExport:
    """
    FileExport is a class for exporting data from evolution process to a file.
    """

    def __init__(self, manager: EvolutionManager, path: str, timestamp: bool = True):
        """
        :param manager: reference to the EvolutionManager object.
        :param path: string of filename without extension.
        :param timestamp: if true, it adds timestamp to the filename at the end.
        Timestamp is evaluated at the time of initialization of the FileExport object.
        """
        self.manager = manager
        self.path = path
        self.timestamp = f'_{datetime.now().strftime("%Y_%m_%d-%H_%M_%S_%f")[:-3]}' if timestamp else ""
        self.header = False

    def export(self, variant: FileExportVariant, maximize: bool = True):
        """
        Export data to a file.
        :param variant: FileExportVariant ; selected variant of data to export.
        :param maximize: if true, it finds maximum 'Best specimen' value, otherwise minimum.
        Applies only to 'Best' variant of export. Otherwise, it is ignored.
        """
        state = self.manager.getEpochSnapshot()

        def value_lambda():
            return 0

        match variant:
            case FileExportVariant.Best:
                value_lambda = lambda: getBestValue(state, maximize)
            case FileExportVariant.Average:
                value_lambda = lambda: getAverageValue(state)
            case FileExportVariant.StandardDeviation:
                value_lambda = lambda: getStandardDeviationValue(state)
            case _:
                raise ValueError("unknown FileExportVariant")

        if not self.header:
            self.header = True
            with open(f'{self.path}_{variant.name}{self.timestamp}.txt', 'w') as file:
                file.write(f'epoch;value_{variant.name}\n')

        with open(f'{self.path}_{variant.name}{self.timestamp}.txt', 'a') as file:
            file.write(f'{state.currentEpoch};{value_lambda()}\n')
