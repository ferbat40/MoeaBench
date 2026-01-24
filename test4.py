from MoeaBench import mb
import os, importlib
import numpy as np


os.system("cls")  


exp2 = mb.experiment()
exp2.name = 'experiment 1'
exp2.benchmark = mb.benchmarks.DPF3(M = 10, D = 3, K=10, P =2)
#print(exp2.optimal.front().shape)
#mb.spaceplot(exp2.optimal.front(), objectives = [1, 2, 3])


#exp2.moea = mb.moeas.NSGA3(population=150, generations=300)
#exp2.run()
#print(exp2.benchmark.__class__.__name__.split('_')[1]," M =",exp2.benchmark.M," N =",exp2.optimal.set().shape[1])
#exp2.benchmark.M = 5
#exp2.benchmark.D = 4
#print(exp2.benchmark.__class__.__name__.split('_')[1]," M =",exp2.benchmark.M," N =",exp2.optimal.set().shape[1])
#exp2.benchmark.M = 10
#exp2.benchmark.D = 9
#print(exp2.benchmark.__class__.__name__.split('_')[1]," M =",exp2.benchmark.M," N =",exp2.optimal.set().shape[1])


