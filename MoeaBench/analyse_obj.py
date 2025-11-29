from .plot_3D import plot_3D
import numpy as np


class analyse_obj(plot_3D):
      
    @staticmethod
    def IPL_plot_3D(experiments, data, bench, arra_gen, objectives, generations = []):
            
        #try:
            analyse_obj.allowed_obj(bench,bench[0],experiments,objectives)
            axis =  [i for i in range(0,3)]    if len(objectives) == 0 else [i-1 if i > 0 else 0 for i in objectives] 
            
            if not len([i for i in arra_gen if len(i) == 0]) == 0:   
                raise ValueError (f'No results found for plot')
            #dt = [ {'gen': generations[b], experiments[i]:  arra_gen[i][generations[b]]} for b in range(0,len(generations)) for i in range(0, len(array))]
            #analyse_obj.allowed_DATA(data, experiments)
            plot_3D_obj =  analyse_obj(bench,arra_gen,experiments,axis, generations)
            plot_3D_obj.configure()
        #except Exception as e:
            #rint(e)

    
