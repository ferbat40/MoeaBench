from .analyse import analyse
from itertools import zip_longest
import numpy as np


class analyse_gen(analyse):
 
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
    

