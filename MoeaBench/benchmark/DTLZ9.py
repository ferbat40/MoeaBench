from MoeaBench.P_DTLZ9 import P_DTLZ9
from MoeaBench.CACHE import CACHE


def DTLZ9(M = 3, N = 10, P = 700):
        """
        - ARG: 
            M (int): número de objetivos do problema:        
            N (int): número de variáveis de decisão.
            P (int): números de pontos gerados randomicamente. 
             
        - Default:
            M = 3
            N = 10
            P = 700

        - Exemplo:
            dtlz9 = problem.DTLZ9(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de K deve ser N >= 5.
        
         - NOTES:
         - Para obter informações detalhadas sobre a método:
         https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ9/DTLZ9/    
        """
        cache = CACHE()
        bk = P_DTLZ9(M, N, P, cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
        return bk