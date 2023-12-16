from typing import *

from Core.FitnessFunction import FitnessFunction
from Core.Speciman import Specimen
from Core.EvolutionState import EvolutionState
from Core.EvolutionManager import EvolutionManager
from Core.Chromosome import Chromosome



class Selection():
    """
    Class managing selection of population
    """
    LimitType_Constant = 1      #LimitValue=10 == 10 top osobnikow
    LimitType_Percentage = 2    #LimitValue=10 == 10% top osobnikow

    def __init__(self, selectionLimitType: str, selectionLimitValue: int):
        self.__selectionLimitType = selectionLimitType
        self.__selectionLimitValue = selectionLimitValue
    
    def specimenFitness(self,specimen: Specimen) -> float:
        """
        Calculate value of specimen fitness based on his chromosomes.

        :param specimen: The specimen from which we calculate value of function.
        :type specimen: Specimen
        :return: Value of fitness for given specimen
        :rtype: float
        """
        Values = []
        for chromosome in specimen.getChromosomes():
            chromosome_val = chromosome.getChromosomeNumericValue()
            chromosome_weight = 1
            # chromosome_weight = chromosome.getChromosomeWeight() #NYI
            chromosome_val_expected = 1
            # chromosome_val_expected = chromosome.getChromosomeExpectedNumericValue() #NYI
            Values.push(abs(chromosome_val_expected-chromosome_val)*chromosome_weight)
        return sum(Values) #closer to zero, the better
    
    def specimenSelection(self,specimens: Collection[Specimen]) -> Collection[Specimen]:
        """
        Select top specimens based on their fitness and selection type.

        :param specimens: The specimens to select from.
        :type specimens: Collection[Specimen]
        :return: Selected top specimens.
        :rtype: Collection[Specimen]
        """
        evaluated_specimens = [{'val': self.specimenFitness(specimen), 'specimen': specimen} for specimen in specimens] #fitness values
        evaluated_specimens = sorted(evaluated_specimens, key=lambda x: x['val']) #sorting ascended
        evaluated_specimens = [item['specimen'] for item in evaluated_specimens] #list of specimens

        specimens_selection_amount = 0
        specimens_selection_amount += int(self.__selectionLimitType==Selection.LimitType_Constant)*max(1,min(self.__selectionLimitValue,len(evaluated_specimens))) #if constant, then min(limit,len_of_species)
        specimens_selection_amount += int(self.__selectionLimitType==Selection.LimitType_Percentage)*max(1,min(int(len(evaluated_specimens)*(self.__selectionLimitValue/100)),len(evaluated_specimens))) #if percentage, then min(len_of_species*percentage,len_of_species)

        return evaluated_specimens[0:specimens_selection_amount]