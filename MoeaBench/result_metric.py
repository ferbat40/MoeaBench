from .result import result
from .IPL_MoeaBench import IPL_MoeaBench
import numpy as np


class result_metric(IPL_MoeaBench):

    @staticmethod
    def allowed_obj(objective,result):
        M = result.get_elements()[0][1].get_M()
        IPL_MoeaBench.allowed_obj(objective)
        less = [i if i > M else f'obj' for idx, i in enumerate(objective, start = 0)  ]
        digit = [i for i in less if str(i).isdigit()]
        if digit:
            raise ValueError (f'Objective(s) {less} can´t be greather than {M}')  
 

    def DATA(self,result,generation, objective, reference = []):
        gen_f_test = [b[0].get_F_gen_non_dominate() for b in result.get_elements()]
        gen_f_max = max([len(gen)  for gen in gen_f_test])
        generations = [0,gen_f_max] if isinstance(generation, (list)) and len(generation) == 0 else generation
        result_metric.allowed_gen(generations)
        result_metric.allowed_gen_max(gen_f_max,generations[1])
        objectives = [1,2,3] if isinstance(objective, (list)) and  len(objective) == 0 else objective  
        result_metric.allowed_obj(objectives,result)
             
        gen_f_valid = [b[0].get_F_gen_non_dominate()[generations[0]:generations[1]] for b in result.get_elements()]
        slicing = [[i-1,i]  for i in objectives]
        F_gen = []
        for i in range(len(gen_f_valid)):
            vet_aux = []
            for z in range(len(gen_f_valid[i])):
                vet_aux.append(result_metric.slicing_arr(slicing,gen_f_valid[i][z]))
            F_gen.append(vet_aux)           
        F = [b[0].get_arr_DATA() for b in result.get_elements()]
        F_slice = [np.hstack( [b[:,i:j]  for i,j in slicing]) for b in F ]        
        return F_gen,F_slice 
            

    def IPL_GD(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        gd_gen = result_metric.set_GD(F_GEN,F)
        return [float(gd.evaluate().flatten()) for gd in gd_gen][0]
    

    def IPL_GDplus(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        gdplus_gen = result_metric.set_GDplus(F_GEN,F)
        return [float(gdplus.evaluate().flatten()) for gdplus in gdplus_gen][0]
    

    def IPL_IGD(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        igd_gen = result_metric.set_IGD(F_GEN,F)
        return [float(igd.evaluate().flatten()) for igd in igd_gen][0]
    

    def IPL_IGDplus(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        igdplus_gen = result_metric.set_IGD_plus(F_GEN,F)
        return [float(igdplus.evaluate().flatten()) for igdplus in igdplus_gen][0]
    
    
    