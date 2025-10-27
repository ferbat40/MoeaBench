from .RESULT import RESULT
import numpy as np

class result_obj_var(RESULT):

    def F(self,result, generations = None):
        return [b[0].get_F_GEN() for b in result.get_elements()] if generations is None else [b[0].get_F_GEN()[generations[0]:generations[1]] for b in result.get_elements()]

    
    def X(self,result, generations = None):
        return [b[0].get_X_GEN() for b in result.get_elements()] if generations is None else [b[0].get_X_GEN()[generations[0]:generations[1]] for b in result.get_elements()]


    def dict_data(self):
        return {0: self.F, 1: self.X}


    def DATA(self,result,generation, objective, default = 0):
        gen_f_test = self.dict_data()[default](result)
        gen_f_max = max([len(gen)  for gen in gen_f_test])
        generations = [0,gen_f_max] if isinstance(generation, (list)) and len(generation) == 0 else generation
        RESULT.allowed_gen(generations)
        RESULT.allowed_gen_max(gen_f_max,generations[1])        
        gen_f_valid = self.dict_data()[default](result,generations)
        slicing = [[objective-1,objective]]
        F_gen = []
        for i in range(len(gen_f_valid)):
            vet_aux = []
            for z in range(len(gen_f_valid[i])):
                vet_aux.append(RESULT.slicing_arr(slicing,gen_f_valid[i][z]))
            F_gen.append(vet_aux)                   
        return F_gen 