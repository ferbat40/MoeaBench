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
           
        - Notes:
            O valor de N = D+K-1
            Após a execução, o método retornará um objeto contendo todas as 
            funções necessárias
            para geração de pontos referente ao problema.        
        """
        cache = CACHE()
        bk = P_DPF3(M, K, D, P, cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
        return bk