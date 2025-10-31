from MoeaBench.P_DTLZ2 import P_DTLZ2
from MoeaBench.CACHE import CACHE


def DTLZ2(M = 3, K = 5, P = 700):
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
            dtlz2 = problem.DTLZ2(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de K deve ser K > 0.
        
        - NOTES:
         - Para obter informações detalhadas sobre a método:
         https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ2/DTLZ2/
   
        """

        cache = CACHE()
        bk = P_DTLZ2(M, K, P, cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
        return bk