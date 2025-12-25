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


exp2 = mb.experiment()
exp2.benchmark = mb.benchmarks.DTLZ1()
exp2.moea = mb.moeas.NSGA3(generations = 10, population = 100)
exp2.moea.generations=300
exp2.run(repeat = 10)


nd = exp2.round[0].front
pop = exp2.round[0].objectives


pr = mb.stats.paretorank(exp2)
print(pr.rank())