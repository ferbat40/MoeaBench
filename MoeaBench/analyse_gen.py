from .analyse import analyse
from itertools import zip_longest
import numpy as np


class analyse_gen(analyse):

    @staticmethod
    def allowed_obj(data,objective):
        if not isinstance(objective, (int)):
            raise TypeError("Only int are allowed in 'objectives'")
        min=0
        for i in data:
          min = i.get_arr_DATA().shape[1] if i.get_arr_DATA().shape[1] < min or min == 0  else min
        if  objective > min:
            raise ValueError (f'Objective {objective} can´t be greather than {min}') 
    
 
    @staticmethod
    def allowed_gen_max(result, mtc, N):
        N = len(result.gret_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[mtc])  if N is None  else N
        vmax = max(len(arr.get_METRIC_gen().get_arr_Metric_gen()[mtc]) for arr in result)
        if not N <= vmax:
            raise TypeError(f"generations = {N} not be allowed. It must be between 0 and {vmax}" )
  

    @staticmethod
    def allowed_gen(generations):
        if not isinstance(generations, (list)):
            raise TypeError("Only arrays are allowed in 'generations'")
        if not len(generations) == 2:
            raise TypeError(f"generations = {generations} not be allowed. I is necessary to follow the format: generations = [begin, end]" )
        if not generations[0] <= generations[1]:
            raise TypeError("the initial generation must be smaller than the final generation")
    

    @staticmethod
    def normalize_gen(data,generations,metric,objective):   
        print("metric ",metric)
        vet = [i.get_METRIC_gen().get_arr_Metric_gen()[metric] for i in data]
        vet_pt=[row for row in zip_longest(*vet,fillvalue=np.nan)]
        max_col = max([arr.shape[0] if isinstance(arr, np.ndarray) 
                       else np.nan for pts in vet_pt  for  arr in pts])
     
        moea=[]
        gen=[]
        for pts in vet_pt:
           moea=[]
           for  arr in pts:            
               if not isinstance(arr, (np.ndarray)):
                   moea.append(np.full( (max_col,1), np.nan))
               elif isinstance(arr, (np.ndarray)):
                   moea.append(np.vstack( (arr[:,objective-1:objective], np.full( (max_col-arr.shape[0],1), np.nan)) ))
           gen.append(moea)       
        return gen[generations[0]:generations[1]+1]
    

