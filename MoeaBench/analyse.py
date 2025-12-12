from .IPL_MoeaBench import IPL_MoeaBench
import ipywidgets as widgets
from IPython.display import  display
import numpy as np


class analyse(IPL_MoeaBench):

    @staticmethod    
    def allowed_DATA(i):
        if hasattr(i,'result') and hasattr(i.result,'get_elements'):
            return True
        else:
            return False


    @staticmethod
    def DATA(i):
        if hasattr(i,'result') and hasattr(i.result,'get_elements'):
            return i.result
        else:
            return None
     

    @staticmethod
    def extract_pareto_result(args):
        idx = [i for i in range(1,len(args)+1)]
        val = np.array(list(map(lambda key: analyse.allowed_DATA(key),[i for i in args])))
        data = []
        benk = []
       
        if len(np.where(val == False)[0]):
            raise TypeError(f'incorrect data format: {[args[i] for i in range(0,len(val)) if val[i] == False] [0]  }')
        
        it_exp = iter(idx)
        it_arr = iter(idx)
        for i in args:
            arr = analyse.DATA(i)
            name =  f'{i.__class__.__name__} {next(it_exp)}' if arr is not None else f'{i.__class__.__name__} {next(it_arr)}'
            arr =  arr if arr is not None else i
            data.append(arr)
            benk.append(name)
        return benk, data
    
    
    def PLT(self):  
         out = widgets.Output()
         with out:
             display(self.figure)
         self.ui = widgets.VBox([widgets.HBox([out], layout=widgets.Layout(justify_content='center')),])
         display(self.ui)
