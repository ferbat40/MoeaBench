
import os
from MoeaBench import moeabench
import numpy as np
from MoeaBench.base_benchmark import BaseBenchmark
from IPython.display import  display
from MoeaBench.NSGA2deap import my_NSGA2deap
from MoeaBench.my_dtlz5 import my_dtlz5

os.system("cls")  

exp = moeabench.experiment()
exp.benchmark = moeabench.benchmarks.DTLZ5()
exp.moea = moeabench.moeas.NSGAIII()
exp.run()

#exp.save("gavan")




exp.moea.generations = 600
exp.moea.population = 260
exp.run()

#exp.save("sharivan")











































