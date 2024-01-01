from typing import *
import random


if __name__ == "__main__":
    #personal testing purposes
    class Specimen:
        def __init__(self):
            self.val = round(random.uniform(-20,20)*100)/100
    class FitnessFunction:
        def calculateValue(self, specimen: Specimen) -> float:
            return specimen.val
else:
    from Core.FitnessFunction import FitnessFunction
    from Core.Speciman import Specimen
    from Core.EvolutionState import EvolutionState
    from Core.EvolutionManager import EvolutionManager
    from Core.Chromosome import Chromosome




class Selection():
    """
    Class managing selection of population
    """
    
    SelectionType_Top = 1   #Top - we choose n amount of best specimens
    SelectionType_Roulette = 2    #Roulette - random, where fitness is a weight
    SelectionType_Tournament = 3    #Tournament - specimens fight each other in brackets untill there are more then desired specimens

    LimitType_Constant = 1      #LimitValue=10 == 10 top osobnikow
    LimitType_Percentage = 2    #LimitValue=10 == 10% top osobnikow

    EvalMethod_Minimum = 1      #closer to zero the specimen fitness, the better
    EvalMethod_Maximum = 2    #higher the specimen fitness, the better

    def __init__(self, fitnessFunction: FitnessFunction, selectionType: int, selectionLimitType: str, selectionLimitValue: int, selectionEvalMethod: int):
        """
        Constructor for Selection class

        :param fitnessFunction: Function to evaluate specimen fitness.
        :type fitnessFunction: FitnessFunction

        :param selectionType: Type of selection (Top,Roulette,Tournament).
        :type selectionType: int

        :param selectionLimitType: Type of final amount of selected specimens (Constant,Percentage).
        :type selectionLimitType: int

        :param selectionLimitValue: Value of final amount of selected specimens (Constant,Percentage).
        :type selectionLimitValue: int

        :param selectionEvalMethod: Method of evaluating specimens fitness (Minimum,Maximum).
        :type selectionEvalMethod: int
        """
        self.__fitnessFunction = fitnessFunction
        self.__selectionType = selectionType
        self.__selectionLimitType = selectionLimitType
        self.__selectionLimitValue = selectionLimitValue
        self.__selectionEvalMethod = selectionEvalMethod
        
        self.__specimens_selection_amount = 0


    def selection(self,specimens: Collection[Specimen]) -> Collection[Specimen]:
        """
        Select specimens based on their fitness and selection type.

        :param specimens: The specimens to select from.
        :type specimens: Collection[Specimen]
        :return: Selected top specimens.
        :rtype: Collection[Specimen]
        """
        specimens_dict = [{'val': self.__fitnessFunction.calculateValue(specimen), 'specimen': specimen} for specimen in specimens] #fitness values        

        if self.__selectionEvalMethod == Selection.EvalMethod_Minimum: #normalizing all values to be closest to minimum for MINIMUM
            specimens_dict = [{'val':abs(specimen['val']),'specimen':specimen['specimen']} for specimen in specimens_dict]

        if self.__selectionEvalMethod == Selection.EvalMethod_Maximum: #normalizing all values to be closest to minimum for MAXIMUM
            specimens_dict_val_min = min([item['val'] for item in specimens_dict])
            specimens_dict = [{'val':specimen['val']-specimens_dict_val_min,'specimen':specimen['specimen']} for specimen in specimens_dict]
            specimens_dict_val_max = max([item['val'] for item in specimens_dict])
            specimens_dict = [{'val':abs(specimen['val']-specimens_dict_val_max),'specimen':specimen['specimen']} for specimen in specimens_dict]
            #now the biggest value is 0 and the rest is ascending from it

        self.__specimens_selection_amount = 0
        self.__specimens_selection_amount += int(self.__selectionLimitType==Selection.LimitType_Constant)*max(1,min(self.__selectionLimitValue,len(specimens_dict))) #if constant, then min(limit,len_of_species)
        self.__specimens_selection_amount += int(self.__selectionLimitType==Selection.LimitType_Percentage)*max(1,min(int(len(specimens_dict)*(self.__selectionLimitValue/100)),len(specimens_dict))) #if percentage, then min(len_of_species*percentage,len_of_species)
        
        specimens_dict_return = []
        if self.__selectionType == Selection.SelectionType_Top:
            specimens_dict_return = self.__selection_Top(specimens_dict)
            
        if self.__selectionType == Selection.SelectionType_Roulette:
            specimens_dict_return = self.__selection_Roulette(specimens_dict)

        if self.__selectionType == Selection.SelectionType_Tournament:
            specimens_dict_return = self.__selection_Tournament(specimens_dict)
        
        specimens_dict_return = sorted(specimens_dict_return, key=lambda x: x['val']) #sorting ascending
        specimens_selected = [item['specimen'] for item in specimens_dict_return] #list of specimens
        return specimens_selected


    def __selection_Top(self,specimens_dict: Collection[Specimen]) -> Collection[Specimen]:
        specimens_dict = sorted(specimens_dict, key=lambda x: x['val']) #sorting ascending
        return specimens_dict[0:self.__specimens_selection_amount] #choose best n

    def __selection_Roulette(self,specimens_dict: Collection[Specimen]) -> Collection[Specimen]:
        while len(specimens_dict)>self.__specimens_selection_amount: #while we have more specimen than desired
            weights = [d['val'] for d in specimens_dict] #create list of weights (fitness)
            index_to_kill = random.choices(range(len(specimens_dict)), weights=weights, k=1)[0] #choose index to kill
            specimens_dict.pop(index_to_kill) #remove from list of specimen (kill)
        return specimens_dict

    def __selection_Tournament(self,specimens_dict: Collection[Specimen]) -> Collection[Specimen]:
        while len(specimens_dict)>self.__specimens_selection_amount: # continue untill we have a desired number of selected species.
            for i in range(len(specimens_dict)): specimens_dict[i]['points'] = 0 #reset bracket points
            specimens_dict_indexes = [i for i in range(len(specimens_dict))] #indexes for bracket pairs
            random.shuffle(specimens_dict_indexes) #random setup of brackets
            for i in range(0,len(specimens_dict_indexes),2):
                if i+1<len(specimens_dict_indexes):
                    index1 = specimens_dict_indexes[i]
                    index2 = specimens_dict_indexes[i+1]

                    #fights
                    if specimens_dict[index1]['val']<specimens_dict[index2]['val']: specimens_dict[index1]['points'] += 1
                    if specimens_dict[index1]['val']>specimens_dict[index2]['val']: specimens_dict[index2]['points'] += 1
                    if specimens_dict[index1]['val']==specimens_dict[index2]['val']: specimens_dict[random.choice([index1,index2])]['points'] += 1
                    
            specimens_dict = sorted(specimens_dict, key=lambda x: x['points'])[::-1] #sorting descending, from winners to losers
            specimens_dict_choose = max(self.__specimens_selection_amount,int(len(specimens_dict)/2)) #select half of winners, minumum n
            specimens_dict = specimens_dict[0:specimens_dict_choose] #select winners
        return specimens_dict




