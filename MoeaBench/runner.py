from .I_MOEA import I_MOEA
from .GEN_history import GEN_history
from .CACHE import CACHE


class runner(I_MOEA):

    def __init__(self):
        self.result=CACHE()
        self.M_register = {}


    def get_history(self,history,F):
         return GEN_history(history,F)
    
    
    def register_moea(self):
        def decorator(cls):
            try:
                name = cls.__name__
                if len(self.M_register) > 0:
                     raise MemoryError("There is already an implementation of the user's MOEA registered")
                self.M_register[name] = cls
            except Exception as e:
                 print(e)
            return cls
        return decorator


    def get_moea(self):
        return next(iter(self.M_register.values())) if len(self.M_register.values()) > 0 else None
        

    def my_new_moea(self,problem,population,generations):
        try:
             my_moea = self.get_moea()
             self.result.get_DATA_conf().set_DATA_MOEA(my_moea(problem,population,generations),problem)
             return self.result
        except Exception as e:
             print(e)

    

       
           
    

    
   
    
                     
  
