
import os
from MoeaBench import moeabench
from MoeaBench.base_moea import BaseMoea
import sys
from  MoeaBench.CACHE_bk_user import CACHE_bk_user
#sys.modules['__main__'].my_dtlz7 = my_dtlz7




import numpy as np


os.system("cls")  
exp  = moeabench()
exp.problem = exp.benchmark.my_implemented_benchmark(my_dtlz7(CACHE_bk_user()))
    

exp.moea = moeabench.Moea.MOEAD(problem=exp.problem, population = 130, generations = 400)
exp.run()

exp.save('sharivan')
exp.load('sharivan')









































































