from MoeaBench import mb
import os
import numpy as np



os.system("cls")  


exp = mb.experiment()
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.NSGA3(generations = 400, population = 100)
exp.run()
#print(exp.dominated.objectives())


