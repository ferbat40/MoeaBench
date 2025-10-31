from MoeaBench.CACHE import CACHE
from MoeaBench.UNSGA_pymoo import UNSGAPymoo


@staticmethod
def U_NSGA_III(problem, *, population = 100, generations = 300, seed = 1):
        result = CACHE()
        result .get_DATA_conf().set_DATA_MOEA(UNSGAPymoo(problem,population,generations,seed),problem)
        return result       

