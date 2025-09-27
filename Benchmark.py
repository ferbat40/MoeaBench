from P_DTLZ1 import P_DTLZ1
from P_DTLZ2 import P_DTLZ2
from P_DTLZ3 import P_DTLZ3
from P_DTLZ4 import P_DTLZ4
from P_DTLZ5 import P_DTLZ5
from P_DTLZ6 import P_DTLZ6
from P_DTLZ7 import P_DTLZ7
from P_DTLZ8 import P_DTLZ8
from P_DTLZ9 import P_DTLZ9
from P_DPF1 import P_DPF1
from P_DPF2 import P_DPF2
from P_DPF3 import P_DPF3
from P_DPF4 import P_DPF4
from P_DPF5 import P_DPF5
from ENGINE import ENGINE


class Benchmark:    
    """  
    - Instância:    
      problem = PROBLEM(Engine)  

    - PROBLEM contém implementações de problemas de teste Benchmark.
    - NOTES:
      - Para informações sobre a classe:
      https://evobench.github.io/benchmark/problems/DTLZ1/DTLZ1/  
    """   




    def DTLZ1(self, *, M = 3, K = 5, P = 700):
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
          https://evobench.github.io/benchmark/problems/DTLZ1/DTLZ1/  

        """
        
        bk = P_DTLZ1(ENGINE(), M, K, P)
        bk.set_BENCH_conf() 
        return bk
       

    def DTLZ2(self, *, M = 3, K = 5, P = 700):
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
         https://evobench.github.io/benchmark/problems/DTLZ2/DTLZ2/
   
        """
        bk = P_DTLZ2(ENGINE(), M, K, P)
        bk.set_BENCH_conf() 
        return bk
    

    def DTLZ3(self, *, M = 3, K = 5, P = 700):
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
            dtlz3 = problem.DTLZ3(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de K deve ser K > 0.
        
        - Notes:
            Após a execução, o método retornará um objeto contendo todas as 
            funções necessárias
            para geração de pontos referente ao problema.        
        """
        bk =  P_DTLZ3(ENGINE(), M, K, P)
        bk.set_BENCH_conf() 
        return bk
    

    def DTLZ4(self, *, M = 3, K = 5, P = 700):
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
            dtlz4 = problem.DTLZ4(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de K deve ser K > 0.
        
        - Notes:
            Após a execução, o método retornará um objeto contendo todas as 
            funções necessárias
            para geração de pontos referente ao problema.        
        """
        
        bk =  P_DTLZ4(ENGINE(), M, K, P)
        bk.set_BENCH_conf() 
        return bk
    

    def DTLZ5(self, *, M = 3, K = 5, P = 700):
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
        bk = P_DTLZ5(ENGINE(), M, K, P)
        bk.set_BENCH_conf() 
        return bk
    

    def DTLZ6(self, *, M = 3, K = 5, P = 700):
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
        bk = P_DTLZ6(ENGINE(), M, K, P)
        bk.set_BENCH_conf() 
        return bk
    

    def DTLZ7(self, *, M = 3, K = 5, P = 700):
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
            dtlz7 = problem.DTLZ7(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de K deve ser K > 0.
        
        - Notes:
            Após a execução, o método retornará um objeto contendo todas as 
            funções necessárias
            para geração de pontos referente ao problema.        
        """
        bk = P_DTLZ7(ENGINE(), M, K, P)
        bk.set_BENCH_conf() 
        return bk


    def DTLZ8(self, *, M = 3, N = 10, P = 700):
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
         https://evobench.github.io/benchmark/problems/DTLZ8/DTLZ8/      
        """
        bk = P_DTLZ8(ENGINE(), M , N , P)
        bk.set_BENCH_conf() 
        return bk
      

    def DTLZ9(self, *, M = 3, N = 10, P = 700):
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
        
        - Notes:
            Após a execução, o método retornará um objeto contendo todas as 
            funções necessárias
            para geração de pontos referente ao problema.        
        """
        bk = P_DTLZ9(ENGINE(), M, N, P)
        bk.set_BENCH_conf() 
        return bk
    

    def DPF1(self, *, M = 3, K = 5, D = 2, P = 700):
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
            dpf1 = problem.DPF1(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de M deve ser M < N.
           
        - Notes:
            O valor de N = D+K-1
            Após a execução, o método retornará um objeto contendo todas as 
            funções necessárias
            para geração de pontos referente ao problema.        
        """
        bk =  P_DPF1(ENGINE(), M, K, D, P)
        bk.set_BENCH_conf() 
        return bk
    

    def DPF2(self, *, M = 3, K = 5, D = 2, P = 700):
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
            dpf2 = problem.DPF2(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de M deve ser M < N.
           
        - Notes:
            O valor de N = D+K-1
            Após a execução, o método retornará um objeto contendo todas as 
            funções necessárias
            para geração de pontos referente ao problema.        
        """
        bk =  P_DPF2(ENGINE(), M, K, D, P)
        bk.set_BENCH_conf() 
        return bk
    

    def DPF3(self, *, M = 3, K = 5, D = 2, P = 700):
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
        bk = P_DPF3(ENGINE(), M, K, D, P)
        bk.set_BENCH_conf() 
        return bk
    

    def DPF4(self, *, M = 3, K = 5, D = 2, P = 700):
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
            dpf4 = problem.DPF4(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de M deve ser M < N.
           
        - Notes:
            O valor de N = D+K-1
            Após a execução, o método retornará um objeto contendo todas as 
            funções necessárias
            para geração de pontos referente ao problema.        
        """
        bk = P_DPF4(ENGINE(), M, K, D, P)
        bk.set_BENCH_conf() 
        return bk
    

    def DPF5(self, *, M = 3, K = 5, D = 2, P = 700):
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
            dpf5= problem.DPF5(problem)

        - Exception:                
            O valor de M deve ser M > 2.
            O valor de M deve ser M < N.
           
        - NOTES:
         - Para obter informações detalhadas sobre a método:
         https://evobench.github.io/benchmark/problems/DPF5/DPF5/
        """
        bk = P_DPF5(ENGINE(), M, K, D, P)
        bk.set_BENCH_conf()
        return bk


    
    
  
        