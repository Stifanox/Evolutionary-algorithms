import random
from abc import ABC, abstractmethod
from typing import *

from Core.RealRepresentation.ChromosomeReal import ChromosomeReal
from Core.RealRepresentation.SpecimenReal import SpecimenReal


class CrossoverTypeReal(ABC):
    """
    Classes inheriting from this class represent a single method of crossover.
    """

    @abstractmethod
    def mix(self, a: SpecimenReal, b: SpecimenReal, *args) -> Union[Tuple[SpecimenReal], Tuple[SpecimenReal, SpecimenReal]]:
        """
        Generates at least one child from two parents or a single parent.
        For crossover methods that take 1 parent, parameters other than the first one are ignored, and they return a single child.
        For crossover methods that take 2 parents, they return a tuple of two children or a single child.
        For crossover methods that take more than 2 parents, they return a single child.
        :param a: SpecimenReal ; Parent A.
        :param b: SpecimenReal ; Parent B. If the method takes only one parent, this argument is ignored.
        :param args: SpecimenReal ; Additional parents. If the method takes only one or two parents, this argument is ignored.
        :return: Tuple of two, newly generated specimens or a tuple with one specimen.
        """
        pass

    @staticmethod
    def _mix(a: SpecimenReal, b: SpecimenReal) -> Tuple[float, float, float, float, Tuple[float, float], Tuple[float, float]]:
        """
        Helper method for mix() method. It extracts chromosomes from two parents and checks if they have the same domain.
        :param a: SpecimenReal ; Parent A.
        :param b: SpecimenReal ; Parent B.
        :return: Tuple of: 4 chromosomes values x1,y1 for "a", x2,y2 for "b", and 2 tuples of their domains x and y.
        :raises RuntimeError: if specimen a have different domains than b.
        """
        x1 = a.getChromosomes()[0]
        y1 = a.getChromosomes()[1]
        x2 = b.getChromosomes()[0]
        y2 = b.getChromosomes()[1]

        # try:
        #     new_domain_x = ChromosomeReal.calculateFunctionsDomainsIntersection(x1, x2)
        #     new_domain_y = ChromosomeReal.calculateFunctionsDomainsIntersection(y1, y2)
        # except ValueError as e:  # if domains do not intersect
        #     raise RuntimeError(str(e))  # rethrows ValueError as RuntimeError, IDK how to handle it, so I just try to kill the program

        # x1 and x2 have the same domain; y1 and y2 also have the same domain

        if x1.getFunctionDomain() != x2.getFunctionDomain() or y1.getFunctionDomain() != y2.getFunctionDomain():
            raise RuntimeError("specimens have different domains")
        return float(x1), float(y1), float(x2), float(y2), x1.getFunctionDomain(), y1.getFunctionDomain()


class ArithmeticCrossover(CrossoverTypeReal):
    """
    Implements arithmetic crossover.
    """

    def __init__(self, k: float):
        """
        :param k : float ; in the range (0;1), it can be constant, set at the time of object creation or can be changed between calls of mix() method for every pair of parents.
            It can be generated based on the number of iterations of the algorithm. It's up to the user to decide how to generate it. The number is validated.
        :raises ValueError: if k is not in the range (0;1)
        """
        self.k = k

    @property
    def k(self):
        """
        k parameter getter.
        :return: k parameter.
        """
        return self._k

    @k.setter
    def k(self, k: float):
        """
        k parameter setter.
        :param k: in the range (0;1)
        :raises ValueError: if k is not in the range (0;1)
        """
        if not 0 < k < 1:
            raise ValueError("k must be in range (0;1)")
        self._k = k

    def mix(self, a: SpecimenReal, b: SpecimenReal, *args) -> Tuple[SpecimenReal, SpecimenReal]:
        """
        Generates two children from two parents.
        :param a : Specimen ; Parent A.
        :param b : Specimen ; Parent B.
        :param args :  ignored
        :return: Tuple of two, newly generated specimens with chromosomes in domains of parents (parents have the same domain).
        """
        x1, y1, x2, y2, domain_x, domain_y = super()._mix(a, b)

        x1_new = self.k * x1 + (1 - self.k) * x2
        y1_new = self.k * y1 + (1 - self.k) * y2

        x2_new = (1 - self.k) * x1 + self.k * x2
        y2_new = (1 - self.k) * y1 + self.k * y2

        # I am 99% sure, that the new chromosomes will be in the ranges specified by new_domain_x and new_domain_y, but just to be sure
        # I will clamp them to the domain, because it is allowed by the task and I don't want to throw an exception here.
        # (But really I just don't want to mathematically prove that the new chromosomes will be in the specified domains :p)
        x1_new = ChromosomeReal.clampNumberToDomain(x1_new, domain_x)
        y1_new = ChromosomeReal.clampNumberToDomain(y1_new, domain_y)

        x2_new = ChromosomeReal.clampNumberToDomain(x2_new, domain_x)
        y2_new = ChromosomeReal.clampNumberToDomain(y2_new, domain_y)

        first_child = SpecimenReal([ChromosomeReal(x1_new, domain_x), ChromosomeReal(y1_new, domain_y)], 2)
        second_child = SpecimenReal([ChromosomeReal(x2_new, domain_x), ChromosomeReal(y2_new, domain_y)], 2)
        return first_child, second_child


