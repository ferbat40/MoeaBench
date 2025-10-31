from MoeaBench.CACHE import CACHE
from MoeaBench.RVEA_pymoo  import RVEApymoo
    

@staticmethod
def RVEA(problem, *, population = 100, generations = 300, seed = 1):
        result = CACHE()
        result.get_DATA_conf().set_DATA_MOEA(RVEApymoo(problem,population,generations,seed),problem)
        return result