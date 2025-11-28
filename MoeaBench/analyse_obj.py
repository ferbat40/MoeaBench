from .plot_3D import plot_3D
import numpy as np


class analyse_obj(plot_3D):
      
    @staticmethod
    def IPL_plot_3D(experiments, data, bench, array, objectives):
        arr = [np.concatenate(   (array[i][1],array[i][1])) for i in range(0, len(array))]
        #for i in arr:
            #print(i.shape)
            #join = np.concatenate(   (array[0][50],array[0][-1]))
            #arr.extend(join.shape)
        #arr = []
        #join = np.concatenate(   (array[0][50],array[0][-1]))
        #arr.append(join)
        try:
            analyse_obj.allowed_obj(bench,bench[0],experiments,objectives)
            axis =  [i for i in range(0,3)]    if len(objectives) == 0 else [i-1 if i > 0 else 0 for i in objectives] 
            #analyse_obj.allowed_DATA(data,experiments)
            if not len([i for i in arr if len(i) == 0]) == 0:   
                raise ValueError (f'No results found for plot')
            plot_3D_obj =  analyse_obj(bench,arr,experiments,axis)
            plot_3D_obj.configure()
        except Exception as e:
            print(e)

    
