from .plot_surface_3D import plot_surface_3D

class analyse_surface_obj(plot_surface_3D):

    @staticmethod
    def IPL_plot_3D(experiments, data, bench, array, objectives):
        try:
            analyse_surface_obj.allowed_obj(bench,bench[0],experiments,objectives)
            axis =  [i for i in range(0,3)]    if len(objectives) == 0 else [i-1 if i > 0 else 0 for i in objectives] 
            if not len([i for i in array if len(i) == 0]) == 0:   
                raise ValueError (f'No results found for plot')
            plot_surface_3D_obj =  analyse_surface_obj(bench,array,experiments,axis)
            plot_surface_3D_obj.configure()
        except Exception as e:
            print(e)