if __name__ == "__main__":

    # SelLimitType = Selection.LimitType_Constant
    SelLimitType = Selection.LimitType_Percentage
    SelLimitVal = 18
    # SelEvalMethod = Selection.EvalMethod_Minimum
    SelEvalMethod = Selection.EvalMethod_Maximum
    
    print("TEST ________ Selection TOP ________________________________________________")
    SpecimensToBeSelected = []
    SpecimenAmount = random.randint(56,88)
    Specimen_ValMin = 99999
    Specimen_ValMax = -100
    Specimen_Values_First = []
    Specimen_Values_Selected = []

    Sel = Selection(FitnessFunction(),Selection.SelectionType_Top,SelLimitType,SelLimitVal,SelEvalMethod)
    for i in range(SpecimenAmount):
        SpecToAdd = Specimen()
        Specimen_ValMin = min(Specimen_ValMin,SpecToAdd.val)
        Specimen_ValMax = max(Specimen_ValMax,SpecToAdd.val)
        Specimen_Values_First += [SpecToAdd.val]
        SpecimensToBeSelected += [SpecToAdd]
    Specimen_Values_First.sort()

    SpecimensSelected = Sel.selection(SpecimensToBeSelected)
    for Spec in SpecimensSelected:
        Specimen_Values_Selected += [Spec.val]

    print("Added",SpecimenAmount,"Specimens",Specimen_Values_First)
    print("Selected",len(SpecimensSelected),"Specimens",Specimen_Values_Selected,100*len(Specimen_Values_Selected)/len(Specimen_Values_First))
    print()

    
    
    print("TEST ________ Selection Roulette ________________________________________________")
    SpecimensToBeSelected = []
    SpecimenAmount = random.randint(56,88)
    Specimen_ValMin = 99999
    Specimen_ValMax = -100
    Specimen_Values_First = []
    Specimen_Values_Selected = []

    Sel = Selection(FitnessFunction(),Selection.SelectionType_Roulette,SelLimitType,SelLimitVal,SelEvalMethod)
    for i in range(SpecimenAmount):
        SpecToAdd = Specimen()
        Specimen_ValMin = min(Specimen_ValMin,SpecToAdd.val)
        Specimen_ValMax = max(Specimen_ValMax,SpecToAdd.val)
        Specimen_Values_First += [SpecToAdd.val]
        SpecimensToBeSelected += [SpecToAdd]
    Specimen_Values_First.sort()

    SpecimensSelected = Sel.selection(SpecimensToBeSelected)
    for Spec in SpecimensSelected:
        Specimen_Values_Selected += [Spec.val]

    print("Added",SpecimenAmount,"Specimens",Specimen_Values_First)
    print("Selected",len(SpecimensSelected),"Specimens",Specimen_Values_Selected,100*len(Specimen_Values_Selected)/len(Specimen_Values_First))
    print()

    
    
    print("TEST ________ Selection Tournament ________________________________________________")
    SpecimensToBeSelected = []
    SpecimenAmount = random.randint(56,88)
    Specimen_ValMin = 99999
    Specimen_ValMax = -100
    Specimen_Values_First = []
    Specimen_Values_Selected = []

    Sel = Selection(FitnessFunction(),Selection.SelectionType_Tournament,SelLimitType,SelLimitVal,SelEvalMethod)
    for i in range(SpecimenAmount):
        SpecToAdd = Specimen()
        Specimen_ValMin = min(Specimen_ValMin,SpecToAdd.val)
        Specimen_ValMax = max(Specimen_ValMax,SpecToAdd.val)
        Specimen_Values_First += [SpecToAdd.val]
        SpecimensToBeSelected += [SpecToAdd]
    Specimen_Values_First.sort()

    SpecimensSelected = Sel.selection(SpecimensToBeSelected)
    for Spec in SpecimensSelected:
        Specimen_Values_Selected += [Spec.val]

    print("Added",SpecimenAmount,"Specimens",Specimen_Values_First)
    print("Selected",len(SpecimensSelected),"Specimens",Specimen_Values_Selected,100*len(Specimen_Values_Selected)/len(Specimen_Values_First))
    print()














