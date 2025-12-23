from MoeaBench import mb
import os, importlib
import numpy as np


os.system("cls")  


exp = mb.experiment()
exp.name = 'experiment 1'
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.MOEAD(generations = 10, population = 150)
exp.moea.generations=150
exp.moea.seed = 4
exp.run()


exp2 = mb.experiment()
exp2.name = 'experiment 2'
exp2.benchmark = mb.benchmarks.DTLZ1()
exp2.moea = mb.moeas.NSGA3(generations = 10, population = 150)
exp2.moea.generations=300
exp2.run()

ref = [exp, exp2]


hv_100  = mb.hypervolume(exp, generation=100, reference = ref) 
print(hv_100)


ht = mb.hypervolume.trace(exp, reference = ref)
print(ht)

mb.hypervolume.timeplot(exp, exp2)