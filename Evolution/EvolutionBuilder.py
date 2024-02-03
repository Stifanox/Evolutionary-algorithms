import benchmark_functions

from Mutation.Mutation import Mutation
from Mutation.Inversion import Inversion
from Crossover.CrossoverTypes import CrossoverType
from Selection.Selection import Selection
from Core.FitnessFunction import FitnessFunction
import benchmark_functions as bf
from GUI.GUIParams import GUIParams
from Mutation.Mutation import TwoPointMutation, SinglePointMutation, EdgeMutation
from Crossover.CrossoverTypes import KPointCrossover, ShuffleCrossover, DiscreteCrossover, UniformCrossover
from Elitism.Elitism import Elitism, ElitismByPercent, ElitismByCount
from Core.EvolutionManager import EvolutionManager
from Evolution.Evolution import Evolution
from typing import Tuple
from Mutation.MutationReal import UniformMutationReal
from Mutation.MutationReal import GaussMutationReal
from Crossover.CrossoverTypesReal import AverageCrossover, ArithmeticCrossover, BlendCrossoverAlfa, \
    BlendCrossoverAlfaBeta, FlatCrossover, LinearCrossover


class EvolutionBuilder:

    def __init__(self, GUIParameters: GUIParams):
        self.__selection: Selection | None = None
        self.__crossover: CrossoverType | None = None
        self.__elitism: Elitism | None = None
        self.__inverse: Inversion | None = None
        self.__mutation: Mutation | None = None
        self.__maximize = False
        self.__showChart = False
        self.__isReal = False

        self.__fitnessFunction: FitnessFunction | None = None
        self.__GUIParams = GUIParameters
        self.__setFitnessFunction()

    def setSelection(self, selectionType: str, selectionByNumberOrPercent: str, selectionSpecimenCount: int,
                     toMaximize: bool):
        selectionTypeConverted = 0
        match selectionType:
            case "Top":
                selectionTypeConverted = Selection.SelectionType_Top
            case "Roulette":
                selectionTypeConverted = Selection.SelectionType_Roulette
            case "Tournament":
                selectionTypeConverted = Selection.SelectionType_Tournament

        selectionByNumberOrPercentConverted = 0

        match selectionByNumberOrPercent:
            case "Number":
                selectionByNumberOrPercentConverted = Selection.LimitType_Constant
            case "Percent":
                selectionByNumberOrPercentConverted = Selection.LimitType_Percentage

        toMaximizeArg = Selection.EvalMethod_Maximum

        match toMaximize:
            case False:
                toMaximizeArg = Selection.EvalMethod_Minimum
            case True:
                toMaximizeArg = Selection.EvalMethod_Maximum

        self.__selection = Selection(self.__fitnessFunction, selectionTypeConverted,
                                     selectionByNumberOrPercentConverted, selectionSpecimenCount, toMaximizeArg)
        return self

    def setMutation(self, mutationType: str, mutationArgument: float):
        match mutationType:
            case "TwoPointMutation":
                self.__mutation = TwoPointMutation(mutationArgument)
            case "SinglePointMutation":
                self.__mutation = SinglePointMutation(mutationArgument)
            case "EdgeMutation":
                self.__mutation = EdgeMutation(mutationArgument)
            case "UniformMutation":
                self.__mutation = UniformMutationReal(mutationArgument)
            case "GaussMutation":
                self.__mutation = GaussMutationReal(mutationArgument)

        return self

    def setCrossover(self, crossoverType: str, crossoverArguments: Tuple[float, float]):
        match crossoverType:
            case "KPointCrossover":
                self.__crossover = KPointCrossover(int(crossoverArguments[0]))
            case "ShuffleCrossover":
                self.__crossover = ShuffleCrossover()
            case "DiscreteCrossover":
                self.__crossover = DiscreteCrossover(crossoverArguments[0])
            case "UniformCrossover":
                self.__crossover = UniformCrossover()
            case "ArithmeticCrossover":
                self.__crossover = ArithmeticCrossover(crossoverArguments[0])
            case "BlendCrossoverAlfa":
                self.__crossover = BlendCrossoverAlfa(crossoverArguments[0])
            case "BlendCrossoverAlfaBeta":
                self.__crossover = BlendCrossoverAlfaBeta(crossoverArguments[0], crossoverArguments[1])
            case "AverageCrossover":
                self.__crossover = AverageCrossover()
            case "FlatCrossover":
                self.__crossover = FlatCrossover()
            case "LinearCrossover":
                self.__crossover = LinearCrossover(self.__fitnessFunction.calculateValue, self.__maximize)

        return self

    def setElitism(self, elitismByNumberOrPercent: str, elitismArgument: float, maximize: bool):
        if elitismArgument <= 0:
            return self
        match elitismByNumberOrPercent:
            case "Number":
                self.__elitism = ElitismByCount(elitismArgument, maximize)
            case "Percent":
                self.__elitism = ElitismByPercent(elitismArgument, maximize)

        return self

    def setInverse(self, useInversion: bool, inversionProbability: float):
        if useInversion:
            self.__inverse = Inversion(inversionProbability)

        return self

    def setMaximize(self, maximize: bool):
        self.__maximize = maximize
        return self

    def setShowChart(self, showChart: bool):
        self.__showChart = showChart
        return self

    def buildEvolution(self, specimenCount: int, epochCount: int, chromosomePrecision: int):
        evoManager = EvolutionManager(specimenCount, epochCount, self.__fitnessFunction)
        evolution = Evolution(evoManager, chromosomePrecision, self.__selection, self.__crossover, self.__elitism,
                              self.__inverse,
                              self.__mutation, self.__maximize, self.__showChart, self.__fitnessFunction, self.__isReal)
        return evolution

    def setIsReal(self, isReal: bool):
        self.__isReal = isReal
        return self

    def __setFitnessFunction(self):
        benchmarkFunc = benchmark_functions.Hypersphere()
        if self.__GUIParams.functionType in ["Martin And Gaddy", "Styblinski And Tang"]:
            benchmarkFunc = getattr(bf, self.__GUIParams.functionType.replace(" ", "").replace("And", ""))(
                int(self.__GUIParams.functionDimension))
        else:
            benchmarkFunc = getattr(bf, self.__GUIParams.functionType.replace(" ", ""))(
                int(self.__GUIParams.functionDimension))

        self.__fitnessFunction = FitnessFunction(int(self.__GUIParams.functionDimension),
                                                 tuple([self.__GUIParams.domainBound] * int(
                                                     self.__GUIParams.functionDimension)),
                                                 benchmarkFunc)
