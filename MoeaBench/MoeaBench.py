from .Benchmark import Benchmark
from .RUN import RUN
from .CACHE import CACHE
import numpy as np

class MoeaBench:

    def __init__(self):
        self.cache_benckmark=CACHE()
        self.benchmark=Benchmark(self.cache_benckmark)
        self.cache_moea=CACHE()
        self.Moea=RUN(self.cache_moea)


    def RUN(self):
        self.Moea.MOEA_execute(self.Moea.DT_CONF.get_DATA_MOEA(),self.Moea.DT_CONF.get_problem())
    

    def hypervolume(self, N = None):
        mtc = self.cache_moea.get_elements()[0][0]
        return mtc.get_METRIC_gen().get_arr_Metric_gen()[1][0:N]
    

    def GD(self, N = None):
        mtc = self.cache_moea.get_elements()[0][0]
        return mtc.get_METRIC_gen().get_arr_Metric_gen()[2][0:N]
    

    def GDplus(self, N = None):
        mtc = self.cache_moea.get_elements()[0][0]
        return mtc.get_METRIC_gen().get_arr_Metric_gen()[3][0:N]
    

    def IGD(self, N = None):
        mtc = self.cache_moea.get_elements()[0][0]
        return mtc.get_METRIC_gen().get_arr_Metric_gen()[4][0:N]
    

    def IGDplus(self, N = None):
        mtc = self.cache_moea.get_elements()[0][0]
        return mtc.get_METRIC_gen().get_arr_Metric_gen()[5][0:N]
    

    def objectives(self, I, N = None):
        mtc = self.cache_moea.get_elements()[0][0]
        objs = []
        for idx, obj in enumerate(mtc.get_METRIC_gen().get_arr_Metric_gen()[7], start = 0):
            if idx <= N:
                objs.append(obj[:,I-1:I])
        return objs

    


 
        



    
    

    
