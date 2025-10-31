
from .I_benchmark import I_benchmark
from .CACHE_bk_user import CACHE_bk_user



class Benchmarkgavan(I_benchmark):    

    def __init__(self):
        self.cache=None
        self.M_register = {}
   
            

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
    


    
    
  
        