class BlendCrossoverAlfa(CrossoverTypeReal):
    """
    Implements blend crossover alfa (BLX-alfa).
    """

    def __init__(self, alfa: float):
        """
        :param alfa : float ; it would be best for it to be in the range (0;1), it can be constant, set at the time of object creation or can be changed
            between calls of mix() method for every pair of parents. It can be generated based on the number of
            iterations of the algorithm. It's up to the user to decide how to generate it. This number isn't validated.
        """
        self.alfa = alfa

    @property
    def alfa(self):
        """
        alfa parameter getter.
        :return: alfa parameter.
        """
        return self._alfa

    @alfa.setter
    def alfa(self, alfa: float):
        """
        alfa parameter setter.
        :param alfa: float ; in the range (0;1)
        """
        self._alfa = alfa

    def mix(self, a: SpecimenReal, b: SpecimenReal, *arg) -> Tuple[SpecimenReal, SpecimenReal]:
        """
        Generates two children from two parents.
        :param a : Specimen ; Parent A.
        :param b : Specimen ; Parent B.
        :param arg :  ignored
        :return: Tuple of two, newly generated specimens with chromosomes in domains of parents (parents have the same domain).
        """
        x1, y1, x2, y2, domain_x, domain_y = super()._mix(a, b)

        alfa_delta_x = self.alfa * (domain_x[1] - domain_x[0])
        alfa_delta_y = self.alfa * (domain_y[1] - domain_y[0])

        new_domain_x = (min(x1, x2) - alfa_delta_x, max(x1, x2) + alfa_delta_x)
        new_domain_y = (min(y1, y2) - alfa_delta_y, max(y1, y2) + alfa_delta_y)  # w prezce jest max(y1,xy) ale chyba powinno byc max(y1,y2)

        new_domain_x = ChromosomeReal.calculateFunctionsDomainsIntersection(new_domain_x, domain_x)
        new_domain_y = ChromosomeReal.calculateFunctionsDomainsIntersection(new_domain_y, domain_y)

        x1_new = random.uniform(*new_domain_x)
        y1_new = random.uniform(*new_domain_y)
        x2_new = random.uniform(*new_domain_x)
        y2_new = random.uniform(*new_domain_y)

        first_child = SpecimenReal([ChromosomeReal(x1_new, domain_x), ChromosomeReal(y1_new, domain_y)], 2)
        second_child = SpecimenReal([ChromosomeReal(x2_new, domain_x), ChromosomeReal(y2_new, domain_y)], 2)

        return first_child, second_child


class BlendCrossoverAlfaBeta(CrossoverTypeReal):
    """
    Implements blend crossover alfa beta (BLX-alfa-beta).
    """

    def __init__(self, alfa: float, beta: float):
        """
        :param alfa: it would be best for it to be in the range (0;1), it can be constant, set at the time of object creation or can be changed
            between calls of mix() method for every pair of parents. It can be generated based on the number of
            iterations of the algorithm. It's up to the user to decide how to generate it. This number isn't validated.
        :param beta: it would be best for it to be in the range (0;1), it can be constant, set at the time of object creation or can be changed
             between calls of mix() method for every pair of parents. It can be generated based on the number of
            iterations of the algorithm. It's up to the user to decide how to generate it. This number isn't validated.
        """
        self.alfa = alfa
        self.beta = beta

    @property
    def alfa(self):
        """
        alfa parameter getter.
        :return: alfa parameter.
        """
        return self._alfa

    @alfa.setter
    def alfa(self, alfa: float):
        """
        alfa parameter setter.
        :param alfa: float ; in the range (0;1)
        """
        self._alfa = alfa

    @property
    def beta(self):
        """
        beta parameter getter.
        :return: beta parameter.
        """
        return self._beta

    @beta.setter
    def beta(self, beta: float):
        """
          beta parameter setter.
          :param beta: float ; in the range (0;1)
        """
        self._beta = beta

    def mix(self, a: SpecimenReal, b: SpecimenReal, *arg) -> Tuple[SpecimenReal, SpecimenReal]:
        """
        Generates two children from two parents.
        :param a : Specimen ; Parent A.
        :param b : Specimen ; Parent B.
        :param arg :  ignored
        :return:  Tuple of two, newly generated specimens with chromosomes in domains of parents (parents have the same domain).
        """
        x1, y1, x2, y2, domain_x, domain_y = super()._mix(a, b)

        delta_x = (domain_x[1] - domain_x[0])
        delta_y = (domain_y[1] - domain_y[0])

        new_domain_x = (min(x1, x2) - self.alfa * delta_x, max(x1, x2) + self.beta * delta_x)
        new_domain_y = (min(y1, y2) - self.alfa * delta_y, max(y1, y2) + self.beta * delta_y)  # w prezce jest max(y1,xy) ale chyba powinno byc max(y1,y2)

        new_domain_x = ChromosomeReal.calculateFunctionsDomainsIntersection(new_domain_x, domain_x)
        new_domain_y = ChromosomeReal.calculateFunctionsDomainsIntersection(new_domain_y, domain_y)

        x1_new = random.uniform(*new_domain_x)
        y1_new = random.uniform(*new_domain_y)
        x2_new = random.uniform(*new_domain_x)
        y2_new = random.uniform(*new_domain_y)

        first_child = SpecimenReal([ChromosomeReal(x1_new, domain_x), ChromosomeReal(y1_new, domain_y)], 2)
        second_child = SpecimenReal([ChromosomeReal(x2_new, domain_x), ChromosomeReal(y2_new, domain_y)], 2)

        return first_child, second_child


