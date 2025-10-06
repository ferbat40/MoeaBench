from .plot_solutions_3D import plot_solutions_3D
import numpy as np


class analyse_obj_gen(plot_solutions_3D):

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
    def IPL_plot_3D(*args, experiments, generations , objectives, mtc ):  
      try:
        analyse_obj_gen.allowed_gen(generations)
        data  = [b[0] for i in args for b in i.result.get_elements()]
        bench = [b[1] for i in args for b in i.result.get_elements()]
        analyse_obj_gen.allowed_obj(bench,bench[0],experiments,objectives)
        vet_pt=analyse_obj_gen.normalize_gen(data,generations,mtc)
           
        if not len([b for i in vet_pt for b in i if not np.all(np.isnan(b)) and len(b) > 0]) > 0:   
            raise ValueError (f'No results found for plot')

        axis =  [i for i in range(0,3)]    if len(objectives) == 0 else [i-1 if i > 0 else 0 for i in objectives] 
        
        plot_3DSO =  analyse_obj_gen(bench,vet_pt,generations,experiments,axis)
        plot_3DSO.configure()
      except Exception as e:
        print(e)