from .result import result
import numpy as np


class result_metric(result):

    def DATA(self,result,generation, objective):
        gen_f_test = [b[0].get_F_GEN() for b in result.get_elements()]
        gen_f_max = max([len(gen)  for gen in gen_f_test])
        generations = [0,gen_f_max] if isinstance(generation, (list)) and len(generation) == 0 else generation
        result_metric.allowed_gen(generations)
        result_metric.allowed_gen_max(gen_f_max,generations[1])
        objectives = [1,2,3] if isinstance(objective, (list)) and  len(objective) == 0 else objective  
        result_metric.allowed_obj(objectives)
             
        gen_f_valid = [b[0].get_F_GEN()[generations[0]:generations[1]] for b in result.get_elements()]
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
    

    def IPL_hypervolume(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        hv_gen = result_metric.set_hypervolume(F_GEN,F)
        hypervolume_gen = np.array([hv.evaluate() for hv in hv_gen]).flatten()
        return hypervolume_gen.reshape(hypervolume_gen.shape[0],1)
            

    def IPL_GD(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        gd_gen = result_metric.set_GD(F_GEN,F)
        GD__gen = np.array([hv.evaluate() for hv in gd_gen]).flatten()
        return GD__gen.reshape(GD__gen.shape[0],1)
    

    def IPL_GDplus(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        gdplus_gen = result_metric.set_GDplus(F_GEN,F)
        GDplus__gen = np.array([hv.evaluate() for hv in gdplus_gen]).flatten()
        return GDplus__gen.reshape(GDplus__gen.shape[0],1)
    

    def IPL_IGD(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        igd_gen = result_metric.set_IGD(F_GEN,F)
        IGD__gen = np.array([hv.evaluate() for hv in igd_gen]).flatten()
        return IGD__gen.reshape(IGD__gen.shape[0],1)
    

    def IPL_IGDplus(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        igdplus_gen = result_metric.set_IGD_plus(F_GEN,F)
        IGDplus__gen = np.array([hv.evaluate() for hv in igdplus_gen]).flatten()
        return IGDplus__gen.reshape(IGDplus__gen.shape[0],1)
    
    
    