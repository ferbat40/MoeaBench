from .problems import problems


@staticmethod
def DTLZ8(M = 3, N = 10, P = 700):
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
            dtlz8 = problem.DTLZ8(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de K deve ser N >= 5.
        
        - NOTES:
         - Para obter informações detalhadas sobre a método:
         https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ8/DTLZ8/       
        """
        problem = problems(DTLZ8.__name__)
        bk = problem.get_problem(M , N , P)
        bk.set_BENCH_conf() 
        bk.POFsamples()
        return bk