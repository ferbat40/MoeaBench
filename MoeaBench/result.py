from .IPL_MoeaBench import IPL_MoeaBench 
import numpy as np


class result(IPL_MoeaBench):

    @staticmethod
    def allowed_gen(generations):
        if generations is not None and not isinstance(generations, (list)):
            raise TypeError("Only arrays are allowed in 'generations'")    
        if generations is not None and not len(generations) == 1:
            raise TypeError(f"generations = {generations} not be allowed. I is necessary to follow the format: generations = [chosen generation]" )
        

    @staticmethod
    def allowed_gen_max(maximum, N):
        if N is not None and not N[0] <= maximum:
            raise TypeError(f"generations = {N} not be allowed. It must be between 0 and {maximum}" )
      

    def gen_data(self, gen_all, generations = None):
        return gen_all[-1] if generations is None else gen_all[generations[0]]


    def DATA(self,gen_f_max,generation):
        result.allowed_gen(generation)
        result.allowed_gen_max(len(gen_f_max),generation)        
        return self.gen_data(gen_f_max,generation)