
import os
from MoeaBench import moeabench

import numpy as np


os.system("cls")  


exp  = moeabench()
exp2 = moeabench()
exp3 = moeabench()
exp4 = moeabench()

exp.problem = moeabench.benchmark.DTLZ1()
exp2.problem = moeabench.benchmark.DTLZ1()
exp3.problem = moeabench.benchmark.DTLZ1()
exp.moea = moeabench.Moea.NSGA3(problem=exp.problem, population = 130, generations = 500)
exp2.moea = moeabench.Moea.U_NSGA3(problem=exp2.problem, population = 240, generations = 200)
exp3.moea = moeabench.Moea.U_NSGA3(problem=exp3.problem, population = 100, generations = 300)
exp4.moea = moeabench.Moea.U_NSGA3(problem=exp2.problem, population = 350, generations = 300)
exp.RUN()

exp2.RUN()
#exp3.RUN()




#HV = exp.hypervolume(100)
#GD = exp.GD(100)
#GDplus =exp.GDplus(100)
#IGD = exp.IGD(100)
#IGDplus = exp.IGDplus(100)
#objectives = exp.objectives(3,90)





#exp2.IGDplus(199)



#exp.hypervolume(300)


exp2.hypervolume(300)
exp2.GD(300)
exp2.GDplus(300)
exp2.IGD(300)
exp2.IGDplus(300)
exp.objectives(1,270)







#moeabench.plot_hypervolume(exp, exp2, generations = 180)


moeabench.plot_obj(  exp, exp2,   generations = [150,170])


































































