from MoeaBench.base_benchmark import BaseBenchmark
from enum import Enum
import numpy as np
import os
from MoeaBench import moeabench
from MoeaBench.my_dtlz5 import my_dtlz5
from MoeaBench.NSGA2deap import my_NSGA2deap



os.system("cls")  



moeabench.add_benchmark(my_dtlz5)
moeabench.add_moea(my_NSGA2deap)


exp = moeabench.experiment()
#exp.benchmark = moeabench.benchmarks.my_dtlz5(M = 3, D = 2, P = 1000, K = 5)
#exp.moea = moeabench.moeas.my_NSGA2deap(generations =100 , population = 100)

exp.benchmark = moeabench.benchmarks.DPF5()
exp.moea = moeabench.moeas.NSGAIII()
exp.run()
exp.save("DPF5")

exp.benchmark.M=4
#print(exp.benchmark.M)


exp.benchmark.K=15


exp.benchmark.P=2000


exp.benchmark.D=3


exp.moea.population = 200
exp.moea.generations = 400
exp.run()


exp.save("DPF5_up")

#exp4  = moeabench.experiment()
#exp4.load("gavan")

#df = exp4.hypervolume()
#print(df)