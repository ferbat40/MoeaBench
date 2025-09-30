
import os
from MoeaBench import moeabench

import numpy as np


os.system("cls")  


exp  = moeabench()
exp2 = moeabench()
exp.problem = moeabench.benchmark.DTLZ1()
exp2.problem = moeabench.benchmark.DTLZ1(M = 4)
exp.moea = moeabench.Moea.NSGA3(problem=exp.problem, population = 140, generations = 300)
exp2.moea = moeabench.Moea.U_NSGA3(problem=exp2.problem, population = 140, generations = 300)
exp.RUN()

exp2.RUN()




HV = exp.hypervolume(100)
GD = exp.GD(100)
GDplus =exp.GDplus(100)
IGD = exp.IGD(100)
IGDplus = exp.IGDplus(100)
objectives = exp.objectives(3,90)





HV = exp2.hypervolume(100)
GD = exp2.GD(100)
GDplus =exp2.GDplus(100)
IGD = exp2.IGD(100)
IGDplus = exp2.IGDplus(100)
objectives = exp.objectives(3,3)



moeabench.plot_hypervolume(exp, exp2, generations = 180)


































































