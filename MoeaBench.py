from Benchmark import Benchmark
from RUN import RUN

class MoeaBench:

    def __init__(self):
        self.Benchmark=Benchmark()
        self.Moea=RUN()

    def RUN(self):
        print(self.Moea.DT_CONF.get_problem(), self.Moea.DT_CONF.get_DATA_MOEA())
        self.Moea.MOEA_execute(self.Moea.DT_CONF.get_DATA_MOEA(),self.Moea.DT_CONF.get_problem())
        print(self.Moea.CACHE.get_elements())
        



    
    

    
