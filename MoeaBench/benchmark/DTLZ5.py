from MoeaBench.P_DTLZ5 import P_DTLZ5
from MoeaBench.CACHE import CACHE


def DTLZ5(M = 3, K = 5, P = 700):
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
            dtlz5 = problem.DTLZ5(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de K deve ser K > 0.
        
        - Notes:
            Após a execução, o método retornará um objeto contendo todas as 
            funções necessárias
            para geração de pontos referente ao problema.        
        """

        cache = CACHE()
        bk = P_DTLZ5(M, K, P, cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
        return bk