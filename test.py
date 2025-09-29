
import os
from MoeaBench import moeabench

import numpy as np


os.system("cls")   
exp = moeabench
exp.problem = moeabench.benchmark.DTLZ1()
print(exp.problem.CACHE)


exp.moea = moeabench.Moea.NSGA3(problem=exp.problem, population = 140, generations = 300)
exp.RUN()
print(exp.moea,"caba",exp)
#print("hv",exp.hypervolume(100))
#print("gd",exp.GD(100))
#print("gdplus",exp.GDplus(100))
#print("IGD",exp.IGD(100))
#print("IGDplus",exp.IGDplus(100))
#obj = exp.objectives(3,90)
#for i in obj:
   # print(i)






#for i in exp.problem.get_CACHE().get_elements():
    #print(i)
#for i in exp.moea:
    #print(i)





































