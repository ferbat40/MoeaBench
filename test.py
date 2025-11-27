
import os
from MoeaBench import moeabench
#from MoeaBench.NSGA2deap import my_NSGA2deap
#from MoeaBench.my_dtlz5 import my_dtlz5
import numpy as np
from MoeaBench.base_benchmark import BaseBenchmark
from IPython.display import  display

os.system("cls")  

exp = moeabench()
stat = moeabench()



#exp.add_benchmark(my_dtlz5)
#exp.add_moea(my_NSGA2deap)


#exp.benchmark = moeabench.benchmark.my_dtlz5()
#exp.moea = moeabench.moea.my_NSGA2deap()
#exp.run()
#exp.save("savage")


exp = moeabench()
exp.benchmark = moeabench.benchmarks.DTLZ8()
exp.moea = moeabench.moeas.MOEAD()
exp.run()

exp2 = moeabench()
exp2.benchmark = moeabench.benchmarks.DTLZ8()
exp2.moea = moeabench.moeas.SPEAII()
exp2.run()


stat = moeabench()

stat.kstest = moeabench.stat.kstest(exp.objective(), exp2.objective())
display(stat.kstest)


stat.indice = moeabench.stat.indice(exp.objective(), exp2.objective())
display(stat.indice)

#moeabench.stats.kstest(exp2.objective(objective = 3), exp.objective(objective = 3))
#moeabench.stats.indices(exp2.objective(), exp.objective())
#hv = exp.hypervolume()
#print(hv)



#print(exp.objective()[-1])
#exp2.hypervolume()

#exp.save("savagef")
#exp.load("savagef")

#HV = exp2.hypervolume(generations = [130,150], objectives = [1,3])
#print(HV)

#HV2 = exp.hypervolume(generations = [130,150], objectives = [1,3])
#print(HV2)

#ss = exp.objective(objective = [2])
#ss = exp.variable(variable = "x")
#ff = exp.hypervolume( objectives= [1,2])


#exp.save("metalder")
#exp.load("metalder")

#exp.load("yrinfrt")

#exp3 = moeabench()
#exp.load("experiment")

#HV_all = exp.hypervolume()
#print(HV_all)

#exp3 = moeabench()
#exp3.problem = moeabench.benchmark.DTLZ1(M=3)
#exp3.moea = moeabench.Moea.SPEA2(problem=exp3.problem, population = 200, generations = 300)
#exp3.run()


#print(exp.result.get_elements()[0][0].get_F_GEN())

#moeabench.plot_hypervolume(exp.result,  objectives = [2,3])









 #ks = [b.get_F_GEN()[-1] for i in args for b in i.get_elements()[0]  if hasattr(b.__class__,"get_F_GEN")]
        #for obj, begin in enumerate(range(0,3), start = 1):
         #stat, value = ks_2samp(ks[0][:,begin],ks[1][:,begin])
         #print(f'objective {obj} KS stats {stat},  p-value {value}')




























































