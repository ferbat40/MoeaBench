from MoeaBench import mb
import os, importlib
import numpy as np


os.system("cls")  





exp = mb.experiment()
exp.name = 'experiment 1'
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.MOEAD(generations = 10, population = 50)
exp.moea.generations=150
exp.moea.seed = 4
exp.name = "turicer"
#exp.run()


exp2 = mb.experiment()
exp2.benchmark = mb.benchmarks.DTLZ1()
exp2.moea = mb.moeas.NSGA3(generations = 10, population = 100)
exp2.moea.generations=200
exp2.run(repeat = 3)


nd = exp2.round[0].front
pop = exp2.round[0].objectives


mask = np.ones(pop.shape[0], dtype=bool)
print(    nd[:   , None, :])


#mask_nd = np.any(
    #np.all(np.isclose(F[:, None, :], F_nd[None, :, :]), axis=2),
   # axis=1
#)