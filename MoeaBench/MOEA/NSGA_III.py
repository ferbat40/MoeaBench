from MoeaBench.CACHE import CACHE
from MoeaBench.NSGA_pymoo import NSGAPymoo


@staticmethod
def NSGA_III(problem, *, population = 100, generations = 300, seed = 1):
        result = CACHE()
        result.get_DATA_conf().set_DATA_MOEA(NSGAPymoo(problem,population,generations,seed),problem)
        return result     
