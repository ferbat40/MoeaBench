from .MoeaBench import MoeaBench

class _MoeaBenchWrapper:
    """     
        - Description:        
            MoeaBench is a framework for experimentation, analysis, and 
            development of benchmark problems for validating the performance     
            of genetic algorithms.
               ...
               - genetic algorithms:
                      - sinxtase:
                      moeabench.MOEA
                      - [NSGA-III](https://moeabench-rgb.github.io/MoeaBench/algorithms/NSGA3/) information about the genetic algorithm
                      - [U-NSGA-3](https://moeabench-rgb.github.io/MoeaBench/algorithms/UNSGA3/) information about the genetic algorithm
 
                ... 
                 - benchmark problems:
                      - sinxtase:
                      moeabench.benchmark
                      - [NSGA-III](https://moeabench-rgb.github.io/MoeaBench/algorithms/NSGA3/) information about the genetic algorithm
                      - [U-NSGA-3](https://moeabench-rgb.github.io/MoeaBench/algorithms/UNSGA3/) information about the genetic algorithm
                ...
              
              
"""





    
    def __getattr__(self, name):
        inst = MoeaBench()
        return getattr(inst, name)

    def __call__(self, *args, **kwargs):
        return MoeaBench(*args,  **kwargs)
    
    def help(self):
        print(self.__class__.__doc__)

moeabench = _MoeaBenchWrapper()
