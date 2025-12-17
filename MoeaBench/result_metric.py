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
 

    @staticmethod
    def DATA(result,generation, objective):
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
    

    @staticmethod
    def IPL_hypervolume(result, generation = []):
        objective = [1,2,3]
        F_GEN, F =  result_metric.DATA(result,generation, objective)
        metric = result_metric.set_hypervolume(F_GEN, F, np.min(F[0], axis = 0), np.max(F[0], axis = 0))
        metric_evaluate = metric[0].evaluate()
        return [float(i)  for i in metric_evaluate]
            
    
    @staticmethod
    def IPL_GD(result, generation, objective):
        F_GEN, F =  result_metric.DATA(result,generation, objective)
        metric = result_metric.set_GD(F_GEN,F)
        metric_evaluate = metric[0].evaluate()
        return [float(i)  for i in metric_evaluate]
    
    
    @staticmethod
    def IPL_GDplus(result, generation, objective):
        F_GEN, F =  result_metric.DATA(result,generation, objective)
        metric = result_metric.set_GDplus(F_GEN,F)
        metric_evaluate = metric[0].evaluate()
        return [float(i)  for i in metric_evaluate]
    
    
    @staticmethod
    def IPL_IGD(result, generation, objective):
        F_GEN, F = result_metric.DATA(result,generation, objective)
        metric = result_metric.set_IGD(F_GEN,F)
        metric_evaluate = metric[0].evaluate()
        return [float(i)  for i in metric_evaluate]
    
    
    @staticmethod
    def IPL_IGDplus(result, generation, objective):
        F_GEN, F =  result_metric.DATA(result,generation, objective)
        metric = result_metric.set_IGD_plus(F_GEN,F)
        metric_evaluate = metric[0].evaluate()
        return [float(i)  for i in metric_evaluate]
    
    
    