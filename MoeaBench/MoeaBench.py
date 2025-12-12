import inspect
from .analyse_obj import analyse_obj
from .analyse_surface_obj import analyse_surface_obj
from .analyse_metric_gen import analyse_metric_gen
from .I_UserMoeaBench import I_UserMoeaBench
import importlib
from .experiment import experiment
from .stat import stat
from MoeaBench.hypervolume.hypervolume import hypervolume
import numpy as np

class MoeaBench(I_UserMoeaBench):


    @property
    def hypervolume(self):
        return hypervolume()
    
      
    def experiment(self):
        return experiment(self)
    
    
    def stat(self):
        return stat(self)
    

    def __getattr__(self,name):
        if name.startswith("__") and name.endswith("__"):
            return super().__getattribute__(name)
        if name.startswith("_") and name in ["_benchmark","_moea","_result","_pof"]:
           raise AttributeError(name)
        try:
            return importlib.import_module(f"MoeaBench.{name}")
        except ModuleNotFoundError:
            raise AttributeError(name)
    

    def plot_GD(self, *args, generations = [], objectives = []):   
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
         try:     
             analyse_metric_gen.IPL_plot_GD(args, generations, objectives)     
         except Exception as e:
            print(e)


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
         try:     
             analyse_metric_gen.IPL_plot_GDplus(args, generations, objectives)     
         except Exception as e:
            print(e)
    
    
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
         try:     
             analyse_metric_gen.IPL_plot_IGD(args, generations, objectives)     
         except Exception as e:
            print(e)
        

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
         try:     
             analyse_metric_gen.IPL_plot_IGDplus(args, generations, objectives)     
         except Exception as e:
            print(e)
            

    def surfaceplot(self, *args, objectives = []):
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
        try:
            analyse_surface_obj.IPL_plot_3D(args, objectives)   
        except Exception as e:
            print(e)   
        

    def spaceplot(self, *args, objectives = []):
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
      

        try:     
            analyse_obj.IPL_plot_3D(args, objectives)     
        except Exception as e:
            print(e)
        

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
    


    






    





 

    

    
    


 
        



    
    

    
