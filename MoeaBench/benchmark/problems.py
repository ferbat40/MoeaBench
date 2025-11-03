from .I_problems import I_problems
from MoeaBench import benchmark
from typing import TYPE_CHECKING
if TYPE_CHECKING: from problem_benchmark import P_DTLZ1,P_DTLZ2,P_DTLZ3,P_DTLZ4,P_DTLZ5,P_DTLZ6,P_DTLZ7,P_DTLZ8,P_DTLZ9,P_DPF1,P_DPF2,P_DPF3,P_DPF4,P_DPF5
if TYPE_CHECKING: from MoeaBench.CACHE import CACHE
if TYPE_CHECKING: from MoeaBench.CACHE_bk_user import CACHE_bk_user


class problems(I_problems):

    def __init__(self,name):
        self.__memory=benchmark.CACHE()
        self.__memory_user=benchmark.CACHE_bk_user()
        self.__name = name
    

    def DPF1(self, M, K, P, D):
        return benchmark.P_DPF1(M, K, D, P, self.get_CACHE())


    def DPF2(self, M, K, P, D):
        return benchmark.P_DPF2(M, K, D, P, self.get_CACHE())


    def DPF3(self, M, K, P, D):
        return benchmark.P_DPF3(M, K, D, P, self.get_CACHE())


    def DPF4(self, M, K, P, D):
        return benchmark.P_DPF4(M, K, D, P, self.get_CACHE())


    def DPF5(self, M, K, P, D):
        return benchmark.P_DPF5(M, K, D, P, self.get_CACHE())

    
    def DTLZ1(self, M, K, P, D):
        return benchmark.P_DTLZ1(M, K, P, self.get_CACHE())

    
    def DTLZ2(self, M, K, P, D):
        return benchmark.P_DTLZ2(M, K, P, self.get_CACHE())


    def DTLZ3(self, M, K, P, D):
        return benchmark.P_DTLZ3(M, K, P, self.get_CACHE())


    def DTLZ4(self, M, K, P, D):
        return benchmark.P_DTLZ4(M, K, P, self.get_CACHE())


    def DTLZ5(self, M, K, P, D):
        return benchmark.P_DTLZ5(M, K, P, self.get_CACHE())


    def DTLZ6(self, M, K, P, D):
        return benchmark.P_DTLZ6(M, K, P, self.get_CACHE())


    def DTLZ7(self, M, K, P, D):
        return benchmark.P_DTLZ7(M, K, P, self.get_CACHE())


    def DTLZ8(self, M, K, P, D):
        return benchmark.P_DTLZ8(M , K , P, self.get_CACHE())


    def DTLZ9(self, M, K, P, D):
        return benchmark.P_DTLZ9(M, K, P, self.get_CACHE())


    def dict_data(self):
        return {benchmark.E_problems.DPF1 : self.DPF1,
                benchmark.E_problems.DPF2 : self.DPF2,
                benchmark.E_problems.DPF3 : self.DPF3,
                benchmark.E_problems.DPF4 : self.DPF4,
                benchmark.E_problems.DPF5 : self.DPF5,
                benchmark.E_problems.DTLZ1 : self.DTLZ1,
                benchmark.E_problems.DTLZ2 : self.DTLZ2,
                benchmark.E_problems.DTLZ3 : self.DTLZ3,
                benchmark.E_problems.DTLZ4 : self.DTLZ4,
                benchmark.E_problems.DTLZ5 : self.DTLZ5,
                benchmark.E_problems.DTLZ6 : self.DTLZ6,
                benchmark.E_problems.DTLZ7 : self.DTLZ7,
                benchmark.E_problems.DTLZ8 : self.DTLZ8,
                benchmark.E_problems.DTLZ9 : self.DTLZ9,
                }


    def get_CACHE(self):
        return self.__memory
    

    def get_CACHE_USER(self):
        return self.__memory_user
    

    def get_problem(self,M = None, K = None, P = None, D = None):
        problem = [problem for problem in list(benchmark.E_problems) if problem.name == self.__name][0]
        return self.dict_data()[problem](M, K, P, D)

