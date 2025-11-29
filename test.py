
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
exp.moea = moeabench.moeas.NSGAIII(population = 150, generations = 300)
exp.run()

for i in exp.result.get_elements():
    for b in i[0].get_F_gen_non_dominate():
        print(b.shape)

dd = exp.hypervolume()
#print(dd)


#exp2 = moeabench.experiment()
#exp2.benchmark = moeabench.benchmarks.DPF1()
#exp2.moea = moeabench.moeas.RVEA(population = 100, generations = 101)
#exp2.run()

#moeabench.pareto(exp.result, exp2.result, generations = [30,50,70,100])
#print(exp2.result.get_elements()[0][0].get_arr_DATA().shape)
#print(exp2.result.get_elements()[0][0].get_F_GEN()[-1].shape)
#exp2.hypervolume()
#arr1 = exp.objective()[0]

#arr2 = exp2.objective()[0]

#stat = moeabench.stat()
#stat.indice = moeabench.indice(arr1)






















































