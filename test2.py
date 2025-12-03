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
exp.moea = moeabench.moeas.my_NSGA2deap()
exp.run()
exp.save("gavan")




exp.moea.generations = 600
exp.moea.population = 260
exp.run()

exp.save("sharivan")


#exp2 = moeabench.experiment()
#exp2.load("sharivan")
#hv = exp2.hypervolume()
#print(hv)