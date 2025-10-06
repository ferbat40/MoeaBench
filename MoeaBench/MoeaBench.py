from .Benchmark import Benchmark
from .RUN import RUN
from .CACHE import CACHE
from .analyse_obj_gen  import analyse_obj_gen
import inspect
from .result_metric import result_metric
from .result_obj import result_obj
from .result_var import result_var
from .analyse_POF import analyse_POF
from .analyse_metric_gen import analyse_metric_gen
from .I_UserMoeaBench import I_UserMoeaBench


class MoeaBench(I_UserMoeaBench):

    def __init__(self):
        self.problem=None
        self.pof=None
        self.moea=None
        self.result=None
        self.benchmark=Benchmark()
        self.result=CACHE()
        self.Moea=RUN(self.result)
        self.result_metric=result_metric()
        self.result_obj=result_obj()
        self.result_var=result_var()
        self.analyse_pof=analyse_POF()


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


    def plot_obj(self,*args, generations = [], objectives = []):  
        caller = inspect.currentframe().f_back.f_locals.items()
        analyse_obj_gen.IPL_plot_obj(*args, experiments = [key for i in args for key, val in caller if i is val], generations = generations, objectives = objectives) 
       

    def plot_hypervolume(self,*args, generations = None):   
        caller = inspect.currentframe().f_back.f_locals.items()
        analyse_metric_gen.IPL_plot_Hypervolume(args,generations,1,experiments = [key for i in args for key, val in caller if i is val])


    def plot_GD(self,*args, generations = None):   
         caller = inspect.currentframe().f_back.f_locals.items()
         analyse_metric_gen.IPL_plot_GD(args,generations,2,experiments = [key for i in args for key, val in caller if i is val])


    def plot_GDplus(self,*args, generations = None):  
        caller = inspect.currentframe().f_back.f_locals.items() 
        analyse_metric_gen.IPL_plot_GDplus(args,generations,3,experiments = [key for i in args for key, val in caller if i is val])

    
    def plot_IGD(self,*args, generations = None):   
        caller = inspect.currentframe().f_back.f_locals.items()
        analyse_metric_gen.IPL_plot_IGD(args,generations,4,experiments = [key for i in args for key, val in caller if i is val])


    def plot_IGDplus(self,*args, generations = None):   
        caller = inspect.currentframe().f_back.f_locals.items()
        analyse_metric_gen.IPL_plot_IGDplus(args,generations,5,experiments = [key for i in args for key, val in caller if i is val])
            

    def pareto(self,*args, objectives):
        print(args,objectives)
        
        
    def RUN(self):
        self.Moea.MOEA_execute(self.result)


    def hypervolume(self, N = None):
        self.result_metric.IPL_display(self.result_metric.IPL_hypervolume(self.result, N))
     

    def GD(self, N = None):
        self.result_metric.IPL_display(self.result_metric.IPL_GD(self.result, N))


    def GDplus(self, N = None):
        self.result_metric.IPL_display(self.result_metric.IPL_GDplus(self.result, N))
    

    def IGD(self, N = None):
        self.result_metric.IPL_display(self.result_metric.IPL_IGD(self.result, N))
    

    def IGDplus(self, N = None):
        self.result_metric.IPL_display(self.result_metric.IPL_IGDplus(self.result, N))
    
    
    def objectives(self, I, N = None):
        self.result_obj.IPL_display(self.result_obj.IPL_objectives(self.result, I,  N),I)


    def variables(self, I, N = None):
        self.result_var.IPL_display(self.result_var.IPL_variables(self.result, I,  N),I)


 

    

    
    


 
        



    
    

    
