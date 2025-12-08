from MoeaBench import mb
import os, importlib
import numpy as np




os.system("cls")  


exp = mb.experiment()
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.NSGA3(generations = 300, population = 200)
exp.run()


hv = mb.hypervolume(exp)
print(hv)

hy_arr = mb.hypervolume.trace(exp, generations = [200,250])
print(hy_arr)



