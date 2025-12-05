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
exp.benchmark = moeabench.benchmarks.my_dtlz5()
#print(exp.moea.creator)
exp.moea = moeabench.moeas.my_NSGA2deap()

exp.run()
exp.save("jaspion")

exp.benchmark.M=4


exp.benchmark.K=15


exp.benchmark.P=2000

exp.benchmark.D=3


exp.moea.population = 180
exp.moea.generations = 320
exp.run()


#print("exp.benchmark.P ",exp.benchmark.P)#exp.run()
exp.save("gavan")

exp4  = moeabench.experiment()
exp4.load("gavan")

df = exp4.hypervolume()
print(df)