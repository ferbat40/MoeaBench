from .Benchmark import Benchmark
from .RUN import RUN
from .CACHE import CACHE
from .plot_gen import plot_gen
import numpy as np

class MoeaBench:

    def __init__(self):
        self.problem=None
        self.pof=None
        self.moea=None
        self.result=None
        self.benchmark=Benchmark()
        self.result=CACHE()
        self.Moea=RUN(self.result)
        self.plot_g=None


    @property
    def moea(self):
        return self._moea
    

    @moea.setter
    def moea(self,value):
        self._moea=value
        self.result=value


    @property
    def problem(self):
        return self._problem
    

    @problem.setter
    def problem(self,value):
        self._problem=value
        self.pof=value


    def plot_hypervolume(self,*args, generations = None):   
        markers,label,title = self.DATA(args,generations,metrics=1)
        self.plot_g=self.plot_g(markers,label,title, metric = ['Hypervolume','Evaluations']) if self.plot_g is not None else plot_gen(markers,label,title, metric = ['Hypervolume','Generations'])
        self.plot_g.PLT()
            

    def pareto(self,*args, objectives):
        print(args,objectives)
        
        
    def RUN(self):
        self.Moea.MOEA_execute(self.result)


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


    def DATA(self,args,generations,metrics):
        data  = [b[0] for i in args for b in i.result.get_elements()]
        bench = [b[1] for i in args for b in i.result.get_elements()]
        evaluate = [[np.array(i) for i in range(0,generations)]]
        metric = [np.array(i.get_METRIC_gen().get_arr_Metric_gen()[metrics][0:generations]).flatten() for i in data]
        label = [f'{dt.get_description()}     (GEN={dt.get_generations()},POP={dt.get_population()})     (M={bk.get_M()},K={bk.get_K()},N={bk.get_Nvar()},D={bk.get_D()})' if int(dt.get_generations())+int(dt.get_population())>0 
                 else f'{dt.get_description()}' for dt,bk in zip(data,bench)]
        title=f'for {bench[0].get_BENCH()}'
        return [evaluate,metric],label,title
    

    
    


 
        



    
    

    
