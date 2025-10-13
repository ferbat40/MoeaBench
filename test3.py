from MoeaBench.base_benchmark import BaseBenchmark
from MoeaBench import moeabench
import os



os.system("cls") 

exp = moeabench()
exp2 = moeabench()

@exp.benchmark.register_benchmark()
class my_dtlz7(BaseBenchmark):

    def __init__(self):
        self.M=3
        self.P=150
        self.N=10
    

    def evaluation(self):
        print("gavan")



exp.problem = exp.benchmark.my_new_benchmark()
exp2.problem = moeabench.benchmark.DTLZ1()

print(exp.problem,"   ",exp2.problem)









