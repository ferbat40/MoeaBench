from scipy.stats import mannwhitneyu
from .allowed_stats import allowed_stats
import numpy as np


class mwtest_instance(allowed_stats):
    
    def __init__(self, args, alternative_metric):
        self.args = args
        self.statistic = None
        self.pvalue = None
        self.alternative_metric = alternative_metric


    def allowed(self,args):
        valid = [True if isinstance(arr,np.ndarray) and  arr.ndim == 1 else False for arr in args]
        if False in valid:
            raise ValueError("only one-dimensional arrays are allowed.")    
        if valid is not None and len(valid) != 2:
            raise ValueError("only two arrays are allowed for the metric calculation.")


    def __call__(self):      
        try:
            self.allowed(self.args)
            valid_values = [i[0] for i in self.args]
            stat, value = mannwhitneyu(valid_values[0],valid_values[1], alternative=self.alternative_metric)
            self.statistic = float(stat)
            self.pvalue = float(value)
        except Exception as e:
            print(e)  
          
        
def mwtest(*args, alternative):
    mb = mwtest_instance(args, alternative)
    mb()
    return mb