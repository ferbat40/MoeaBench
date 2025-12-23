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
    def __call__(self, *args, generation = None, reference = []):
        try:
            gen = [-2,-1] if generation is None else [generation-1, generation] 
            objectives = [1,2,3] 
            evaluate, hypervolume_gen, bench = HV.analyse_metric_gen.IPL_hypervolume(args, gen, objectives = objectives, reference = reference)
            return float(hypervolume_gen[0][0])
        except Exception as e:
             print(e)
           

    def trace(self, *args, objectives = [], reference = []):
        try:
            generations = []
            objectives = [1,2,3] if len(objectives) == 0 else objectives
            evaluate, hypervolume_gen, bench = HV.analyse_metric_gen.IPL_hypervolume(args, generations, objectives = objectives, reference = reference)
            return hypervolume_gen[0]
        except Exception as e:
            print(e)
              
    
    def timeplot(self, *args, generations = [], objectives = [], reference = []):
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
            objectives = [1,2,3] if len(objectives) == 0 else objectives
            HV.analyse_metric_gen.IPL_plot_Hypervolume(args,generations, objectives = objectives, reference = reference)
        except Exception as e:
            print(e)
