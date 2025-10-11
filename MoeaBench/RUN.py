from .MOEAD_pymoo import MOEADpymoo
from .SPEA_pymoo import SPEAPymoo
from .UNSGA_pymoo import UNSGAPymoo
from .RVEA_pymoo import RVEApymoo
from .NSGA_pymoo import NSGAPymoo
from .I_MOEA import I_MOEA
from .GEN_history import GEN_history


class RUN(I_MOEA):

    def __init__(self,result):
        self.result=result
        self.M_register = {}
    
    
    def register_moea(self):
        def decorator(cls):
            try:
                if not len(self.M_register.values()) == 0:
                     raise MemoryError(f'{len(self.Moea.M_register.values())} implementations where found in memory. Only one execution is allowed')
                name = cls.__name__
                self.M_register[name] = cls
            except Exception as e:
                 print(e)
            return cls
        

        return decorator


    def get_moea(self):
        return next(iter(self.M_register.values())) if len(self.M_register.values()) > 0 else None
    

    def MOEA_execute(self,result,problem = None, name_moea = None): 
            data = result.edit_DATA_conf().get_DATA_MOEA().exec()
            problem = result.edit_DATA_conf().get_problem()
            GEN_Hist = GEN_history(data[3],[value for key,value in data[0].items()][0])
            approx_ideal,approx_nadir,hist_F,n_evals,hist_n = GEN_Hist.evaluate() 
            result.DATA_store([key for key,value in data[0].items()][0],
                              data[1],
                              data[2],
                              [value for key,value in data[0].items()][0],
                              hist_F,
                              hist_n,
                              problem,
                              n_evals)
            

    def my_new_moea(self,problem,population,generations):
        my_moea = self.get_moea()
        self.result.get_DATA_conf().set_DATA_MOEA(my_moea(problem,population,generations),problem)
        return self.result
           

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
      
      



        





    