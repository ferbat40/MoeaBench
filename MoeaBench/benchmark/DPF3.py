from MoeaBench.P_DPF3 import P_DPF3
from MoeaBench.CACHE import CACHE


def DPF3(M = 3, K = 5, D = 2, P = 700):
        """
        - ARG: 
            M (int): número de objetivos do problema:        
            N (int): número de variáveis de decisão.
            P (int): números de pontos gerados randomicamente. 
             
        - Default:
            M = 3
            K = 5
            D = 2
            P = 700

        - Exemplo:
            dpf3 = problem.DPF3problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de M deve ser M < N.
           
        - NOTES:
         - Para obter informações detalhadas sobre a método:
         https://moeabench-rgb.github.io/MoeaBench/problems/DPF3/DPF3/        
        """
        cache = CACHE()
        bk = P_DPF3(M, K, D, P, cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
        return bk