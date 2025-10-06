from .IPL_MoeaBench import IPL_MoeaBench
import numpy as np

class RESULT(IPL_MoeaBench):

    def DATA(self,result,N,idx):
        return np.array([i for i in result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[idx][0:N]])
    
    

 

    
    
    
