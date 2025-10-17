from .plot_gen_result import plot_gen_result
import numpy as np


class analyse_var_gen(plot_gen_result):

    @staticmethod
    def allowed_obj(element,data, experiments, variables, obj = ('get_Nvar',)):
        if not isinstance(variables, (list)):
            raise TypeError("Only arrays are allowed in 'variables'")
        if  0 < len(variables) < 3:
            raise TypeError(f"varuiables = {variables} not be allowed. I is necessary to follow the format: variables = [var1, var2, var3] " )
        list_valid = list(map(lambda o: o.get_Nvar(), filter(lambda o: all(hasattr(o,m) for m in obj), element)))
        if not all(np.array_equal(data.get_Nvar(),arr) for arr in list_valid):
            objs = [f'{experiments[idx]}.problem = {i.get_Nvar()} variables' for idx, i in enumerate(element, start = 0)]
            raise ValueError (f'{objs} must be equals')   
        less = [i if i > element[0].get_Nvar() else f'var' for idx, i in enumerate(variables, start = 0)  ]
        digit = [i for i in less if str(i).isdigit()]
        if digit:
            raise ValueError (f'Decision variable(s) {less} can´t be greather than {element[0].get_Nvar()}')  
        

    @staticmethod
    def IPL_plot_3D(*args, experiments, generations , objectives, mtc, type ):  
      try:
        analyse_var_gen.allowed_gen(generations)
        data  = [b[0] for i in args for b in i.result.get_elements()]
        bench = [b[1] for i in args for b in i.result.get_elements()]
        analyse_var_gen.allowed_gen(generations)
        analyse_var_gen.allowed_gen_max(data, 8, generations[1])
        analyse_var_gen.allowed_obj(bench,bench[0],experiments,objectives)
        vet_pt=analyse_var_gen.normalize_gen(data,generations,mtc)
           
        if not len([b for i in vet_pt for b in i if not np.all(np.isnan(b)) and len(b) > 0]) > 0:   
            raise ValueError (f'No results found for plot')
        
        axis =  [i for i in range(0,3)]    if len(objectives) == 0 else [i-1 if i > 0 else 0 for i in objectives] 
        
        plot_gen_result =  analyse_var_gen(bench,vet_pt,generations,experiments,axis,type)
        plot_gen_result.configure()
      except Exception as e:
        print(e)