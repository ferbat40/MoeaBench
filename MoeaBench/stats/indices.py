from scipy import stats
from IPython.display import  display
import numpy as np
import pandas as pd


class indices:
    
    def __init__(self, *args):
        self.__call__(*args)

    
    def allowed_array(self,args):
        results = [False if not (isinstance(i,np.ndarray)) else True for i in args ]
        if False in results:
            raise ValueError("Only arrays are allowed for the metric calculation.")
        


    def __call__(self,*args):
       
        try:
            self.allowed_array(args)
            
            table = {
            "array" : [],
            "mean" : [],
            "variance" : [],
            "std_dev" : [],
            "skewness" : [],
            "kurtosis" : []
            }

            for idx, i in enumerate(args, start = 1):
                table["array"].append(f'array {idx}')
                table["mean"].append(np.mean(i))
                table["variance"].append(np.var(i))
                table["std_dev"].append(np.std(i))
                table["skewness"].append(stats.skew(i))
                table["kurtosis"].append(stats.kurtosis(i))
            df = pd.DataFrame(table)
            df.index = df.index+1
            display(df)
        except Exception as e:
            print(e)  