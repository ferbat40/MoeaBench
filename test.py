from MoeaBench import mb
import os, importlib
import numpy as np




os.system("cls")  


exp = mb.experiment()
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.NSGA3(generations = 300, population = 160)
exp.run()


exp2 = mb.experiment()
exp2.benchmark = mb.benchmarks.DTLZ1()
exp2.moea = mb.moeas.NSGA3(generations = 300, population = 160)
exp2.run()


ref = [exp, exp2]

hy_arr = mb.hypervolume.trace(exp, objectives = [1,3], reference = ref)
print(hy_arr)


hv = mb.hypervolume(hy_arr, generation = 1000)
#print(hv)


#hv_obj = mb.hypervolume(exp)
#print(hv_obj)