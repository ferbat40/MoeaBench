
import os
from MoeaBench import MoeaBench

import numpy as np


os.system("cls")   
moeabench = MoeaBench()


dtlz1 = moeabench.benchmark().DTLZ1()
nsga3 = moeabench.run().NSGA3(problem=dtlz1, population = 140, generations = 300)





































