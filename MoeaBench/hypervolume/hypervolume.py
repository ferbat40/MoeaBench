from ..result_metric import result_metric
from ..result import result
import numpy as np


class hypervolume(result_metric):
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
             result.allowed_gen(generation)
             gen = -1 if generation is None else generation
         
             if isinstance(args, np.ndarray):
                 result.allowed_gen_max(len(args),generation)
                 return args[gen]
         
             elif isinstance(args, object) and hasattr(args,'result') and hasattr(args.result,'get_elements'):    
                 
                 gen_f_max = [dt.get_F_gen_non_dominate() 
                          for data in args.result.get_elements() 
                          for dt in data 
                          if hasattr(dt,"get_F_gen_non_dominate")][0]
                 
                 result.allowed_gen_max(len(gen_f_max),generation)   
                 
                 return self.IPL_hypervolume(args.result)[gen]
         except Exception as e:
             print(e)
           

    def trace(self, args, objectives = [], reference = []):
        try:
            return self.IPL_hypervolume(args.result, objectives, reference)
        except Exception as e:
            print(e)


    def IPL_hypervolume(self, result, objective = [], reference = [], generation = []):
        F_GEN, F =  self.DATA(result,generation, objective, reference)
        hv_gen = hypervolume.set_hypervolume(F_GEN,F)
        hv = [hv.evaluate().flatten() for hv in hv_gen][0]
        return hv