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
exp.run(repeat = 2)


