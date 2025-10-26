from .plot_gen import plot_gen
import numpy as np
from .GEN_hypervolume import GEN_hypervolume


class analyse_metric_gen(plot_gen):



       
    @staticmethod
    def DATA(args,generations, objectives, experiments, bench):
        gen_max = [b[0].get_F_GEN() for i in args for b in i.get_elements()]
        F = [b[0].get_arr_DATA() for i in args for b in i.get_elements()]
        analyse_metric_gen.allowed_obj(bench,bench[0],experiments,objectives)
        analyse_metric_gen.allowed_gen_max([len(gen)  for gen in gen_max],generations[1])


               
    
        slc = [[begin,end]      for end, begin in enumerate(range(0,len(objectives)), start = 1)]
        F_GEN_slice = [np.hstack( [b[:,i:j]  for i,j in slc]) for i in gen_max for b in i]

        
        F_GEN = F_GEN_slice[generations[0]:generations[1]]
        

        
        F_slice = [np.hstack( [b[:,i:j]  for i,j in slc]) for b in F ]

        

        evaluate = [np.arange(generations[0],generations[1]) for _ in range(len(F_GEN))]
       
 
        return evaluate,F_GEN,F_slice
      
    
    @staticmethod
    def IPL_plot_Hypervolume(args,generations, experiments, objectives, bench):
        try:
            evaluate,F_GEN,F = analyse_metric_gen.DATA(args,generations , objectives, experiments, bench)
            hv_gen = [GEN_hypervolume(fgen,f.shape[1],f.min(axis=0),f.max(axis=0)) for fgen,f in zip(F_GEN,F)]
            hypervolume_gen = [hv.evaluate() for hv in hv_gen]
            plot_g = analyse_metric_gen([evaluate,hypervolume_gen],experiments,metric = ['Hypervolume','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)
            
    
    @staticmethod
    def IPL_plot_GD(args,generations, val_metric,experiments):
        try:
            markers = analyse_metric_gen.DATA(args,generations,val_metric)
            plot_g = analyse_metric_gen(markers,experiments,metric = ['GD','Generations'])
            #plot_g.configure()
        except Exception as e:
            print(e)


    @staticmethod
    def IPL_plot_GDplus(args,generations, val_metric,experiments):
        try:
            markers = analyse_metric_gen.DATA(args,generations,val_metric)
            plot_g = analyse_metric_gen(markers,experiments,metric = ['GD plus','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)

    
    @staticmethod
    def IPL_plot_IGD(args,generations, val_metric,experiments):
        try:
            markers = analyse_metric_gen.DATA(args,generations,val_metric)
            plot_g = analyse_metric_gen(markers,experiments,metric = ['IGD','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)

    
    @staticmethod
    def IPL_plot_IGDplus(args,generations, val_metric,experiments):
        try:
            markers = analyse_metric_gen.DATA(args,generations,val_metric)
            plot_g = analyse_metric_gen(markers,experiments,metric = ['IGD plus','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)


