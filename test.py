
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




#exp.hypervolume(290)
#exp.GD(200)
#exp.GDplus(200)
#exp.IGD(200)
exp2.IGDplus(200)
#exp.objectives(3,500)


#exp2.variables(7,200)







#moeabench.plot_hypervolume(exp, exp2, generations = 700)


moeabench.plot_obj(  exp, exp2,   generations = [150,170])
moeabench.plot_var(  exp, exp2,   generations = [150,170])


































































