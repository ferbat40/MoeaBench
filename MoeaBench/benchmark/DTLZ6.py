from MoeaBench.P_DTLZ6 import P_DTLZ6
from MoeaBench.CACHE import CACHE


def DTLZ6(M = 3, K = 5, P = 700):
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
            dtlz6 = problem.DTLZ6(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de K deve ser K > 0.
        
        - Notes:
            Após a execução, o método retornará um objeto contendo todas as 
            funções necessárias
            para geração de pontos referente ao problema.        
        """
        cache = CACHE()
        bk = P_DTLZ6(M, K, P, cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
        return bk