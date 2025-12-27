from MoeaBench import mb
import os, importlib
import numpy as np


os.system("cls")  





exp = mb.experiment()
exp.name = 'experiment 1'
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.MOEAD(generations = 10, population = 150)
exp.moea.generations=250
exp.moea.seed = 4
exp.name = "turicer"
exp.run()


hv  = mb.hypervolume(exp, generation = 100)   
#print(hv)

gd  = mb.igdplus(exp, generation = 100)
h_obj= mb.igdplus.trace(exp, objectives=[1,2])  # Restricted to some objectives.


#mb.igdplus.timeplot(exp, objectives=[1,2], generations = [99,100])


ind = mb.stats.indice(exp, generation = 125)
ks = mb.stats.kstest(exp, exp)
#print(ind)
#print(ks)

#print(mb.hypervolume.trace(exp).ndim)

mw = mb.stats.mwtest(mb.hypervolume.trace(exp),
                     mb.hypervolume.trace(exp), alternative='less')

print(mw.statistic)


pr = mb.stats.paretorank(exp)  # For a single experiment.
#pr.rank()                      # The rank array.
#pr.plot()    
