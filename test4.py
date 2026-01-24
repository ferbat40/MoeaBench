from MoeaBench import mb
import os, importlib
import numpy as np


os.system("cls")  


exp2 = mb.experiment()
exp2.name = 'experiment 1'
exp2.benchmark = mb.benchmarks.DTLZ5(M = 3, K = 10, P = 1000)
benchmark = exp2.benchmark.__class__.__name__.split('_')[1]
name = f"c:\\optimal\\legacy_{benchmark}_M_{exp2.benchmark.M}_K_{exp2.benchmark.K}_N_{exp2.optimal.set().shape[1]}_samples_{exp2.benchmark.P}.csv"
print(name)
np.savetxt(name, exp2.optimal.front(), delimiter=',', fmt='%f')