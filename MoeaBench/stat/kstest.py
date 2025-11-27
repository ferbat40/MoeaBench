from scipy.stats import ks_2samp
from IPython.display import  display
import numpy as np


class kstest:
    
    def __init__(self, *args):
        self.args = args

    
    def allowed_array(self,args):
        results = [False if not (isinstance(i[-1],np.ndarray)) else True for i in args ]
        if False in results:
            raise ValueError("Only arrays are allowed for the metric calculation.")
        if len(results) != 2:
            raise ValueError("Only two arrays are allowed for the metric calculation.")


    def __call__(self):
        try:
            self.allowed_array( self.args)
            stat, value = ks_2samp(self.args[0][-1],self.args[1][-1])
            return (f'KS stats {stat[0]},  p-value {value[0]}')     
        except Exception as e:
            print(e)  
       
    
        
        