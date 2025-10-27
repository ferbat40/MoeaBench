from .IPL_MoeaBench import IPL_MoeaBench
import numpy as np

class RESULT(IPL_MoeaBench):
                   
    def DATA(self,result,generation, objective):
        gen_f_test = [b[0].get_F_GEN() for b in result.get_elements()]
        gen_f_max = max([len(gen)  for gen in gen_f_test])
        generations = [0,gen_f_max] if isinstance(generation, (list)) and len(generation) == 0 else generation
        RESULT.allowed_gen(generations)
        RESULT.allowed_gen_max(gen_f_max,generations[1])
        objectives = [1,2,3] if isinstance(objective, (list)) and  len(objective) == 0 else objective  
        RESULT.allowed_obj(objectives)
             
        gen_f_valid = [b[0].get_F_GEN()[generations[0]:generations[1]] for b in result.get_elements()]
        slicing = [[i-1,i]  for i in objectives]
        F_gen = []
        for i in range(len(gen_f_valid)):
            vet_aux = []
            for z in range(len(gen_f_valid[i])):
                vet_aux.append(RESULT.slicing_arr(slicing,gen_f_valid[i][z]))
            F_gen.append(vet_aux)           
        F = [b[0].get_arr_DATA() for b in result.get_elements()]
        F_slice = [np.hstack( [b[:,i:j]  for i,j in slicing]) for b in F ]        
        return F_gen,F_slice 

    
    
    

 

    
    
    
