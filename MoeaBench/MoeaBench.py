from .Benchmark import Benchmark
from .RUN import RUN
from .CACHE import CACHE
from .plot_gen import plot_gen
from .plot_solutions_3D import plot_solutions_3D
import numpy as np
from itertools import zip_longest
import inspect
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


    def allowed_gen(self, generations):
        if not isinstance(generations, (list)):
            raise TypeError("Only arrays are allowed in 'generations'")
        if not len(generations) == 2:
            raise TypeError(f"generations = {generations} not be allowed. I is necessary to follow the format: generations = [begin, end]" )
        

    def allowed_obj(self,element,data, experiments, objectives, obj = ('get_M',)):
        if not isinstance(objectives, (list)):
            raise TypeError("Only arrays are allowed in 'objectives'")
        if  0 < len(objectives) < 3:
            raise TypeError(f"objectives = {objectives} not be allowed. I is necessary to follow the format: objectives = [obj1, obj2, obj3] " )
        list_valid = list(map(lambda o: o.get_M(), filter(lambda o: all(hasattr(o,m) for m in obj), element)))
        if not all(np.array_equal(data.get_M(),arr) for arr in list_valid):
            objs = [f'{experiments[idx]}.problem = {i.get_M()} objectives' for idx, i in enumerate(element, start = 0)]
            raise ValueError (f'{objs} must be equals')   
        less = [i if i > element[0].get_M() else f'obj' for idx, i in enumerate(objectives, start = 0)  ]
        digit = [i for i in less if str(i).isdigit()]
        if digit:
            raise ValueError (f'Objective(s) {less} can´t be greather than {element[0].get_M()}')   


    def plot_obj(self,*args, generations = [], objectives = []):  
      try:
        self.allowed_gen(generations)
        caller = inspect.currentframe().f_back.f_locals.items()
        experiments = [key for i in args for key, val in caller if i is val]
        data  = [b[0] for i in args for b in i.result.get_elements()]
        bench = [b[1] for i in args for b in i.result.get_elements()]
        self.allowed_obj(bench,bench[0],experiments,objectives)
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
                        pad = np.full((max-i.shape[0],i.shape[1]), np.nan)
                        arr = np.vstack([i,pad])
                        vet_aux.append(arr)
                    else:
                        vet_aux.append(i)   

                except Exception as e:
                    pad = np.full((max,3), np.nan)
                    vet_aux.append(pad)     
            vet_pt.append(vet_aux)          


        if not len([b for i in vet_pt for b in i if not np.all(np.isnan(b)) and len(b) > 0]) > 0:   
            raise ValueError (f'No results found for plot')

        axis =  [i for i in range(0,3)]    if len(objectives) == 0 else [i-1 if i > 0 else 0 for i in objectives] 
        self.plot_3DSO =  plot_solutions_3D(data,bench,vet_pt,generations,experiments,axis)
        self.plot_3DSO.configure()
      except Exception as e:
        print(e)


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
        try:
            N=N+1
        except Exception as e:
            pass
        mtc = np.array([i for idx, i in enumerate(self.result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[1][0:N], start = 0)])
        mtcr = mtc.reshape(mtc.shape[0],1)
        return mtcr
    

    def GD(self, N = None):
        try:
            N=N+1
        except Exception as e:
            pass
        mtc = np.array([i for idx, i in enumerate(self.result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[2][0:N], start = 0)])
        mtcr = mtc.reshape(mtc.shape[0],1)
        return mtcr 
    

    def GDplus(self, N = None):
        try:
            N=N+1
        except Exception as e:
            pass
        mtc = np.array([i for idx, i in enumerate(self.result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[3][0:N], start = 0)])
        mtcr = mtc.reshape(mtc.shape[0],1)
        return mtcr
    

    def IGD(self, N = None):
        try:
            N=N+1
        except Exception as e:
            pass
        mtc = np.array([i for idx, i in enumerate(self.result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[4][0:N], start = 0)])
        mtcr = mtc.reshape(mtc.shape[0],1)
        return mtcr
    

    def IGDplus(self, N = None):
        try:
            N=N+1
        except Exception as e:
            pass
        mtc = np.array([i for idx, i in enumerate(self.result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[5][0:N], start = 0)])
        mtcr = mtc.reshape(mtc.shape[0],1)
        return mtcr
    
    
    def objectives(self, I, N = None):
        mtc = self.result.get_elements()[0][0]
        mtcr = [[idx,obj[:,I-1:I]] for idx, obj in enumerate(mtc.get_METRIC_gen().get_arr_Metric_gen()[7][0:N])]
        return mtcr
    

    def display(self,objectives):
        try:
            for i in objectives:
                print(f'\ngeneration {i[0]}\n')
            for f in i[1]:
                print(f)
        except Exception as e:
            pass
       
        try:
            for idx, i in enumerate(objectives, start = 0):
                print(f'generation {idx} = {i[0]}')
        except Exception as e:
            pass


 

    def DATA(self,args,generations,metrics):
        data  = [b[0] for i in args for b in i.result.get_elements()]
        bench = [b[1] for i in args for b in i.result.get_elements()]
        evaluate = [np.arange(1,generations+1) for _ in range(len(data))]
        metric = [np.array(i.get_METRIC_gen().get_arr_Metric_gen()[metrics][0:generations]).flatten() for i in data]
        label = [f'{dt.get_description()}     (GEN={dt.get_generations()},POP={dt.get_population()})     (M={bk.get_M()},K={bk.get_K()},N={bk.get_Nvar()},D={bk.get_D()})' if int(dt.get_generations())+int(dt.get_population())>0 
                 else f'{dt.get_description()}' for dt,bk in zip(data,bench)]
        title=f'for {bench[0].get_BENCH()}'
        return [evaluate,metric],label,title
    

    
    


 
        



    
    

    
