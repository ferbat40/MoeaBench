from .MoeaBench import MoeaBench

class _MoeaBenchWrapper:
    """
- Benchmarks:
    MoeaBench uses several evolutionary algorithms from the pymoo library.
    ...
    - NSGA-III:
        - sintaxe:
          experiment.moea = moeabench.MOEA.NSGA_III(args)
        - [NSGA-III](https://moeabench-rgb.github.io/MoeaBench/algorithms/NSGA3/) information about the genetic algorithm
    ...
    - U-NSGA-III:
        - sintaxe:
          experiment.moea = moeabench.MOEA.U_NSGA_III(args)
        - [U-NSGA-3](https://moeabench-rgb.github.io/MoeaBench/algorithms/UNSGA3/) information about the genetic algorithm
    ...
    - SPEA-II:
        - sintaxe:
          experiment.moea = moeabench.MOEA.SPEA_II(args)
        - [SPEA-II](https://moeabench-rgb.github.io/MoeaBench/algorithms/SPEA2/) information about the genetic algorithm
    ...
    - MOEA/D:
        - sintaxe:
          experiment.moea = moeabench.MOEA.MOEAD(args)
        - [MOEA/D](https://moeabench-rgb.github.io/MoeaBench/algorithms/MOEAD/) information about the genetic algorithm
    ...
    - RVEA:
        - sintaxe:
          experiment.moea = moeabench.MOEA.RVEA(args)
        - [RVEA](https://moeabench-rgb.github.io/MoeaBench/algorithms/RVEA/) information about the genetic algorithm
    ...
    - my_new_moea:
        - sintaxe:
          experiment.moea = moeabench.MOEA.my_new_moea(args)
        - [my_new_moea](https://moeabench-rgb.github.io/MoeaBench/implement_moea/memory/memory/) information about the method
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
