
import os
from MoeaBench import moeabench
#from MoeaBench.NSGA2deap import my_NSGA2deap
#from MoeaBench.my_dtlz5 import my_dtlz5
import numpy as np
from MoeaBench.base_benchmark import BaseBenchmark
from IPython.display import  display

os.system("cls")  

exp = moeabench.experiment()
exp.benchmark = moeabench.benchmarks.DTLZ1(M = 3)
exp.moea = moeabench.moeas.NSGAIII(population = 100, generations = 200)
exp.run()




exp2 = moeabench.experiment()
exp2.benchmark = moeabench.benchmarks.DTLZ8()
exp2.moea = moeabench.moeas.SPEAII(population = 100, generations = 200)
exp2.run()

moeabench.pareto(exp.result, exp2.result, generations = [30,50,70,100])

#arr1 = exp.objective()[0]

#arr2 = exp2.objective()[0]

#stat = moeabench.stat()
#stat.indice = moeabench.indice(arr1)






















































