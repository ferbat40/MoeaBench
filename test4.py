from MoeaBench import mb
import os, importlib
import numpy as np


os.system("cls")  





exp = mb.experiment()
exp.name = 'experiment 1'
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.MOEAD(generations = 10, population = 50)
exp.moea.generations=150
exp.moea.seed = 4
exp.name = "turicer"
exp.run()


hv  = mb.hypervolume(exp, generation = 100)   
print(hv)

gd  = mb.gd(exp, generation = 100)
print(gd)


gg = exp.GD(generations = [99,100])
print(gg)