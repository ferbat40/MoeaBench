from .IPL_MoeaBench import IPL_MoeaBench 
import numpy as np


class result(IPL_MoeaBench):

    def gen_data(self, gen_all, generations = None):
        return gen_all[-1] if generations is None else gen_all[generations[0]]


    def DATA(self,gen_f_max,generation):
        result.allowed_gen(generation)
        result.allowed_gen_max(len(gen_f_max),generation)        
        return self.gen_data(gen_f_max,generation)