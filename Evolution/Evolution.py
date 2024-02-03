import time

from Core.EvolutionManager import EvolutionManager
from Selection.Selection import Selection
from Crossover.CrossoverTypes import CrossoverType
from Elitism.Elitism import Elitism
from Mutation.Inversion import Inversion
from Mutation.Mutation import Mutation
from Plot.Plot import Plot, PlotLayout
from FileExport.FileExport import FileExport, FileExportVariant
from Core.Utils import initRandomBinaryPopulation
from Core.FitnessFunction import FitnessFunction
import random
from typing import Callable, Collection
from matplotlib.figure import Figure
from Core.Chromosome import Chromosome
from Core.RealRepresentation.testReal import initRandomRealPopulation


class Evolution:

    def __init__(self, evoManager: EvolutionManager,
                 chromosomePrecision: int,
                 selection: Selection | None,
                 crossover: CrossoverType | None,
                 elitism: Elitism | None,
                 inverse: Inversion | None,
                 mutation: Mutation | None,
                 maximize: bool,
                 showChart: bool,
                 fitnessFunction: FitnessFunction,
                 isReal: bool):
        self.__evoManager = evoManager
        self.__selection: Selection | None = selection
        self.__crossover: CrossoverType | None = crossover
        self.__elitism: Elitism | None = elitism
        self.__inverse: Inversion | None = inverse
        self.__mutation: Mutation | None = mutation
        self.__maximize = maximize
        self.__showChart = showChart
        self.__chromosomePrecision = chromosomePrecision
        self.__isReal = isReal

        self.__fitnessFunction = fitnessFunction
        self.__plot = Plot(evoManager, PlotLayout.ONE_LARGE, self.__maximize, 1)
        self.__saveToFile = FileExport(evoManager, "EvolutionSave")

        self.__timeOfEvolution = 0

    def startEvolution(self, renderPlot: Callable[[bool, Figure], None],
                       showResult: Callable[[float, float, Collection[Chromosome]], None]):
        # Init 1st population
        startTime = time.time()
        prevTime = startTime
        initPopulation = []

        if self.__isReal:
            initPopulation = initRandomRealPopulation(self.__evoManager.getEpochSnapshot().populationSize,
                                                      self.__fitnessFunction)
        else:
            initPopulation = initRandomBinaryPopulation(self.__evoManager.getEpochSnapshot().populationSize,
                                                        self.__chromosomePrecision, self.__fitnessFunction)
        self.__evoManager.setFirstPopulation(initPopulation)

        # Show chart
        if self.__showChart:
            self.__plot.refreshData()
            self.__plot.redraw()
            renderPlot(True, self.__plot.getFigure())
        # For epoch count
        for i in range(self.__evoManager.getEpochSnapshot().epochCount):
            # Evaluation
            for specimen in self.__evoManager.getEpochSnapshot().currentPopulation:
                specimen.setSpecimenValue(self.__fitnessFunction.calculateValue(specimen))

            # Elitism
            if self.__elitism is not None:
                self.__evoManager.updateNewPopulation(
                    self.__elitism.selectBest(self.__evoManager.getEpochSnapshot().currentPopulation))

            # Selection
            self.__evoManager.updateSelectedPopulation(
                self.__selection.selection(self.__evoManager.getEpochSnapshot().currentPopulation))

            # Crossover
            while self.__evoManager.getEpochSnapshot().populationSize > len(
                    self.__evoManager.getEpochSnapshot().newPopulation):
                specimens = self.__crossover.mix(random.choice(self.__evoManager.getEpochSnapshot().selectedPopulation),
                                                 random.choice(self.__evoManager.getEpochSnapshot().selectedPopulation))
                if len(self.__evoManager.getEpochSnapshot().newPopulation) + 1 >= self.__evoManager.getEpochSnapshot().populationSize:
                    self.__evoManager.updateNewPopulation([specimens[0]])
                else:
                    self.__evoManager.updateNewPopulation(specimens)

            # Mutation
            for specimen in self.__evoManager.getEpochSnapshot().newPopulation:
                for chromosome in specimen.getChromosomes():
                    self.__mutation.mutate(chromosome)

            if self.__inverse is not None:
                for specimen in self.__evoManager.getEpochSnapshot().newPopulation:
                    for chromosome in specimen.getChromosomes():
                        startEndPositionsToInverse = self.__inverse.inversion(chromosome)
                        if not isinstance(startEndPositionsToInverse, str):
                            (start, end) = startEndPositionsToInverse
                            oldChromo = chromosome.getChromosomeBinaryValue()
                            newChromosome = oldChromo[0:start] + oldChromo[end:max(start - 1, 0):-1] + oldChromo[
                                                                                                       end + 1 if start != 0 else end:]
                            chromosome.updateChromosome(newChromosome)

            for specimen in self.__evoManager.getEpochSnapshot().newPopulation:
                specimen.setSpecimenValue(self.__fitnessFunction.calculateValue(specimen))

            print("Best specimen in population: ", end="")
            if self.__maximize:
                print(max(self.__evoManager.getEpochSnapshot().newPopulation,
                          key=lambda x: x.getSpecimenValue()).getSpecimenValue())
            else:
                print(min(self.__evoManager.getEpochSnapshot().newPopulation,
                          key=lambda x: x.getSpecimenValue()).getSpecimenValue())

            self.__plot.refreshData()
            crrTime = time.time()

            if crrTime - prevTime > 0.3 and self.__showChart:  # refresh period (in seconds)
                prevTime = crrTime
                self.__plot.redraw()
                renderPlot(False, self.__plot.getFigure())

            # FIXME: uncomment if wanted to be saved to files

            # self.__saveToFile.export(FileExportVariant.Best, self.__maximize)
            # self.__saveToFile.export(FileExportVariant.Average, self.__maximize)
            # self.__saveToFile.export(FileExportVariant.StandardDeviation, self.__maximize)

            # Go to next epoch
            self.__evoManager.updateEpoch()

        if self.__showChart:
            self.__plot.refreshData()
            self.__plot.redraw()
            renderPlot(False, self.__plot.getFigure())

        endTime = time.time()

        # Last eval
        for specimen in self.__evoManager.getEpochSnapshot().currentPopulation:
            specimen.setSpecimenValue(self.__fitnessFunction.calculateValue(specimen))

        if self.__maximize:
            bestSpecimen = sorted(self.__evoManager.getEpochSnapshot().currentPopulation, reverse=True,
                                  key=lambda x: x.getSpecimenValue())[0]
            showResult(endTime - startTime, bestSpecimen.getSpecimenValue(), bestSpecimen.getChromosomes())
        else:
            bestSpecimen = sorted(self.__evoManager.getEpochSnapshot().currentPopulation,
                                  key=lambda x: x.getSpecimenValue())[0]
            showResult(endTime - startTime, bestSpecimen.getSpecimenValue(), bestSpecimen.getChromosomes())
