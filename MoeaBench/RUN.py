from .MOEAD_pymoo import MOEADpymoo
from .SPEA_pymoo import SPEAPymoo
from .UNSGA_pymoo import UNSGAPymoo
from .RVEA_pymoo import RVEApymoo
from .NSGA_pymoo import NSGAPymoo
from .I_MOEA import I_MOEA
from .SOLUTION import SOLUTION



class RUN(I_MOEA):

    def __init__(self,result):
        self.result=result
    

    def runner_MOEA(self,OBJ,method):
        return getattr(OBJ, method)


    def EXTERNAL(self,MOEA,method='exec'):
        obj = vars(MOEA)
        problem = obj['problem']
       

        try:
            runner = self.runner_MOEA(MOEA,method)
            solutions = runner()
            population = MOEA.population
            generations = MOEA.generations
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
      

    def MOEA_execute(self,result):
            data = result.edit_DATA_conf().get_DATA_MOEA().exec()
            problem = result.edit_DATA_conf().get_problem()
            result.DATA_store([key for key,value in data[0].items()][0],
                                    data[1],
                                    data[2],
                                    [value for key,value in data[0].items()][0],
                                    data[4],
                                    data[3],
                                    problem)
       

    def NSGA3(self,problem, *, population = 100, generations = 300,seed = 1):
        self.result.get_DATA_conf().set_DATA_MOEA(NSGAPymoo(problem,population,generations,seed),problem)
        return self.result       


    def U_NSGA3(self,problem, *, population = 100, generations = 300,seed = 1):
         self.result.get_DATA_conf().set_DATA_MOEA(UNSGAPymoo(problem,population,generations,seed),problem)
         return self.result       


    def SPEA2(self,problem, *,  population = 100, generations = 300,seed = 1):
         self.result.get_DATA_conf().set_DATA_MOEA(SPEAPymoo(problem,population,generations,seed),problem)
         return self.result       
    
                     
    def MOEAD(self,problem, *, population = 100, generations = 300,seed = 1):
         self.result.get_DATA_conf().set_DATA_MOEA(MOEADpymoo(problem,population,generations,seed),problem)
         return self.result 
                 

    def RVEA(self,problem, *, population = 100, generations = 300,seed = 1):
         self.result.get_DATA_conf().set_DATA_MOEA(RVEApymoo(problem,population,generations,seed),problem)
         return self.result 
      
      



        





    