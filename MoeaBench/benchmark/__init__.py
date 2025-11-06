"""
        - ARG: 
            M (int): número de objetivos do problema:        
            K (int): tamnanho do vetor |XM|, que receberá a influência da função G(XM).
            P (int): números de pontos gerados randomicamente. 
    
        - Default:
            M = 3
            K = 5
            P = 700

        - Exemplo:
            dtlz1 = problem.DTLZ1(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de K deve ser K > 0.
        
        - NOTES:
          - Para informações sobre o método DTLZ1:
          https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/
          [moeabench.benchmark.DTLZ3](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/).
          
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







    