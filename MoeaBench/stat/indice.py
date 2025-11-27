from scipy import stats
import numpy as np
import pandas as pd


class indice:


    def __init__(self, *args):
        self.args = args 
    
    
    def allowed_array(self,args):
        results = [False if not (isinstance(i[-1],np.ndarray)) else True for i in args ]
        if False in results:
            raise ValueError("Only arrays are allowed for the metric calculation.")
        


    def __call__(self):
       
        try:
            self.allowed_array(self.args)
            
            table = {
            "array" : [],
            "mean" : [],
            "variance" : [],
            "std_dev" : [],
            "skewness" : [],
            "kurtosis" : []
            }

            for idx, i in enumerate(self.args, start = 1):
                table["array"].append(f'array {idx}')
                table["mean"].append(np.mean(i[-1]))
                table["variance"].append(np.var(i[-1]))
                table["std_dev"].append(np.std(i[-1]))
                table["skewness"].append(stats.skew(i[-1])[0])
                table["kurtosis"].append(stats.kurtosis(i[-1])[0])
            df = pd.DataFrame(table)
            df.index = df.index+1
            return df
        except Exception as e:
            print(e)  