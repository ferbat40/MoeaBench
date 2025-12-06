from .I_MoeaBench import I_MoeaBench
import numpy as np
from .GEN_hypervolume import GEN_hypervolume
from .GEN_gd import GEN_gd
from .GEN_gdplus import GEN_gdplus
from .GEN_igd import GEN_igd
from .GEN_igdplus import GEN_igdplus


class IPL_MoeaBench(I_MoeaBench):

    def IPL_variables(self):
        raise NotImplementedError("Not implemented")
    

    def DATA(self):
        raise NotImplementedError("Not implemented")


    def axis(self):
        raise NotImplementedError("Not implemented")

   
    def IPL_objectives(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_plot_3D(self):
        raise NotImplementedError("Not implemented")
    
    
    def PLT(self):
        raise NotImplementedError("Not implemented")  
            
    
    def configure(self):
        raise NotImplementedError("Not implemented")
    

    def IPL_GD(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_GDplus(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_IGD(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_IGDplus(self):
        raise NotImplementedError("Not implemented")
      
    
    def IPL_hypervolume(self):
        raise NotImplementedError("Not implemented")
    

    def allowed_gen(self):
        raise NotImplementedError("Not implemented")
    

    def IPL_plot_GD(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_plot_GDplus(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_plot_IGD(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_plot_IGDplus(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_plot_hypervolume(self):
        raise NotImplementedError("Not implemented")
    

    def IPL_loader(self):
        raise NotImplementedError("Not implemented")
    

    def IPL_save(self):
        raise NotImplementedError("Not implemented")
    
    
    def F(self):
        raise NotImplementedError("Not implemented")
    

    def X(self):
        raise NotImplementedError("Not implemented")
    

    def dict_data(self):
        raise NotImplementedError("Not implemented")
    

    def verify(self):
        raise NotImplementedError("Not implemented")
    
    
    @staticmethod
    def slicing_arr(slc,arr):
        return np.hstack([arr[:,i:j]  for i,j in slc])
    

    @staticmethod
    def set_hypervolume(F_GEN,F):
        return [GEN_hypervolume(fgen,f.shape[1],f.min(axis=0),f.max(axis=0)) for fgen,f in zip(F_GEN,F)]
    
    
    @staticmethod
    def set_GD(F_GEN,F):
        return [GEN_gd(fgen,f) for fgen,f in zip(F_GEN,F)]
    

    @staticmethod
    def set_GDplus(F_GEN,F):
        return [GEN_gdplus(fgen,f) for fgen,f in zip(F_GEN,F)]

    
    @staticmethod
    def set_IGD(F_GEN,F):
        return [GEN_igd(fgen,f) for fgen,f in zip(F_GEN,F)]

    
    @staticmethod
    def set_IGD_plus(F_GEN,F):
        return [GEN_igdplus(fgen,f) for fgen,f in zip(F_GEN,F)]
    

    @staticmethod
    def allowed_obj(objective):
        if not isinstance(objective, (list)):
            raise TypeError("Only arrays are allowed in 'objectives'")
        objective_set = list({x for x in objective})
        if not len(objective_set) == len(objective):
            raise ValueError("There are repeated elements for objectives")


    @staticmethod
    def allowed_obj_equal(element, data, experiments, objectives, obj = ('get_M',)):
        list_valid = list(map(lambda o: o.get_M(), filter(lambda o: all(hasattr(o,m) for m in obj), element)))
        if not all(np.array_equal(data.get_M(),arr) for arr in list_valid):
            objs = [f'{experiments[idx]} = {i.get_M()} objectives' for idx, i in enumerate(element, start = 0)]
            raise ValueError (f'{objs} must be equals')   
        less = [i if i > element[0].get_M() else f'obj' for idx, i in enumerate(objectives, start = 0)  ]
        digit = [i for i in less if str(i).isdigit()]
        if digit:
            raise ValueError (f'Objective(s) {less} can´t be greather than {element[0].get_M()}')  
 

    def allowed_DATA(LIST, experiments):             
        for IDATA,exp in zip(LIST,experiments):
            print(exp.__class__.__name__,"  ", len(IDATA.get_arr_DATA()))

        INF = [f'{IDATA.get_description()}' for IDATA in LIST if np.isinf(IDATA).any()] 
        if len(INF) > 0:
            raise ValueError(f'There are matrices with invalid values: '+",".join(f'{i}' for i in INF))
        

    @staticmethod
    def allowed_gen(generations):
        if not isinstance(generations, (list)):
            raise TypeError("Only arrays are allowed in 'generations'")
        if not len(generations) == 2:
            raise TypeError(f"generations = {generations} not be allowed. I is necessary to follow the format: generations = [begin, end]" )
        if not generations[0] <= generations[1]:
            raise TypeError("the initial generation must be smaller than the final generation")
        

    @staticmethod
    def allowed_gen_max(maximum, N):
        if not N <= maximum:
            raise TypeError(f"generations = {N} not be allowed. It must be between 0 and {maximum}" )
      
    
    @staticmethod
    def extract_pareto_result(args,caller):
        experiment = [] 
        data = []
        benk = []
        arr_gen = []
        for i in args:
            for key, val in caller:
                try:
                    if i == val.result:
                        experiment.append(f'{key}.result')
                        arr_gen.append(i.get_elements()[0][0].get_F_GEN())
                        data.append(i.get_elements()[0][0])
                        benk.append(i.get_elements()[0][1])
                    elif i == val.pof:
                        experiment.append(f'{key}.pof')
                        arr_gen.append(i.get_CACHE().get_elements()[0][0].get_F_GEN())
                        data.append(i.get_CACHE().get_elements()[0][0])
                        benk.append(i.get_CACHE().get_elements()[0][1])
                except Exception as e:
                    pass
        return experiment, data, benk, arr_gen





