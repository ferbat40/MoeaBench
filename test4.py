from MoeaBench import mb
import os, importlib
import numpy as np


os.system("cls")  


#Stopped due to hypervolume
import numpy as np
def stop(experiment):
    #restores the hypervolume of all generations to date.
    metric = mb.hypervolume.trace(experiment)
    hv = metric
    #checks generations every 20
    if len(hv)  % 20 == 0:
        gen = np.diff(hv[-21:])
        mean = np.mean(np.abs(gen))
        std_gen = np.std(gen)
        #If no increase is considered, execution is halted.
        return mean < 1e-3 and std_gen < 1e-3


exp = mb.experiment()
exp.name = 'experiment 1'
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.MOEAD(generations = 10, population = 50)
exp.moea.generations=150
exp.moea.seed = 4
exp.stop = stop
exp.name = "turicer"
exp.run()


exp2 = mb.experiment()
#exp2.name = 'experiment 2'
exp2.benchmark = mb.benchmarks.DTLZ1()
exp2.moea = mb.moeas.NSGA3(generations = 10, population = 50)
exp2.moea.generations=300
exp2.run(repeat = 5)

ref = [exp, exp2]
#ht = mb.hypervolume.trace(exp, reference=ref)
#mb.hypervolume.timeplot(exp2, exp, reference=ref)
#mb.spaceplot (exp, exp2, exp.front(100)) 


#mb.surfaceplot(exp, exp.objectives(generation = 10), exp2)