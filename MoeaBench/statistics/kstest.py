from scipy.stats import ks_2samp
import pandas as pd
from MoeaBench import statistics


class kstest(statistics.allowed):
    
    def __init__(self, *args):
        self.args = args
        

    def __call__(self):
        
        table = {
            "KS stats" : [],
            "p-value" : [],
            }

        try:
            results = super().allowed_array(self.args)
            if results is not None and len(results) != 2:
                raise ValueError("Only two arrays are allowed for the metric calculation.")
            stat, value = ks_2samp(self.args[0][-1],self.args[1][-1])
            table["KS stats"].append(stat[0])
            table["p-value"].append(value[0])
            df = pd.DataFrame(table)
            df.index = df.index+1
            return df   
        except Exception as e:
            print(e)  
       
    
        
        