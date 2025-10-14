from .Benchmark import Benchmark
from .RUN import RUN
from .RUN_user import RUN_user
from .CACHE import CACHE
from .analyse_obj_gen  import analyse_obj_gen
import inspect
from .result_metric import result_metric
from .result_obj import result_obj
from .result_var import result_var
from .analyse_obj import analyse_obj
from .analyse_surface_obj import analyse_surface_obj
from .analyse_metric_gen import analyse_metric_gen
from .analyse_var_gen import analyse_var_gen
from .I_UserMoeaBench import I_UserMoeaBench
from .save import save
from .loader import loader


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
        self.Moea_user=RUN_user(self.result)
       

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
        analyse_obj_gen.IPL_plot_3D(*args, experiments = [key for i in args for key, val in caller if i is val], generations = generations, objectives = objectives, mtc = 7 , type = "objectives in generations") 
       

    def plot_var(self,*args, generations = [], variables = []):  
        caller = inspect.currentframe().f_back.f_locals.items()
        analyse_var_gen.IPL_plot_3D(*args, experiments = [key for i in args for key, val in caller if i is val], generations = generations, objectives = variables, mtc = 8,  type = "decision variables in generations") 
  

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


    def pareto_surface(self, *args, objectives = []):
        caller = inspect.currentframe().f_back.f_locals.items()
        experiment, data, benk, arr = analyse_surface_obj.extract_pareto_result(args,caller)       
        analyse_surface_obj.IPL_plot_3D(experiment, data, benk, arr, objectives)  


    def pareto(self, *args, objectives = []):
        caller = inspect.currentframe().f_back.f_locals.items()
        experiment, data, benk, arr = analyse_obj.extract_pareto_result(args,caller)       
        analyse_obj.IPL_plot_3D(experiment, data, benk, arr, objectives)     
        
        
    def run(self):
        try:
            name_moea=None
            name_benchmark=None
            try:
                name_moea = self.Moea.get_moea().__name__
            except Exception as e:
                pass
            execute = self.Moea_user if len(self.Moea.M_register.values()) == 1 else self.Moea
            
            try:
                name_benchmark = self.problem.__class__.__name__.split("_")[1]
            except Exception as e:
                name_benchmark = self.problem.__class__.__name__.split("_")
            
            return execute.MOEA_execute(self.result,self.problem,name_moea,name_benchmark)
        except Exception as e:
            print(e)


    def hypervolume(self, N = None):
        try:
            self.result_metric.IPL_display(self.result_metric.IPL_hypervolume(self.result, N))
        except Exception as e:
            print(e)
     

    def GD(self, N = None):
        try:
            self.result_metric.IPL_display(self.result_metric.IPL_GD(self.result, N))
        except Exception as e:
            print(e)


    def GDplus(self, N = None):
        try:
            self.result_metric.IPL_display(self.result_metric.IPL_GDplus(self.result, N))
        except Exception as e:
            print(e)
    

    def IGD(self, N = None):
        try:
            self.result_metric.IPL_display(self.result_metric.IPL_IGD(self.result, N))
        except Exception as e:
            print(e)
    

    def IGDplus(self, N = None):
        try:
            self.result_metric.IPL_display(self.result_metric.IPL_IGDplus(self.result, N))
        except Exception as e:
            print(e)
    
    
    def objectives(self, I, N = None):
        try:
            self.result_obj.IPL_display(self.result_obj.IPL_objectives(self.result, I,  N),I)
        except Exception as e:
            print(e)


    def variables(self, I, N = None):
        try:
            self.result_var.IPL_display(self.result_var.IPL_variables(self.result, I,  N),I)
        except Exception as e:
            print(e)


    def load(self,file):
        try:
            loader.IPL_loader(self,file)      
        except Exception as e:
            print(e)


    def save(self, file):
        try:
            save.IPL_save(self,file)
        except Exception as e:
            print(e)


    def my_new_benchmark(self):
        pass
    



 

    

    
    


 
        



    
    

    
