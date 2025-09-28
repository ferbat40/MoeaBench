
import os
from MoeaBench import MoeaBench

import numpy as np


os.system("cls")   
exp = MoeaBench()
exp.problem = exp.Benchmark.DTLZ1(K=10)
exp.moea = exp.Moea.NSGA3(problem=exp.problem, population = 140, generations = 300)
exp.RUN()






#for i in exp.problem.get_CACHE().get_elements():
    #print(i)
#for i in exp.moea:
    #print(i)





































