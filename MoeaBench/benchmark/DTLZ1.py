from MoeaBench.P_DTLZ1 import P_DTLZ1
from MoeaBench.CACHE import CACHE


def DTLZ1(M = 3, K = 5, P = 700):
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
          
        """
        cache = CACHE()
        bk = P_DTLZ1(M, K, P,cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
        return bk