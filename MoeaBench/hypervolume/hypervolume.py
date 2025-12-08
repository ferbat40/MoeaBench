from ..result_metric import result_metric


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
    

    def __call__(self, args, generations = [], objective = [], reference = []):
        try:
            return self.IPL_hypervolume(args.result, generations, objective, reference)[-1]
        except Exception as e:
            print(e)


    def trace(self, args, generations = [], objective = [], reference = []):
        try:
            return self.IPL_hypervolume(args.result, generations, objective, reference)
        except Exception as e:
            print(e)


    def IPL_hypervolume(self, result, generation, objective, reference):
        F_GEN, F =  self.DATA(result,generation, objective)
        hv_gen = hypervolume.set_hypervolume(F_GEN,F)
        hv = [hv.evaluate().flatten() for hv in hv_gen][0]
        return hv