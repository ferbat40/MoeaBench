
import os
from MoeaBench import moeabench




os.system("cls")  

exp = moeabench()


exp.problem = moeabench.benchmarktest.DTLZ1t(3)
exp.moea = moeabench.moeatest.SPEA2t(problem = exp.problem )
exp.run()

exp.save("gavan_tolu")
#exp.load("gavan_tolu")

#for i in exp.result.get_elements():
    #print(i[0].get_F_GEN())










































































