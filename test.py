
import os
from MoeaBench import moeabench
#from MoeaBench.NSGA2deap import my_NSGA2deap
#from MoeaBench.my_dtlz5 import my_dtlz5



os.system("cls")  

exp = moeabench()


#exp.add_benchmark(my_dtlz5)
#exp.add_moea(my_NSGA2deap)


#exp.benchmark = moeabench.benchmark.my_dtlz5()
#exp.moea = moeabench.moea.my_NSGA2deap()
#exp.run()
#exp.save("savage")

exp2 = moeabench()
exp2.benchmark = moeabench.benchmark.DTLZ7()
exp2.moea = moeabench.moea.U_NSGAIII()
exp2.run()



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









































































