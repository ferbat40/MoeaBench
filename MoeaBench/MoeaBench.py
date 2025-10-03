from .Benchmark import Benchmark
from .RUN import RUN
from .CACHE import CACHE
from .plot_gen import plot_gen
from .plot_solutions_3D import plot_solutions_3D
import numpy as np
from itertools import zip_longest
import inspect
from IPython.display import display,Javascript
import json

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
        self.plot_sl3D=None


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


    def allowed(self,element,data, experiments, obj = ('get_M',)):
        list_valid = list(map(lambda o: o.get_M(), filter(lambda o: all(hasattr(o,m) for m in obj), element)))
        if not all(np.array_equal(data.get_M(),arr) for arr in list_valid):
            obj = [f'{experiments[idx]}.problem = {i.get_M()} obj' for idx, i in enumerate(element, start = 0)]
            raise ValueError (f'{obj} must be equals')   


    def plot_obj(self,*args, generations = [], objectives = []):  
      try:
        caller = inspect.currentframe().f_back.f_locals.items()
        experiments = [key for i in args for key, val in caller if i is val]
        data  = [b[0] for i in args for b in i.result.get_elements()]
        bench = [b[1] for i in args for b in i.result.get_elements()]
        self.allowed(bench,bench[0],experiments)
        vet=[]
        for i in data:
            vet.append(i.get_METRIC_gen().get_arr_Metric_gen()[7][generations[0]:generations[1]+1])
        max = 0
        for row in zip_longest(*vet,fillvalue=np.nan):
            for i in row:
                try:
                    if i.shape[0]> max:
                        max=i.shape[0]
                except Exception as e:
                    continue

        vet_pt=[]
        for row in zip_longest(*vet,fillvalue=np.nan):
            vet_aux=[]
            for i in row:
                try:
                    if i.shape[0]<max:
                        pad = np.zeros((max-i.shape[0],i.shape[1]))
                        arr = np.vstack([i,pad])
                        vet_aux.append(arr)
                    else:
                        vet_aux.append(i)   

                except Exception as e:
                    pad = np.zeros((max,3))
                    vet_aux.append(pad)               
            vet_pt.append(vet_aux)  
        self.plot_3DSO =  plot_solutions_3D(data,bench,vet_pt,generations,experiments)
        self.plot_3DSO.configure()
      except Exception as e:
        msg = json.dumps(str(e))
        display(Javascript(f'alert({msg})'))


    def plot_hypervolume(self,*args, generations = None):   
        markers,label,title = self.DATA(args,generations,metrics=1)
        self.plot_g=self.plot_g(markers,label,title, metric = ['Hypervolume','Generations']) if self.plot_g is not None else plot_gen(markers,label,title, metric = ['Hypervolume','Generations'])
        self.plot_g.PLT()


    def plot_GD(self,*args, generations = None):   
        markers,label,title = self.DATA(args,generations,metrics=2)
        self.plot_g=self.plot_g(markers,label,title, metric = ['GD','Generations']) if self.plot_g is not None else plot_gen(markers,label,title, metric = ['GD','Generations'])
        self.plot_g.PLT()


    def plot_GDplus(self,*args, generations = None):   
        markers,label,title = self.DATA(args,generations,metrics=3)
        self.plot_g=self.plot_g(markers,label,title, metric = ['GD plus','Generations']) if self.plot_g is not None else plot_gen(markers,label,title, metric = ['GD plus','Generations'])
        self.plot_g.PLT()

    
    def plot_IGD(self,*args, generations = None):   
        markers,label,title = self.DATA(args,generations,metrics=4)
        self.plot_g=self.plot_g(markers,label,title, metric = ['IGD','Generations']) if self.plot_g is not None else plot_gen(markers,label,title, metric = ['IGD','Generations'])
        self.plot_g.PLT()


    def plot_IGDplus(self,*args, generations = None):   
        markers,label,title = self.DATA(args,generations,metrics=4)
        self.plot_g=self.plot_g(markers,label,title, metric = ['IGD plus','Generations']) if self.plot_g is not None else plot_gen(markers,label,title, metric = ['IIGD plus','Generations'])
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
        evaluate = [np.arange(1,generations+1) for _ in range(len(data))]
        metric = [np.array(i.get_METRIC_gen().get_arr_Metric_gen()[metrics][0:generations]).flatten() for i in data]
        label = [f'{dt.get_description()}     (GEN={dt.get_generations()},POP={dt.get_population()})     (M={bk.get_M()},K={bk.get_K()},N={bk.get_Nvar()},D={bk.get_D()})' if int(dt.get_generations())+int(dt.get_population())>0 
                 else f'{dt.get_description()}' for dt,bk in zip(data,bench)]
        title=f'for {bench[0].get_BENCH()}'
        return [evaluate,metric],label,title
    

    
    


 
        



    
    

    
