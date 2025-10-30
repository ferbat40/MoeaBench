from .P_DTLZ1 import P_DTLZ1
from .P_DTLZ2 import P_DTLZ2
from .P_DTLZ3 import P_DTLZ3
from .P_DTLZ4 import P_DTLZ4
from .P_DTLZ5 import P_DTLZ5
from .P_DTLZ6 import P_DTLZ6
from .P_DTLZ7 import P_DTLZ7
from .P_DTLZ8 import P_DTLZ8
from .P_DTLZ9 import P_DTLZ9
from .P_DPF1 import P_DPF1
from .P_DPF2 import P_DPF2
from .P_DPF3 import P_DPF3
from .P_DPF4 import P_DPF4
from .P_DPF5 import P_DPF5
from .CACHE import CACHE
from .I_benchmark import I_benchmark
from .CACHE_bk_user import CACHE_bk_user
import importlib
import os
import sys


class Benchmark(I_benchmark):    

    def __init__(self):
        self.cache=None
        self.M_register = {}


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
        self.cache = CACHE()
        bk = P_DTLZ1(M, K, P,self.cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
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

        self.cache = CACHE()
        bk = P_DTLZ2(M, K, P,self.cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
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
        self.cache = CACHE()
        bk = P_DTLZ3(M, K, P,self.cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
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
        self.cache = CACHE()
        bk =  P_DTLZ4(M, K, P,self.cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
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

        self.cache = CACHE()
        bk = P_DTLZ5(M, K, P,self.cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
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
        self.cache = CACHE()
        bk = P_DTLZ6(M, K, P, self.cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
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
        self.cache=CACHE()
        bk = P_DTLZ7(M, K, P,self.cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
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
        self.cache = CACHE()
        bk = P_DTLZ8(M , N , P, self.cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
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
        self.cache = CACHE()
        bk = P_DTLZ9(M, N, P, self.cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
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
        self.cache = CACHE()
        bk =  P_DPF1(M, K, D, P, self.cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
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
        self.cache = CACHE()
        bk =  P_DPF2(M, K, D, P, self.cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
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
        self.cache = CACHE()
        bk = P_DPF3(M, K, D, P, self.cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
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
        self.cache = CACHE()
        bk = P_DPF4(M, K, D, P, self.cache)
        bk.set_BENCH_conf() 
        bk.POFsamples()
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
        self.cache = CACHE()
        bk = P_DPF5(M, K, D, P, self.cache)
        bk.set_BENCH_conf()
        bk.POFsamples()
        return bk
    

    def my_implemented_benchmark(self, name, m = 3 ,p = 600 ,k = 5):
        #sys.path.append('/content')
        #module_name = f'{name}'
        #module = importlib.import_module(module_name)
        #user_benchmark = getattr(module,name)
        my_benchmark = name(CACHE_bk_user(), m, p, k)
        F = my_benchmark.POFsamples()
        my_benchmark.get_CACHE().DATA_store(my_benchmark.__class__.__name__,'IN POF',my_benchmark.M,my_benchmark.N,my_benchmark.n_ieq_constr,F,my_benchmark.P,my_benchmark.K)
        return my_benchmark
            

    def my_new_benchmark(self):
        try:
            my_benchmark = self.get_benchmark()
            my_bk = my_benchmark(CACHE_bk_user())
            F =  my_bk.POFsamples()
            my_bk.get_CACHE().DATA_store(my_bk.__class__.__name__,'IN POF',my_bk.M,my_bk.N,my_bk.n_ieq_constr,F,my_bk.P,my_bk.K)
            return my_bk
        except Exception as e:
            print(e)
        
    
    def register_benchmark(self):
        def decorator(cls):
            try:
                name = cls.__name__
                if len(self.M_register) > 0:
                     raise MemoryError("There is already an implementation of the user's Benchmark registered")
                self.M_register[name] = cls
            except Exception as e:
                 print(e)
            return cls
        return decorator


    def get_benchmark(self):
        return next(iter(self.M_register.values())) if len(self.M_register.values()) > 0 else None
    


    
    
  
        