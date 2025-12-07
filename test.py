from MoeaBench import mb
import os
import numpy as np



os.system("cls")  


exp = mb.experiment()
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.NSGA3(generations = 400, population = 190)
exp.run()

set = exp.set(generations = [10])

sum_set = set
print(set)

var = exp.variables(generations = [10])


sum_var = var
#print(sum_var)


#print(obj[1])


#var = exp.variables(generations = [5])
#print(var)

