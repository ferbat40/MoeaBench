from ..result_metric import result_metric
from ..result_population import result_population
import numpy as np
import inspect
from ..import MoeaBench as HV


class hypervolume:
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
   

    def __call__(self, args, generation = None):
         try:
             result_population.allowed_gen(generation)
             gen = -1 if generation is None else generation
         
             if isinstance(args, np.ndarray):
                 result_population.allowed_gen_max(len(args),generation)
                 return args[gen]
         
             elif isinstance(args, object) and hasattr(args,'result') and hasattr(args.result,'get_elements'):    
                 
                 gen_f_max = [dt.get_F_gen_non_dominate() 
                          for data in args.result.get_elements() 
                          for dt in data 
                          if hasattr(dt,"get_F_gen_non_dominate")][0]
                 
                 result_population.allowed_gen_max(len(gen_f_max),generation)   
                 
                 return result_metric.IPL_hypervolume(args.result)[gen]
         except Exception as e:
             print(e)
           

    def trace(self, args, objectives = [], reference = []):
        try:
            return result_metric.IPL_hypervolume(args.result, objectives, reference)
        except Exception as e:
            print(e)
              
    
    def timeplot(self,*args, generations = [], objectives = [], reference = []):
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
        try:
            HV.analyse_metric_gen.IPL_plot_Hypervolume(args,generations, objectives = objectives, reference = reference)
        except Exception as e:
            print(e)

   