from .IPL_MoeaBench import IPL_MoeaBench
import numpy as np
from itertools import zip_longest

class analyse(IPL_MoeaBench):

    @staticmethod
    def normalize_gen(data,generations,metric):
        vet=[]
        for i in data:
            vet.append(i.get_METRIC_gen().get_arr_Metric_gen()[metric][generations[0]:generations[1]+1])
        max = 0
        for row in zip_longest(*vet,fillvalue=np.nan):
            for i in row:
                try:
                    if i.shape[0]> max:
                        max=i.shape[0]
                except Exception as e:
                    continue

        vet_pt=[]
        for row in zip_longest(*vet,fillvalue=np.nan):
            vet_aux=[]
            for i in row:
                try:
                    if i.shape[0]<max:
                        pad = np.full((max-i.shape[0],i.shape[1]), np.nan)
                        arr = np.vstack([i,pad])
                        vet_aux.append(arr)
                    else:
                        vet_aux.append(i)   

                except Exception as e:
                    pad = np.full((max,3), np.nan)
                    vet_aux.append(pad)     
            vet_pt.append(vet_aux)   
        return vet_pt       


