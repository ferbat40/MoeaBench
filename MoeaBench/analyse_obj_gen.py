from .plot_gen_3D import plot_gen_3D
import numpy as np


class analyse_obj_gen(plot_gen_3D):
    
    
    @staticmethod
    def IPL_plot_3D(*args, experiments, generations , objectives, mtc, type ):  
      try:
        analyse_obj_gen.allowed_gen(generations)
        data  = [b[0] for i in args for b in i.result.get_elements()]
        bench = [b[1] for i in args for b in i.result.get_elements()]
        analyse_obj_gen.allowed_obj(bench,bench[0],experiments,objectives)
        vet_pt=analyse_obj_gen.normalize_gen(data,generations,mtc)
           
        if not len([b for i in vet_pt for b in i if not np.all(np.isnan(b)) and len(b) > 0]) > 0:   
            raise ValueError (f'No results found for plot')

        axis =  [i for i in range(0,3)]    if len(objectives) == 0 else [i-1 if i > 0 else 0 for i in objectives] 
        
        plot_gen_3D_obj =  analyse_obj_gen(bench,vet_pt,generations,experiments,axis,type)
        plot_gen_3D_obj.configure()
      except Exception as e:
        print(e)