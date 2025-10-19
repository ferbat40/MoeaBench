from .plot_gen import plot_gen
import numpy as np


class analyse_metric_gen(plot_gen):

    @staticmethod
    def normalize_gen(data,N,metric):
        vet = [i.get_METRIC_gen().get_arr_Metric_gen()[metric][N[0]:N[1]] for i in data]
        max_row = max(i.shape[0] for i in vet)
        analyse_metric_gen.allowed_gen(N)
        vet_pt=[]
        for b in vet:
            row = b.reshape(b.shape[0],1)
            pad = np.full((max_row-row.shape[0],1), np.nan) if max_row > row.shape[0] else row.shape[0]
            arr = np.vstack([row,pad])
            vet_pt.append(arr.flatten())
        return vet_pt    
        
       
    @staticmethod
    def DATA(args,generations,metrics):
        data  = [b[0] for i in args for b in i.result.get_elements()]
        evaluate = [np.arange(generations[0],generations[1]) for _ in range(len(data))]
        analyse_metric_gen.allowed_gen_max(data, 1, generations[1])
        metric=analyse_metric_gen.normalize_gen(data,generations ,metrics)   
        return [evaluate,metric]
      
    
    @staticmethod
    def IPL_plot_Hypervolume(args,generations, val_metric,experiments):
        try:
            markers = analyse_metric_gen.DATA(args,generations,val_metric)
            plot_g = analyse_metric_gen(markers,experiments,metric = ['Hypervolume','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)

    
    @staticmethod
    def IPL_plot_GD(args,generations, val_metric,experiments):
        try:
            markers = analyse_metric_gen.DATA(args,generations,val_metric)
            plot_g = analyse_metric_gen(markers,experiments,metric = ['GD','Generations'])
            plot_g.configure()
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


