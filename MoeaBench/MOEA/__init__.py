
"""     
        - Benchmarks:       
            MoeaBench uses several evolutionary algorithms from the pymoo library.
               ...
               - NSGA-III:
                      - sinxtase:
                      experiment.moea = moeabench.MOEA.NSGA_III(args) 
                      - [NSGA-III](https://moeabench-rgb.github.io/MoeaBench/algorithms/NSGA3/) Information about the algorithm
               ... 
               - U-NSGA-III:
                      - sinxtase:
                      experiment.moea = moeabench.MOEA.U_NSGA_III(args)
                      - [U-NSGA-3](https://moeabench-rgb.github.io/MoeaBench/algorithms/UNSGA3/) detailed information about the problem
                ...
               - SPEA-II:
                      - sinxtase:
                      experiment.moea = moeabench.MOEA.SPEA_II(args) 
                      - [DTLZ3](https://moeabench-rgb.github.io/MoeaBench/algorithms/SPEA2/) detailed information about the problem
               ... 
               - MOEA/D:
                      - sinxtase:
                      experiment.moea = moeabench.MOEA.MOEAD(args) 
                      - [DTLZ4](https://moeabench-rgb.github.io/MoeaBench/algorithms/MOEAD/) detailed information about the problem
                 ... 
               - RVEA:
                      - sinxtase:
                      experiment.moea = moeabench.MOEA.RVEA(args) 
                      - [DTLZ5](https://moeabench-rgb.github.io/MoeaBench/algorithms/RVEA/) detailed information about the problem
                ... 
              
                
                
                """

import os, importlib


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
    