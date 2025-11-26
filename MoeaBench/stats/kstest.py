from scipy.stats import ks_2samp
from IPython.display import  display
import numpy as np


class kstest:
    
    def __init__(self, *args):
        self.__call__(args)

    
    def allowed_array(self,args):
        results = [False if not (isinstance(i,np.ndarray)) else True for i in args ]
        if False in results:
            raise ValueError("Only arrays are allowed for the metric calculation.")
        if not 0 < len(results) < 3:
            raise ValueError("Only two arrays are allowed for the metric calculation.")


    def __call__(self,args):
        try:
            self.allowed_array(args)
            stat, value = ks_2samp(args[0],args[1])
            display(f'KS stats {stat[0]},  p-value {value[0]}')
        except Exception as e:
            print(e)  
       
    
        
        