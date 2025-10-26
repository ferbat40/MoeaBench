from .analyse import analyse
import numpy as np


class analyse_pareto(analyse):
    
    @staticmethod
    def allowed_obj(element,data, experiments, objectives, obj = ('get_M',)):
        if not isinstance(objectives, (list)):
            raise TypeError("Only arrays are allowed in 'objectives'")
        if  0 < len(objectives) < 3:
            raise TypeError(f"objectives = {objectives} not be allowed. I is necessary to follow the format: objectives = [obj1, obj2, obj3] " )
       
        
        analyse_pareto.allowed_obj_equal(element, data, experiments, objectives)
       
       
         
    

    

    

    


