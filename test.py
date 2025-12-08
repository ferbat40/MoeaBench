from MoeaBench import mb
import os, importlib
import numpy as np




os.system("cls")  


exp = mb.experiment()
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.NSGA3(generations = 400, population = 150)
exp.run()


exp2 = mb.experiment()
exp2.benchmark = mb.benchmarks.DTLZ1()
exp2.moea = mb.moeas.SPEA2(generations = 250, population = 300)
exp2.run()



mb.hypervolume.timeplot(generations = [100,200])


#ref = [exp,exp2]

#hy_arr_ref = mb.hypervolume.trace(exp, objectives = [1,3],  reference = ref)
#print(hy_arr_ref)


#hy_arr = mb.hypervolume.trace(exp, objectives = [1,3] )
#print(hy_arr)




#hv = mb.hypervolume(hy_arr_ref, generation = 399)
#print(hv)


#hv = mb.hypervolume(hy_arr, generation = 399)
#print(hv)


#hv_obj = mb.hypervolume(exp)
#print(hv_obj)