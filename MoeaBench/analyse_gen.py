from .analyse import analyse
from itertools import zip_longest
import numpy as np


class analyse_gen(analyse):

    @staticmethod
    def allowed_obj(element,data,experiments,objective):
        if not isinstance(objective, (list)):
            raise TypeError("Only arrays are allowed in 'objectives'")
        objective_set = list({x for x in objective})
        if not len(objective_set) == len(objective):
            raise ValueError("There are repeated elements for objectives")
        analyse_gen.allowed_obj_equal(element, data, experiments, objective)
    
 
    @staticmethod
    def allowed_gen_max(maximum, N):
        if not N <= maximum:
            raise TypeError(f"generations = {N} not be allowed. It must be between 0 and {maximum}" )
    


    

