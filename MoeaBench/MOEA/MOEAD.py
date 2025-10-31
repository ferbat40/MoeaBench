from MoeaBench.CACHE import CACHE
from MoeaBench.MOEAD_pymoo import MOEADpymoo  


@staticmethod
def MOEAD(problem, *, population = 100, generations = 300, seed = 1):
        result = CACHE()
        result.get_DATA_conf().set_DATA_MOEA(MOEADpymoo(problem,population,generations,seed),problem)
        return result
                 