from .IPL_MoeaBench import IPL_MoeaBench
import numpy as np
from itertools import zip_longest
import ipywidgets as widgets
from IPython.display import  display


class analyse(IPL_MoeaBench):

    @staticmethod
    def allowed_gen(generations):
        if not isinstance(generations, (list)):
            raise TypeError("Only arrays are allowed in 'generations'")
        if not len(generations) == 2:
            raise TypeError(f"generations = {generations} not be allowed. I is necessary to follow the format: generations = [begin, end]" )
    
    
    @staticmethod
    def allowed_obj(element,data, experiments, objectives, obj = ('get_M',)):
        if not isinstance(objectives, (list)):
            raise TypeError("Only arrays are allowed in 'objectives'")
        if  0 < len(objectives) < 3:
            raise TypeError(f"objectives = {objectives} not be allowed. I is necessary to follow the format: objectives = [obj1, obj2, obj3] " )
        list_valid = list(map(lambda o: o.get_M(), filter(lambda o: all(hasattr(o,m) for m in obj), element)))
        if not all(np.array_equal(data.get_M(),arr) for arr in list_valid):
            objs = [f'{experiments[idx]}.problem = {i.get_M()} objectives' for idx, i in enumerate(element, start = 0)]
            raise ValueError (f'{objs} must be equals')   
        less = [i if i > element[0].get_M() else f'obj' for idx, i in enumerate(objectives, start = 0)  ]
        digit = [i for i in less if str(i).isdigit()]
        if digit:
            raise ValueError (f'Objective(s) {less} can´t be greather than {element[0].get_M()}')   
    

    @staticmethod
    def normalize_gen(data,generations,metric):
        vet=[]
        for i in data:
            vet.append(i.get_METRIC_gen().get_arr_Metric_gen()[metric][generations[0]:generations[1]+1])
        max = 0
        max_col = 0
        for row in zip_longest(*vet,fillvalue=np.nan):
            for i in row:
                try:
                    if i.shape[0]> max:
                        max=i.shape[0]
                    if i.shape[1]> max_col:
                        max_col=i.shape[1]
                except Exception as e:
                    continue

        vet_pt=[]
        for row in zip_longest(*vet,fillvalue=np.nan):
            vet_aux=[]
            for i in row:
                try:
                    if i.shape[0]<max:
                        pad = np.full((max-i.shape[0],i.shape[1]), np.nan)
                        arr = np.vstack([i,pad])
                        vet_aux.append(arr)
                    else:
                        vet_aux.append(i)   

                except Exception as e:
                    pad = np.full((max,max_col), np.nan)
                    vet_aux.append(pad)     
            vet_pt.append(vet_aux)   
        return vet_pt       
    

    def PLT(self):  
         out = widgets.Output()
         with out:
             display(self.figure)
         self.ui = widgets.VBox([widgets.HBox([out], layout=widgets.Layout(justify_content='center')),
                             ])
         display(self.ui)
    

    


