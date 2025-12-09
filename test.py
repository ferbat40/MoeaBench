from MoeaBench import mb
import os, importlib
import numpy as np




os.system("cls")  


exp = mb.experiment()
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.NSGA3(generations = 100, population = 150)
exp.run()


exp2 = mb.experiment()
exp2.benchmark = mb.benchmarks.DTLZ1()
exp2.moea = mb.moeas.SPEA2(generations = 250, population = 300)
exp2.run()

ref = [exp,exp2]


mb.hypervolume.timeplot(exp2.result, generations = [100,200],  reference = ref)




#hy_arr_ref = mb.hypervolume.trace(exp, objectives = [1,3],  reference = ref)
#print(hy_arr_ref)


#hy_arr = mb.hypervolume.trace(exp, objectives = [1,3] )
#print(hy_arr)




#hv = mb.hypervolume(hy_arr_ref, generation = 90)
#print(hv)


#hv = mb.hypervolume(hy_arr, generation = 90)
#print(hv)


#hv_obj = mb.hypervolume(exp)
#print(hv_obj)