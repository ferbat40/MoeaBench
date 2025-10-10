
import os
from MoeaBench import moeabench
from MoeaBench.base_moea import BaseMoea




import numpy as np


os.system("cls")  

exp  = moeabench()

@exp.Moea.register_moea()
class NSGA2deap(BaseMoea):
  def __init__(self,problem,population,generations):
    self.problem=problem
    self.population=population
    self.generations=generations

  def evaluation(self):
    print(self.problem,self.population,self.generations)








exp.moea = exp.Moea.my_new_moea(30,50,60)
exp.run()










#exp2 = moeabench()
#exp3 = moeabench()
#exp4 = moeabench()
#experiment = moeabench()



exp.problem = moeabench.benchmark.DTLZ2()
#exp2.problem = moeabench.benchmark.DTLZ1(M = 3)
#exp3.problem = moeabench.benchmark.DTLZ1()
exp.moea = moeabench.Moea.NSGA3(problem=exp.problem, population = 130, generations = 500)

#exp2.moea = moeabench.Moea.U_NSGA3(problem=exp2.problem, population = 240, generations = 400)
#exp3.moea = moeabench.Moea.U_NSGA3(problem=exp3.problem, population = 100, generations = 300)
#exp4.moea = moeabench.Moea.U_NSGA3(problem=exp2.problem, population = 350, generations = 300)
exp.run()

#exp2.run()
#exp3.RUN()




#exp.hypervolume(6600)
#exp.GD(200)
#exp.GDplus(200)
#exp.IGD(200)
#exp2.IGDplus(200)
#exp.objectives(3,1000)


##exp2.variables(7,910)



#exp2.save("my_experiment")


#experiment.load("my_experiment")
#experiment.hypervolume(200)





#moeabench.plot_hypervolume(exp, exp2, generations = 700)


#moeabench.plot_obj(  exp, exp2,   generations = [150,1500])
#moeabench.plot_var(  exp, exp2,   generations = [0,1500], variables = [1,2,7])


#moeabench.pareto(exp.result, exp2.pof,  objectives = [1,1,3])

#moeabench.pareto_surface(exp.result, exp2.pof,  objectives = [1,1,3])




































































