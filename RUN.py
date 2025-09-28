from MOEAD_pymoo import MOEADpymoo
from SPEA_pymoo import SPEAPymoo
from UNSGA_pymoo import UNSGAPymoo
from RVEA_pymoo import RVEApymoo
from NSGA_pymoo import NSGAPymoo
from I_MOEA import I_MOEA
from SOLUTION import SOLUTION
from CACHE import CACHE


class RUN(I_MOEA):

    def __init__(self):
        self.CACHE=CACHE()

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
        self.CACHE.SAMPLES_add([key for key,value in data[0].items()][0],
                                    data[1],
                                    data[2],
                                    [value for key,value in data[0].items()][0],
                                    data[4],
                                    data[3],
                                    problem)


    def NSGA3(self,problem, *, population = 100, generations = 300,seed = 1):
        self.DT_CONF=self.CACHE.get_DATA_conf()
        self.DT_CONF.set_DATA_MOEA(NSGAPymoo(problem,population,generations,seed),problem)
             

    def U_NSGA3(self,problem, *, population = 100, generations = 300,seed = 1):
        self.DT_CONF=self.CACHE.get_DATA_conf()
        self.DT_CONF.set_DATA_MOEA(UNSGAPymoo(problem,population,generations,seed),problem)
      

    def SPEA2(self,problem, *,  population = 100, generations = 300,seed = 1):
        self.DT_CONF=self.CACHE.get_DATA_conf()
        self.DT_CONF.set_DATA_MOEA(SPEAPymoo(problem,population,generations,seed),problem)
      
                     
    def MOEAD(self,problem, *, population = 100, generations = 300,seed = 1):
        self.DT_CONF=self.CACHE.get_DATA_conf()
        self.DT_CONF.set_DATA_MOEA(MOEADpymoo(problem,population ,generations,seed),problem)
                 

    def RVEA(self,problem, *, population = 100, generations = 300,seed = 1):
        self.DT_CONF=self.CACHE.get_DATA_conf()
        self.DT_CONF.set_DATA_MOEA(RVEApymoo(problem,population,generations,seed),problem)
      
      



        





    