from .analyse import analyse
import numpy as np


class analyse_pareto(analyse):

    @staticmethod
    def DATA(i):
        if hasattr(i,'result') and hasattr(i.result,'get_elements'):
            return [z.get_F_GEN()[-1] for b in i.result.get_elements() for z in b if hasattr(z,'get_F_GEN')][0]  
        else:
            return None


    @staticmethod    
    def allowed_DATA(i):
        if hasattr(i,'result') and hasattr(i.result,'get_elements'):
            return True
        elif isinstance(i,np.ndarray) and i.ndim == 2:
            return True
        else:
            return False
        

    @staticmethod
    def allowed_obj_equal(data, benk):   
        arr = [i.shape[1] for i in data]
        if len(set(arr)) > 1:
            objs = [f'{benk[idx]} = {i} objectives' for idx, i in enumerate(arr, start = 0)]  
            raise ValueError (f'{objs} must be equals')   
          

    @staticmethod
    def allowed_obj(objectives, data, benk):
        if not isinstance(objectives, (list)):
            raise TypeError("Only arrays are allowed in 'objectives'")
        if  0 < len(objectives) < 3:
            raise TypeError(f"objectives = {objectives} not be allowed. I is necessary to follow the format: objectives = [obj1, obj2, obj3] " )       
        analyse_pareto.allowed_obj_equal(data, benk)
       
       
         
    

    

    

    


