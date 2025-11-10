
import os
from MoeaBench import moeabench




os.system("cls")  

exp = moeabench()


exp.problem = moeabench.benchmark.DTLZ1(M=3)
exp.moea = moeabench.MOEA.NSGA_III(problem=exp.problem, population = 300, generations = 400)
exp.run()

ss = exp.hypervolume(objectives=[1,1])
print(ss)


#exp.save("jaspion")

#exp3 = moeabench()
#exp3.load("jaspion")

#HV_all = exp.hypervolume()
#print(HV_all)

#exp3 = moeabench()
#exp3.problem = moeabench.benchmark.DTLZ1(M=3)
#exp3.moea = moeabench.Moea.SPEA2(problem=exp3.problem, population = 200, generations = 300)
#exp3.run()


#print(exp.result.get_elements()[0][0].get_F_GEN())

#moeabench.plot_hypervolume(exp.result,  objectives = [2,3])









































































