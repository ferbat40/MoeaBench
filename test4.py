from MoeaBench import mb
import os, importlib
import numpy as np


os.system("cls")  


exp = mb.experiment()
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.MOEAD(generations = 10, population = 150)
exp.moea.generations=150
#exp.moea.seed = 4
exp.run()


exp2 = mb.experiment()
exp2.benchmark = mb.benchmarks.DTLZ1()
exp2.moea = mb.moeas.NSGA3(generations = 10, population = 150)
exp2.moea.generations=300
exp2.run(repeat = 5)

ks = mb.stats.kstest(exp, exp.front(100))
print(ks.statistic[1])
print(ks.pvalue[1])

#ks.plot()


mw = mb.stats.mwtest(mb.hypervolume.trace(exp), 
                     mb.hypervolume.trace(exp2), alternative='less')

print(mw.statistic)
print(mw.pvalue)

pr = mb.stats.paretorank(exp)
print(pr.rank())

#pr.plot()
#ind = mb.stats.indice(exp)
#print(ind)
