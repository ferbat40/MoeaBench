from MoeaBench import mb
import os




os.system("cls")  


exp = mb.experiment()
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.NSGA3(generations = 200, population = 100)
exp.run()
exp.save("RVEA")

exp2 = mb.experiment()
exp2.load("RVEA")
arr = exp2.hypervolume()
print(arr)