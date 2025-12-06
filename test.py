from MoeaBench import mb
import os




os.system("cls")  


exp = mb.experiment()
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.NSGA3(generations = 400, population = 190)
exp.run()


#obj = exp.objectives( generations = [199])
#print(obj[1])


#var = exp.variables(generations = [5])
#print(var)

