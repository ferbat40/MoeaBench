
import os
from MoeaBench import moeabench
import numpy as np
from MoeaBench.base_benchmark import BaseBenchmark
from IPython.display import  display
from MoeaBench.NSGA2deap import my_NSGA2deap
from MoeaBench.my_dtlz5 import my_dtlz5

os.system("cls")  

moeabench.add_benchmark(my_dtlz5)
moeabench.add_moea(my_NSGA2deap)


exp = moeabench.experiment()
exp.benchmark = moeabench.benchmarks.DTLZ1()


exp.moea = moeabench.moeas.U_NSGAIII()
exp.run()

exp.save("caba")

exp.moea.generations = 400
exp.moea.population = 250
exp.run()

exp.save("robotec")


#experiment_user = moeabench.experiment()
#experiment_user.benchmark = moeabench.benchmarks.my_dtlz5()
#experiment_user.moea = moeabench.moeas.my_NSGA2deap()
#experiment_user.run()


















































