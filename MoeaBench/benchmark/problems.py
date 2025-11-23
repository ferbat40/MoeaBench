from .I_problems import I_problems
from MoeaBench import benchmark
from typing import TYPE_CHECKING
if TYPE_CHECKING: from problem_benchmark import P_DTLZ1,P_DTLZ2,P_DTLZ3,P_DTLZ4,P_DTLZ5,P_DTLZ6,P_DTLZ7,P_DTLZ8,P_DTLZ9,P_DPF1,P_DPF2,P_DPF3,P_DPF4,P_DPF5
if TYPE_CHECKING: from MoeaBench.CACHE import CACHE
if TYPE_CHECKING: from MoeaBench.CACHE_bk_user import CACHE_bk_user


class problems(I_problems):

    def __init__(self):
        self.__memory=benchmark.CACHE()
        self.__memory_user=benchmark.CACHE_bk_user()
    

    def DPF1(self):
        return benchmark.problem_benchmark.P_DPF1,benchmark.E_problems_bk.P_DPF1


    def DPF2(self):
        return benchmark.problem_benchmark.P_DPF2,benchmark.E_problems_bk.P_DPF2


    def DPF3(self):
        return benchmark.problem_benchmark.P_DPF3,benchmark.E_problems_bk.P_DPF3


    def DPF4(self):
        return benchmark.problem_benchmark.P_DPF4,benchmark.E_problems_bk.P_DPF4


    def DPF5(self):
        return benchmark.problem_benchmark.P_DPF5,benchmark.E_problems_bk.P_DPF5

    
    def DTLZ1(self):
        return benchmark.problem_benchmark.P_DTLZ1,benchmark.E_problems_bk.P_DTLZ1

    
    def DTLZ2(self):
        return benchmark.problem_benchmark.P_DTLZ2,benchmark.E_problems_bk.P_DTLZ2


    def DTLZ3(self):
        return benchmark.problem_benchmark.P_DTLZ3,benchmark.E_problems_bk.P_DTLZ3


    def DTLZ4(self):
        return benchmark.problem_benchmark.P_DTLZ4,benchmark.E_problems_bk.P_DTLZ4


    def DTLZ5(self):
        return benchmark.problem_benchmark.P_DTLZ5,benchmark.E_problems_bk.P_DTLZ5


    def DTLZ6(self):
        return benchmark.problem_benchmark.P_DTLZ6,benchmark.E_problems_bk.P_DTLZ6


    def DTLZ7(self):
        return benchmark.problem_benchmark.P_DTLZ7,benchmark.E_problems_bk.P_DTLZ7


    def DTLZ8(self):
        return benchmark.problem_benchmark.P_DTLZ8,benchmark.E_problems_bk.P_DTLZ8


    def DTLZ9(self):
        return benchmark.problem_benchmark.P_DTLZ9,benchmark.E_problems_bk.P_DTLZ9
    

    def my_new_benchmark(self):
        return benchmark.my_new_benchmark,benchmark.my_new_benchmark.__name__


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
                benchmark.E_problems.my_new_benchmark: self.my_new_benchmark
                }


    def get_CACHE(self):
        return self.__memory
    

    def get_CACHE_USER(self):
        return self.__memory_user
    

    def get_problem(self, name):
        problem = [problem for problem in list(benchmark.E_problems) if problem.name == name]
        return self.dict_data()[problem[0]]() if len(problem) > 0  else False

