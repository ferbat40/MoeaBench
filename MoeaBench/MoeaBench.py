from .Benchmark import Benchmark
from .RUN import RUN
from .CACHE import CACHE
import numpy as np
from weakref import WeakKeyDictionary

class MoeaBench:

    def __init__(self):
        self.benchmark=Benchmark()
        self.result=CACHE()
        self.Moea=RUN(self.result)
        

    def pareto(self, *args):
        print(args)
        
        

    def RUN(self):
        self.Moea.MOEA_execute()


    def hypervolume(self, N = None):
        mtc = self.result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[1][0:N]
        mtcr = mtc.reshape(mtc.shape[0],1)
        return mtcr
    

    def GD(self, N = None):
        mtc = self.result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[2][0:N]
        mtcr = mtc.reshape(mtc.shape[0],1)
        return mtcr
    

    def GDplus(self, N = None):
        mtc = self.result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[3][0:N]
        mtcr = mtc.reshape(mtc.shape[0],1)
        return mtcr
    

    def IGD(self, N = None):
        mtc = self.result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[4][0:N]
        mtcr = mtc.reshape(mtc.shape[0],1)
        return mtcr
    

    def IGDplus(self, N = None):
        mtc = self.result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[5][0:N]
        mtcr = mtc.reshape(mtc.shape[0],1)
        return mtcr
    
    
    def objectives(self, I, N = None):
        mtc = self.result.get_elements()[0][0]
        objs = []
        for idx, obj in enumerate(mtc.get_METRIC_gen().get_arr_Metric_gen()[7], start = 0):
            if idx <= N:
                objs.append(obj[:,I-1:I])
        return objs

    


 
        



    
    

    
