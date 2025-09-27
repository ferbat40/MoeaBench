from MOEAD_pymoo import MOEADpymoo
from SPEA_pymoo import SPEAPymoo
from UNSGA_pymoo import UNSGAPymoo
from RVEA_pymoo import RVEApymoo
from NSGA_pymoo import NSGAPymoo
from I_MOEA import I_MOEA
from SOLUTION import SOLUTION
import inspect

class RUN:
    """  
    - Instância:    
      runner = RUN()  
    - RUN esta dividida em 2 partes:
      - Parte 1: Geração de arquivos com extensão .XLSX, através da Execução de MOEAs 
      importados e configurados da biblioteca Puymoo.
              - runner.NSGA3(args)
              - runner.UNSGA3(args)
              - runner.SPEA2(args)    
              - runner.MOEAD(args)
              - runner.RVEA(args)  
      - Parte 2: Geração de arquivos com extensão .XLSX, com MOEAs externos implementados
      pelo usuário.
              - runner.SAVE(args)
    """   

    def MOEA_allowed(self,MOEA):
        method = I_MOEA.__abstractmethods__
        for mt in method:
           if not hasattr(self,mt) and not hasattr(MOEA,mt):
               raise NotImplementedError(f'No {mt} method implememnted')
           I_MOEA.register(MOEA)


    def runner_MOEA(self,OBJ,method):
        return getattr(OBJ, method)


    def EXTERNAL(self,MOEA,method='exec'):
        obj = vars(MOEA)
        problem = obj['problem']
        """
          Args: 
              problem (PROBLEM): instancia da classe PROBLEM, que executa um dos seus métodos:
                  DTLZ1,DTLZ2,DTLZ3,DTLZ4,DTLZ5,DTLZ6,DTLZ7,DTLZ8,DTLZ9,
                  DPF1,DPF2.DPF3,DPF4,DPF5.

                  
              MOEA (object): Instância da classe que implementa algum algoritimo evolutivo, definido pelo usuário.
                  A classe definida pelo usuário precisa conter a seguinte assinatura:
                      nomedaclasse(PROBLEM, generations, populatoin)
                  E implementar um método 'exec' (nome opcional). O método retornar uma list contendo:
                  8 arrays, que devem ter 2 dimensões cada uma. Para arrays que o usuário não fornecer, usar o formato:[0].

                  
              method (Optional[callable[[PROBLEM], int, int], list]]): Nome da função que será executada dentro do método.
                  Caso não seja fornecido por parametro, o nome padrão será 'exec'. A função deverá retornar uma List, com
                  o mesmo formato descrito acima.              

                  
          Raises:
              Exception: Os dados necessarios serão extraidos dos objetos enviados por parametro, 
                   Qualquer inconsistencia das informações enviadas, será enviada uma mensagem de erro personalizada ao usuário.

                   
          Notes:
              Após passar por validações, será criado um arquivo .XLSX para ser utilizado pelas fereamentas de análise 
              de dados do Evobench
                    
        """

        try:
            self.MOEA_allowed(SOLUTION)
            runner = self.runner_MOEA(MOEA,method)
            solutions = runner()
            population = MOEA.population
            generations=MOEA.generations
            description=MOEA.__class__.__name__
            M=problem.get_ENGINE().get_BENCH_CI().get_M()
            D=problem.get_ENGINE().get_BENCH_CI().get_D()
            K=problem.get_ENGINE().get_BENCH_CI().get_K()
            N=problem.get_ENGINE().get_BENCH_CI().get_Nvar()
            Benckmark=str(problem.__class__.__name__).split('_')[1]
            solver_solution = SOLUTION()
            solver_solution.SOLVER(problem,Benckmark,M,D,K,N,description,solutions,generations,population)
        except Exception as e:
            print(e)
      

    def MOEA_execute(self,MOEA,problem):
        data = MOEA.exec()
        problem.get_ENGINE().SAMPLES_add([key for key,value in data[0].items()][0],
                                    data[1],
                                    data[2],
                                    [value for key,value in data[0].items()][0],
                                    data[4],
                                    data[3])
        
          
    def NSGA3(self,problem, *, population = 100, generations = 300,seed = 1):
        try:
            self.MOEA_allowed(NSGAPymoo)  
            try:
                self.MOEA_execute(NSGAPymoo(problem,population,generations,seed),problem)
            except Exception as e:
                pass
                print(e)
        except Exception as e:
            print(e)
       

    def U_NSGA3(self,problem, *, population = 100, generations = 300,seed = 1):
        try:
            self.MOEA_allowed(UNSGAPymoo)
            try:
                self.MOEA_execute(UNSGAPymoo(problem,population,generations,seed),problem)
            except Exception as e:
                pass
        except Exception as e:
            print(e)
           

    def SPEA2(self,problem, *,  population = 100, generations = 300,seed = 1):
        try:
            self.MOEA_allowed(SPEAPymoo)
            try:
                self.MOEA_execute(SPEAPymoo(problem,population,generations,seed),problem)
            except Exception as e:
                pass
        except Exception as e:
            print(e)
                     

    def MOEAD(self,problem, *, population = 100, generations = 300,seed = 1):
        try:
            self.MOEA_allowed(MOEADpymoo)
            try:
                self.MOEA_execute(MOEADpymoo(problem,population ,generations,seed),problem)
            except Exception as e:
                pass
        except Exception as e:
            print(e)
               

    def RVEA(self,problem, *, population = 100, generations = 300,seed = 1):
        try:
            self.MOEA_allowed(RVEApymoo)
            try:
                self.MOEA_execute(RVEApymoo(problem,population,generations,seed),problem)
            except Exception as e:
                pass
        except Exception as e:
            print(e)



        





    