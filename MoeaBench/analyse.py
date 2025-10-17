from .IPL_MoeaBench import IPL_MoeaBench
import numpy as np
from itertools import zip_longest
import ipywidgets as widgets
from IPython.display import  display


class analyse(IPL_MoeaBench):

    @staticmethod
    def allowed_gen_max(result, mtc, N):
        N = len(result.gret_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[mtc])  if N is None  else N
        vmax = max(len(arr.get_METRIC_gen().get_arr_Metric_gen()[mtc]) for arr in result)
        if not N <= vmax:
            raise TypeError(f"generations = {N} not be allowed. It must be between 0 and {vmax}" )
  

    @staticmethod
    def allowed_gen(generations):
        if not isinstance(generations, (list)):
            raise TypeError("Only arrays are allowed in 'generations'")
        if not len(generations) == 2:
            raise TypeError(f"generations = {generations} not be allowed. I is necessary to follow the format: generations = [begin, end]" )
        if not generations[0] <= generations[1]:
            raise TypeError("the initial generation must be smaller than the final generation")
    

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
    def normalize_gen(data,generations,metric,objective):
        vet=[]

        for i in data:
            vet.append(i.get_METRIC_gen().get_arr_Metric_gen()[metric])
        

        vet_pt=[]
        for row in zip_longest(*vet,fillvalue=np.nan):
           vet_pt.append(row)
        
        
        max = 0
        for pts in vet_pt:
            for  arr in pts:
                try:
                    max = arr.shape[0] if max < arr.shape[0] else max
                except Exception as e:
                    continue
        
        moea=[]
        gen=[]
        for pts in vet_pt:
           moea=[]
           for  arr in pts:
               
               if not isinstance(arr, (np.ndarray)):
                   moea.append(np.full( (max,1), np.nan))
               elif isinstance(arr, (np.ndarray)):
                   moea.append(np.vstack( (arr[:,objective:objective+1], np.full( (max-arr.shape[0],1), np.nan)) ))
           gen.append(moea)
        
        return gen[generations[0]:generations[1]+1]
        
      

        


           
            
            #vet_aux=[]
            #for i in row:
                #vet_aux.append(np.array(i))
            #vet_pt.append(vet_aux)
        
        #for pts, gen in zip(vet_pt,range(0,len(vet_pt))):
            #or b in pts:
                #print(type(pts),gen)
            #print(i)
            #print(i.shape)


               

   
    

    def PLT(self):  
         out = widgets.Output()
         with out:
             display(self.figure)
         self.ui = widgets.VBox([widgets.HBox([out], layout=widgets.Layout(justify_content='center')),
                             ])
         display(self.ui)
    

    


