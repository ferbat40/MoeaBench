from .Benchmark import Benchmark
from .RUN import RUN
from .RUN_user import RUN_user
import inspect
from .result_metric import result_metric
from .result_obj import result_obj
from .result_var import result_var
from .analyse_obj import analyse_obj
from .analyse_surface_obj import analyse_surface_obj
from .analyse_metric_gen import analyse_metric_gen
from .I_UserMoeaBench import I_UserMoeaBench
from .save import save
from .loader import loader
from . import benchmarktest
from . import moeatest
import importlib


class MoeaBench(I_UserMoeaBench):

    def __init__(self):
        self.problem=None
        self.pof=None
        self.moea=None
        self.benchmark=Benchmark()
        self.result=None
        self.Moea=RUN()
        self.result_metric=result_metric()
        self.result_obj=result_obj()
        self.result_var=result_var()
        self.Moea_user=RUN_user()


    def __getattr__(self,name):
        module = importlib.import_module(f"MoeaBench.{name}")
        return module
    

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


    def plot_hypervolume(self,*args, generations = [], objectives = []):   
        caller = inspect.currentframe().f_back.f_locals.items()
        experiment, data, benk, arr = analyse_surface_obj.extract_pareto_result(args,caller)   
        analyse_metric_gen.IPL_plot_Hypervolume(args,generations,experiments = experiment, objectives = objectives, bench = benk)


    def plot_GD(self,*args, generations = [], objectives = []):   
         caller = inspect.currentframe().f_back.f_locals.items()
         experiment, data, benk, arr = analyse_surface_obj.extract_pareto_result(args,caller)  
         analyse_metric_gen.IPL_plot_GD(args,generations,experiments = experiment, objectives = objectives, bench = benk)


    def plot_GDplus(self,*args, generations = [], objectives = []):  
         caller = inspect.currentframe().f_back.f_locals.items()
         experiment, data, benk, arr = analyse_surface_obj.extract_pareto_result(args,caller)  
         analyse_metric_gen.IPL_plot_GDplus(args,generations,experiments = experiment, objectives = objectives, bench = benk)

    
    def plot_IGD(self,*args, generations = [], objectives = []):   
         caller = inspect.currentframe().f_back.f_locals.items()
         experiment, data, benk, arr = analyse_surface_obj.extract_pareto_result(args,caller)  
         analyse_metric_gen.IPL_plot_IGD(args,generations,experiments = experiment, objectives = objectives, bench = benk)


    def plot_IGDplus(self,*args, generations = [], objectives = []):   
         caller = inspect.currentframe().f_back.f_locals.items()
         experiment, data, benk, arr = analyse_surface_obj.extract_pareto_result(args,caller)  
         analyse_metric_gen.IPL_plot_IGDplus(args,generations,experiments = experiment, objectives = objectives, bench = benk)


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
            
            execute = self.Moea_user if len(self.Moea.M_register.values()) == 1 or isinstance(self.result,tuple ) else self.Moea
            name_moea = self.result[2] if isinstance(self.result,tuple) else name_moea
            self.result = self.result[0] if isinstance(self.result,tuple) else self.result
           

            try:
                name_benchmark = self.problem.__class__.__name__.split("_")[1]
            except Exception as e:
                name_benchmark = self.problem.__class__.__name__

            return execute.MOEA_execute(self.result,self.problem,name_moea,name_benchmark)
        except Exception as e:
            print(e)


    def hypervolume(self, generations = [], objectives = []):
        try:
            return self.result_metric.IPL_hypervolume(self.result, generations, objectives)
        except Exception as e:
            print(e)
     

    def GD(self, generations = [], objectives = []):
        try:
            return self.result_metric.IPL_GD(self.result, generations, objectives)
        except Exception as e:
            print(e)


    def GDplus(self, generations = [], objectives = []):
        try:
            return self.result_metric.IPL_GDplus(self.result, generations, objectives)
        except Exception as e:
            print(e)
    

    def IGD(self, generations = [], objectives = []):
        try:
            return self.result_metric.IPL_IGD(self.result, generations, objectives)
        except Exception as e:
            print(e)
    

    def IGDplus(self, generations = [], objectives = []):
        try:
            return self.result_metric.IPL_IGDplus(self.result, generations, objectives)
        except Exception as e:
            print(e)

            
    def objective(self, objective, generations = []):
        try:
            return self.result_obj.IPL_objectives(self.result, generations, objective)
        except Exception as e:
            print(e)


    def variable(self, variable, generations = []):
        try:
            return self.result_var.IPL_variables(self.result, generations, variable)
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


    def add_benchmark(self,problem):
        import MoeaBench.benchmarktest as bk
        print(problem.__name__)
        setattr(bk,problem.__name__,problem)





    





 

    

    
    


 
        



    
    

    
