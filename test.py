
import os
from MoeaBench import moeabench
import numpy as np
from MoeaBench.base_benchmark import BaseBenchmark
from IPython.display import  display
from MoeaBench.NSGA2deap import my_NSGA2deap
from MoeaBench.my_dtlz5 import my_dtlz5

os.system("cls")  

experiment_user = moeabench.experiment()
experiment_user.benchmark = moeabench.benchmarks.DTLZ5()
experiment_user.moea = moeabench.moeas.NSGAIII()
experiment_user.run()

experiment_user.moea.population = 260


experiment_user.run()











































