from MoeaBench.CACHE import CACHE
from MoeaBench.SPEA_pymoo import SPEAPymoo


@staticmethod
def SPEA_II(problem, *, population = 100, generations = 300, seed = 1):
        result = CACHE()
        result.get_DATA_conf().set_DATA_MOEA(SPEAPymoo(problem,population,generations,seed),problem)
        return result      