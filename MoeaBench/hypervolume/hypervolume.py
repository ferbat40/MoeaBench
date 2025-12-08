from ..result_metric import result_metric
from ..result import result
import numpy as np
from ..plot_gen import plot_gen
import inspect


class hypervolume(result_metric,plot_gen):
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

    
    def timeplot(self,*args, generations = [], objectives = [], reference = []):
        caller = inspect.currentframe().f_back.f_locals.items()
        experiment, data, benk, arr = hypervolume.extract_pareto_result(args,caller)   
        hypervolume.IPL_plot_Hypervolume(args,generations,experiments = experiment, objectives = objectives, reference = reference, bench = benk)




    @staticmethod
    def IPL_plot_Hypervolume(args,generations, experiments, objectives, reference, bench):
        print("squi")
        #try:
            #evaluate,F_GEN,F = hypervolume.DATA(args,generations , objectives, experiments, reference, bench)
           # hv_gen = hypervolume.set_hypervolume(F_GEN,F)
            #hypervolume_gen = [hv.evaluate() for hv in hv_gen]
            #plot_g = hypervolume([evaluate,hypervolume_gen],experiments,metric = ['Hypervolume','Generations'])
           # plot_g.configure()
        #except Exception as e:
           #print(e)


    def IPL_hypervolume(self, result, objective = [], reference = [], generation = []):
        F_GEN, F =  self.DATA(result,generation, objective)
        min_non = []
        max_non = []

        if not isinstance(reference,list):
                raise TypeError("Only arrays are allowed in 'references'")
        
        if len(reference) > 0:  
            min_non, max_non = hypervolume.normalize(reference)
        min_slice = [float(min_non[i-1]) for i in objective] if len(min_non) > 0 else np.min(F[0], axis = 0)
        max_slice = [float(max_non[i-1]) for i in objective] if len(max_non) > 0 else np.max(F[0], axis = 0)
        hv_gen = hypervolume.set_hypervolume(F_GEN, F, min_slice, max_slice)
        hv = [hv.evaluate().flatten() for hv in hv_gen][0]
        return hv