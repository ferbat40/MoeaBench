from .IPL_MoeaBench import IPL_MoeaBench
import numpy as np

class RESULT(IPL_MoeaBench):
            
    def allowed_obj(self,result, mtc, I):
        max = result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[mtc][0].shape[1]
        if not I <= max:
            raise TypeError(f"objectives = {I} not be allowed. It must be between 0 and {max}" )
             

    def DATA(self,result,N,idx):
        return np.array([i for i in result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[idx][0:N]])
    
   

    
    
    

 

    
    
    
