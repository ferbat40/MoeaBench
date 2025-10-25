from .Benchmark import Benchmark
from .RUN import RUN
from .RUN_user import RUN_user
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
from .save_github import save_github
from .loader import loader
from .analyse_others_metric_gen import analyse_others_metric_gen


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


    def plot_obj(self,*args, objective, generations = [], std = False, mean = False, minimum = False, maximum = False):  
        try:
            data  = [b[0] for i in args for b in i.result.get_elements()]
            analyse_obj_gen.allowed_obj(data, objective)
            caller = inspect.currentframe().f_back.f_locals.items()
            val_metric = [idx for idx, i in enumerate([std,mean,minimum ,maximum], start = 0) if i is True]
            if len(val_metric) == 0:
                analyse_obj_gen.IPL_plot_3D(*args, experiments = [key for i in args for key, val in caller if i is val], generations = generations, objective = objective, mtc = 7) 
            elif len(val_metric) == 1:
                analyse_others_metric_gen.IPL_plot_3D(*args, experiments = [key for i in args for key, val in caller if i is val], generations = generations, objective = objective, mtc = 7 , val_metric = val_metric, types = "objective") 
            elif len(val_metric) > 1:
                raise ValueError("only one metric should be chosen")
        except Exception as e:
            print(e)
        

    def plot_var(self,*args, variable, generations = [], std = False, mean = False, minimum  = False, maximum = False):  
        try:
            data  = [b[0] for i in args for b in i.result.get_elements()]
            analyse_var_gen.allowed_obj(data, variable,8)
            caller = inspect.currentframe().f_back.f_locals.items()
            val_metric = [idx for idx, i in enumerate([std,mean,minimum ,maximum], start = 0) if i is True]
            if len(val_metric) == 0:
                analyse_var_gen.IPL_plot_3D(*args, experiments = [key for i in args for key, val in caller if i is val], generations = generations, variable = variable, mtc = 8) 
            elif len(val_metric) == 1:
                analyse_others_metric_gen.IPL_plot_3D(*args, experiments = [key for i in args for key, val in caller if i is val], generations = generations, objective = variable, mtc = 8 , val_metric = val_metric, types = "variable") 
            elif len(val_metric) == 2:
                raise ValueError("only one metric should be chosen")
        except Exception as e:
            print(e) 


    def plot_hypervolume(self,*args, generations = []):   
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


    def hypervolume(self, generations = []):
        try:
            return self.result_metric.IPL_hypervolume(self.result, generations)
        except Exception as e:
            print(e)
     

    def GD(self, generations = []):
        try:
            return self.result_metric.IPL_GD(self.result, generations)
        except Exception as e:
            print(e)


    def GDplus(self, generations = []):
        try:
            return self.result_metric.IPL_GDplus(self.result,generations)
        except Exception as e:
            print(e)
    

    def IGD(self, generations = []):
        try:
            return self.result_metric.IPL_IGD(self.result, generations)
        except Exception as e:
            print(e)
    

    def IGDplus(self, generations = []):
        try:
            return self.result_metric.IPL_IGDplus(self.result, generations)
        except Exception as e:
            print(e)
    
    
    def objectives(self, objective, generations = []):
        try:
            return self.result_obj.IPL_objectives(self.result, objective,  generations)
        except Exception as e:
            print(e)


    def variables(self, variable, generations = []):
        try:
            return self.result_var.IPL_variables(self.result, variable, generations)
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


    def save_class(self):
        try:
            save_github.IPL_save_github(self)
        except Exception as e:
            print(e)


    






 

    

    
    


 
        



    
    

    
