from scipy.stats import ks_2samp
from IPython.display import  display
import numpy as np
import pandas as pd


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

        table = {
            "KS stats" : [],
            "p-value" : [],
            }

        try:
            self.allowed_array( self.args)
            stat, value = ks_2samp(self.args[0][-1],self.args[1][-1])
            table["KS stats"].append(stat[0])
            table["p-value"].append(value[0])
            df = pd.DataFrame(table)
            df.index = df.index+1
            return df   
        except Exception as e:
            print(e)  
       
    
        
        