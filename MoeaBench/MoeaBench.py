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
import importlib


class MoeaBench(I_UserMoeaBench):
      
    def __init__(self):
        self.pof=None
        self.result=None
        self.result_metric=result_metric()
        self.result_obj=result_obj()
        self.result_var=result_var()


    def __getattr__(self,name):
        if name.startswith("__") and name.endswith("__"):
            return super().__getattribute__(name)
        if name.startswith("_") and name in ["_benchmark","_moea","_result","_pof"]:
           raise AttributeError(name)
        try:
            return importlib.import_module(f"MoeaBench.{name}")
        except ModuleNotFoundError:
            raise AttributeError(name)
    

    @property
    def moea(self):
        return self._moea
    

    @moea.setter
    def moea(self,value):  
        self.result = value(self.benchmark, self.moeas) if callable(value) else value
        self._moea = value


    @property
    def benchmark(self):
        return self._benchmark
    

    @benchmark.setter
    def benchmark(self,value):
        self._benchmark=value(self.benchmarks) if callable(value) else value
        self.pof=self._benchmark 


    def plot_hypervolume(self,*args, generations = [], objectives = []):   
        """
        - **2D graph for hypervolume:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      moeabench.plot_hypervolume(args) 
                      - [plot_hypervolume](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/plot_hypervolume/) information about the method, accepted variable types, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/exceptions/) information on possible error types

        """
        caller = inspect.currentframe().f_back.f_locals.items()
        experiment, data, benk, arr = analyse_surface_obj.extract_pareto_result(args,caller)   
        analyse_metric_gen.IPL_plot_Hypervolume(args,generations,experiments = experiment, objectives = objectives, bench = benk)


    def plot_GD(self,*args, generations = [], objectives = []):   
         """
        - **2D graph for GD:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      moeabench.plot_GD(args) 
                      - [plot_GD](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/plot_GD/) information about the method, accepted variable types, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/exceptions/) information on possible error types

         """
         caller = inspect.currentframe().f_back.f_locals.items()
         experiment, data, benk, arr = analyse_surface_obj.extract_pareto_result(args,caller)  
         analyse_metric_gen.IPL_plot_GD(args,generations,experiments = experiment, objectives = objectives, bench = benk)


    def plot_GDplus(self,*args, generations = [], objectives = []):  
         """
         - **2D graph for GD+:**
         Click on the links for more
         ...
                - **Informations:**
                      - sinxtase:
                      moeabench.plot_GDplus(args) 
                      - [plot_GDplus](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/plot_GDplus/) information about the method, accepted variable types, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/exceptions/) information on possible error types

         """
         caller = inspect.currentframe().f_back.f_locals.items()
         experiment, data, benk, arr = analyse_surface_obj.extract_pareto_result(args,caller)  
         analyse_metric_gen.IPL_plot_GDplus(args,generations,experiments = experiment, objectives = objectives, bench = benk)

    
    def plot_IGD(self,*args, generations = [], objectives = []):   
         """
         - **2D graph for IGD:**
         Click on the links for more
         ...
                - **Informations:**
                      - sinxtase:
                      moeabench.plot_IGD(args) 
                      - [plot_IGD](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/plot_IGD/) information about the method, accepted variable types, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/exceptions/) information on possible error types

         """
         caller = inspect.currentframe().f_back.f_locals.items()
         experiment, data, benk, arr = analyse_surface_obj.extract_pareto_result(args,caller)  
         analyse_metric_gen.IPL_plot_IGD(args,generations,experiments = experiment, objectives = objectives, bench = benk)


    def plot_IGDplus(self,*args, generations = [], objectives = []):   
         """
         - **2D graph for IGD+:**
         Click on the links for more
         ...
                - **Informations:**
                      - sinxtase:
                      moeabench.plot_IGDplus(args) 
                      - [plot_IGDplus](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/plot_IGDplus/) information about the method, accepted variable types, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/exceptions/) information on possible error types

         """
         caller = inspect.currentframe().f_back.f_locals.items()
         experiment, data, benk, arr = analyse_surface_obj.extract_pareto_result(args,caller)  
         analyse_metric_gen.IPL_plot_IGDplus(args,generations,experiments = experiment, objectives = objectives, bench = benk)


    def pareto_surface(self, *args, objectives = []):
        """
        - **3D graph of the Pareto boundary surface:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      moeabench.pareto_surface(exp.problem, experiment2_result, experiment.pof...)  
                      - [pareto_surface](https://moeabench-rgb.github.io/MoeaBench/analysis/objectives/plot/pareto_surface/) information about the method, accepted variable types, examples and more...
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/objectives/plot/exceptions/) information on possible error types
       
        """
        
        caller = inspect.currentframe().f_back.f_locals.items()
        experiment, data, benk, arr = analyse_surface_obj.extract_pareto_result(args,caller)       
        analyse_surface_obj.IPL_plot_3D(experiment, data, benk, arr, objectives)  


    def pareto(self, *args, objectives = []):
        """
        - **3D graph for Pareto front:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      moeabench.pareto(args)  
                      - [pareto](https://moeabench-rgb.github.io/MoeaBench/analysis/objectives/plot/pareto/) information about the method, accepted variable types, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/objectives/plot/exceptions/) information on possible error types

        """
       

        caller = inspect.currentframe().f_back.f_locals.items()
        experiment, data, benk, arr = analyse_obj.extract_pareto_result(args,caller)       
        analyse_obj.IPL_plot_3D(experiment, data, benk, arr, objectives)     
        
        
    def run(self):
        """
        - **run the genetic algorithm:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.run()   
                      - [run()](https://moeabench-rgb.github.io/MoeaBench/experiments/combinations/combinations/#moeabench-run-the-experiment) Information about the method and return variables.

        """

        if isinstance(self.result,tuple):
            name_moea = self.result[2]
        else:
            name_moea = self.result.edit_DATA_conf().get_DATA_MOEA().__class__.__name__
         
        try:
            name_benchmark=None
            execute = RUN() if self.moea.__module__.find(".moea") >= 0 else RUN_user()
            self.result = self.result[0] if isinstance(self.result,tuple) else self.result

            try:
                name_benchmark = self.benchmark.__class__.__name__.split("_")[1]
            except Exception as e:
                name_benchmark = self.benchmark.__class__.__name__
                
            return execute.MOEA_execute(self.result,self.benchmark,name_moea,name_benchmark)
        except Exception as e:
            print(e)


    def hypervolume(self, generations = [], objectives = []):
        """
        - **array with hypervolume in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.hypervolume(args)  
                      - [hypervolume](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/hypervolume/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return self.result_metric.IPL_hypervolume(self.result, generations, objectives)
        except Exception as e:
            print(e)
     

    def GD(self, generations = [], objectives = []):
        """
        - **array with GD in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.GD(args)  
                      - [GD](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/GD/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return self.result_metric.IPL_GD(self.result, generations, objectives)
        except Exception as e:
            print(e)


    def GDplus(self, generations = [], objectives = []):
        """
        - **array with GD+ in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.GDplus(args)  
                      - [GDplus](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/GDplus/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return self.result_metric.IPL_GDplus(self.result, generations, objectives)
        except Exception as e:
            print(e)
    

    def IGD(self, generations = [], objectives = []):
        """
        - **array with IGD in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.IGD(args)  
                      - [IGD](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/IGD/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return self.result_metric.IPL_IGD(self.result, generations, objectives)
        except Exception as e:
            print(e)
    

    def IGDplus(self, generations = [], objectives = []):
        """
        - **array with IGD+ in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.IGDplus(args)  
                      - [IGDplus](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/IGDplus/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return self.result_metric.IPL_IGDplus(self.result, generations, objectives)
        except Exception as e:
            print(e)

            
    def objective(self, objective = 1, generations = [], last = False):
        """
        - **array with objectives in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.objective(args)  
                      - [objective](https://moeabench-rgb.github.io/MoeaBench/analysis/objectives/data/objective/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return self.result_obj.IPL_objectives(self.result, generations, objective, last)
        except Exception as e:
            print(e)


    def variable(self, variable = 1, generations = []):
        """
        - **array with decision variables in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.variable(args)  
                      - [variable](https://moeabench-rgb.github.io/MoeaBench/analysis/variables/data/variable/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return self.result_var.IPL_variables(self.result, generations, variable)
        except Exception as e:
            print(e)


    def load(self,file):
        """
        - **Loads a user experiment into MoeaBench:**
        Click on the links for more
        ...
                - Informations:
                      - sinxtase:
                      experiment.load(nameFile)  
                      - [load](https://moeabench-rgb.github.io/MoeaBench/experiments/load_experiment/load_experiment/) information about the method, 
                     
        """
        try:
            loader.IPL_loader(self,file)      
        except Exception as e:
            print(e)


    def save(self, file):
        """
        - **save the user's experiment in a zip file:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.save(nameFile)  
                      - [save](https://moeabench-rgb.github.io/MoeaBench/experiments/save_experiment/save_experiment/) information about the method, 
                     
        """
        try:
            save.IPL_save(self,file)
        except Exception as e:
            print(e)

    
    def indices(self):
        self.result


    def add_benchmark(self,problem):
        """
        - **Integrates a user benchmark problem implementation in MoeaBench:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.add_benchmark(module)  
                      - [add_benchmark](https://moeabench-rgb.github.io/MoeaBench/implement_benchmark/integration/integration/) information about the method 
                     
        """
        import MoeaBench.benchmarks as bk
        setattr(bk,problem.__name__,problem)


    def add_moea(self,moea):
        """
        - **integrates a user genetic algorithm implementation into MoeaBench:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.add_moea(module)  
                      - [add_moea](https://moeabench-rgb.github.io/MoeaBench/implement_moea/integration/integration/) information about the method 
                     
        """
        import MoeaBench.moeas as algotithm
        setattr(algotithm,moea.__name__,moea)
    


    






    





 

    

    
    


 
        



    
    

    
