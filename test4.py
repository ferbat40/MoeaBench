from MoeaBench import mb
import os, importlib
import numpy as np


os.system("cls")  


exp2 = mb.experiment()
exp2.name = 'experiment 1'
exp2.benchmark = mb.benchmarks.DTLZ5(M = 3)
exp2.moea = mb.moeas.NSGA3(population=150, generations=300)
exp2.run()


#var = exp.variables(generation = 1)
#print(var.shape)

#ar_r = exp.variables.round(1)
#print(var_r.shape)
#set = exp.set(generation = 89)
print(exp2.set())



#var = exp.dominated.variables(generation = 89)
#@print(var.shape)


#for i in range(0,4):
  #obj_r = exp.set.round(i)
 # print(obj_r.shape)


#print(exp.rounds[1].variables)