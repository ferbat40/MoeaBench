from .MoeaBench import MoeaBench

class _MoeaBenchWrapper:
    """
        - ARG: 
            M (int): número de objetivos do problema:        
            N (int): número de variáveis de decisão.
            P (int): números de pontos gerados randomicamente. 
             
        - Default
            M = 3
            K = 5
            D = 2
            P = 700

        - Exemplo:
            dpf5= problem.DPF5(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de M deve ser M < N.
           
        - NOTES:
         - Para obter informações detalhadas sobre a método:
         https://evobench.github.io/benchmark/problems/DPF5/DPF5/
    """

    
    
    def __getattr__(self, name):
        inst = MoeaBench()
        return getattr(inst, name)

    def __call__(self, *args, **kwargs):
        return MoeaBench(*args,  **kwargs)

moeabench = _MoeaBenchWrapper()