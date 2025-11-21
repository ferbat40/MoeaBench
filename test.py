
import os
from MoeaBench import moeabench
from MoeaBench.NSGA2deap import my_NSGA2deap
from MoeaBench.my_dtlz5 import my_dtlz5



os.system("cls")  

exp = moeabench()


exp.add_benchmark(my_dtlz5)
exp.add_moea(my_NSGA2deap)


exp.benchmark = moeabench.benchmarks.my_dtlz5()
exp.moea = moeabench.moeas.my_NSGA2deap()
exp.run()

#ss = exp.objective(objective = [2])
#ss = exp.variable(variable = "x")
#ff = exp.hypervolume( objectives= [1,2])


exp.save("metalder")
exp.load("metalder")

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









































































