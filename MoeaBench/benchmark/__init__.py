"""     
        - Benchmarks:       
            MoeaBench has implementations of several benchmark problems. 
            Click on the link for the respective benchmark problem of each experiment to 
            obtain more information about the problem and Pareto optimal front simulation.
            - DTLZ1:
              - sinxtase:
              experiment.problem = moeabench.benchmark.DTLZ1(args) 
              - [DTLZ1](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/) detailed information about the problem
              - ([args](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/#arguments)) detailed information on the parameters that can be passed for custom 
              configuration of the benchmark problem, see the parameters that can be passed. 
              - [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/) information on possible error types
          
"""
import os, importlib
import MoeaBench.benchmark.my_new_benchmark as m_bk

_dir = os.path.dirname(__file__)


for root, dirs , files in os.walk(_dir):
    for fl in files:
        if fl.endswith(".py") and fl not in ("__init__.py",):
            path  = os.path.relpath(os.path.join(root,fl),_dir)
            name_module = path.replace(os.sep,".")[:-3]
            module = importlib.import_module(f'{__name__}.{name_module}')
            cls_name = fl[:-3]

           
            globals()[cls_name] = getattr(module, cls_name)
my_module_cache = importlib.import_module("MoeaBench.CACHE")
globals()['CACHE'] = my_module_cache.CACHE
my_module_cache = importlib.import_module("MoeaBench.CACHE_bk_user")
globals()['CACHE_bk_user'] = my_module_cache.CACHE_bk_user
globals()['register_benchmark'] = m_bk.register_benchmark







    