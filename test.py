
import os
from MoeaBench import moeabench

import numpy as np


os.system("cls")  


exp  = moeabench()
exp2 = moeabench()
exp.problem = moeabench.benchmark.DTLZ1()
exp2.problem = moeabench.benchmark.DTLZ1()
exp.moea = moeabench.Moea.U_NSGA3(problem=exp.problem, population = 140, generations = 300)
exp2.moea = moeabench.Moea.NSGA3(problem=exp.problem, population = 140, generations = 300)

print(exp.problem==exp2.problem,exp.moea==exp2.moea,exp==exp2 )


#exp.problem = moeabench.benchmark.DTLZ1()
#exp.moea = moeabench.Moea.U_NSGA3(problem=exp.problem, population = 140, generations = 300)
#exp2.moea = moeabench.Moea.NSGA3(problem=exp.problem, population = 140, generations = 300)
#exp.RUN()

#print(exp.moea,exp2.moea)
#resul=exp.result.get_elements()
#pof=exp.pof.get_elements()
#pof = exp.pof
#result = exp.result
#HV = exp.hypervolume(100)
#GD = exp.GD(100)
#GDplus =exp.GDplus(100)
#IGD = exp.IGD(100)
#IGDplus = exp.IGDplus(100)
#objectives = exp.objectives(3,90)
#print(exp.IGD(),"exp")


























