class AverageCrossover(CrossoverTypeReal):
    """
    Implements average crossover.
    """

    def __init__(self):
        pass

    def mix(self, a: SpecimenReal, b: SpecimenReal, *arg) -> Tuple[SpecimenReal]:
        """
        Generates child from at least 2 parents.
        :param a : Specimen ; Parent A.
        :param b : Specimen ; Parent B.
        :param arg :  Specimen ; Additional parents.
        :return: Tuple of one, newly generated specimen with chromosomes in domains of parents (parents have the same domain).
        """
        specimens = [a, b, *arg]
        avg_x = sum(float(x.getChromosomes()[0]) for x in specimens) / len(specimens)
        avg_y = sum(float(x.getChromosomes()[1]) for x in specimens) / len(specimens)

        domain_x = specimens[0].getChromosomes()[0].getFunctionDomain()
        domain_y = specimens[0].getChromosomes()[1].getFunctionDomain()

        child = SpecimenReal([ChromosomeReal(avg_x, domain_x), ChromosomeReal(avg_y, domain_y)], 2)

        return (child,)


class FlatCrossover(CrossoverTypeReal):
    """
    Implements flat crossover.
    """

    def __init__(self):
        pass

    def mix(self, a: SpecimenReal, b: SpecimenReal, *args) -> Tuple[SpecimenReal]:
        """
        Generates one child from two parents.
        :param a : Specimen ; Parent A.
        :param b : Specimen ; Parent B.
        :param args :  ignored
        :return: Tuple of one, newly generated specimen with chromosomes in domains of parents (parents have the same domain).
        """

        x1, y1, x2, y2, domain_x, domain_y = super().mix(a, b)

        new_domain_x = sorted([x1, x2])
        new_domain_y = sorted([y1, y2])

        x1_new = random.uniform(*new_domain_x)
        y1_new = random.uniform(*new_domain_y)

        child = SpecimenReal([ChromosomeReal(x1_new, domain_x), ChromosomeReal(y1_new, domain_y)], 2)

        return (child,)


class LinearCrossover(CrossoverTypeReal):
    """
    Implements linear crossover.
    """

    def __init__(self, fitness_function: Callable[[SpecimenReal], float], maximize: bool):
        """
        :param fitness_function: Callable[[SpecimenReal], float] ; Fitness function to select 2 best children from 3 generated children.
        :param maximize: bool ; If True, the higher value of fitness function is better, if False, the lower value of fitness function is better.
        """
        self.fitness_function = fitness_function
        self.maximize = maximize
        pass

    def mix(self, a: SpecimenReal, b: SpecimenReal, *args) -> Tuple[SpecimenReal, SpecimenReal]:
        """
        Generates two children from two parents.
        :param a : Specimen ; Parent A.
        :param b : Specimen ; Parent B.
        :param args :  ignored
        :return: Tuple of one, newly generated specimen with chromosomes in domains of parents (parents have the same domain).
        """
        x1, y1, x2, y2, domain_x, domain_y = super().mix(a, b)

        z = ((1 / 2) * x1 + (1 / 2) * x2, (1 / 2) * y1 + (1 / 2) * y2)
        v = ((3 / 2) * x1 - (1 / 2) * x2, (3 / 2) * y1 - (1 / 2) * y2)
        w = (-(1 / 2) * x1 + (3 / 2) * x2, -(1 / 2) * y1 + (3 / 2) * y2)

        # TODO: check if it is necessary to clamp z,v and v to the domain or not

        z = SpecimenReal([ChromosomeReal(z[0], domain_x), ChromosomeReal(z[1], domain_y)], 2)
        v = SpecimenReal([ChromosomeReal(v[0], domain_x), ChromosomeReal(v[1], domain_y)], 2)
        w = SpecimenReal([ChromosomeReal(w[0], domain_x), ChromosomeReal(w[1], domain_y)], 2)

        z.setSpecimenValue(self.fitness_function(z))
        v.setSpecimenValue(self.fitness_function(v))
        w.setSpecimenValue(self.fitness_function(w))

        specimens = [z, v, w]

        specimens = sorted(specimens, key=lambda x: x.getSpecimenValue())
        if self.maximize:
            return specimens[1], specimens[2]
        else:
            return specimens[0], specimens[1]
