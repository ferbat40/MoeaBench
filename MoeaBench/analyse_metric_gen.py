from .plot_gen import plot_gen
import numpy as np


class analyse_metric_gen(plot_gen):

    @staticmethod
    def allowed_gen(max,N):
        if not max == N:
            raise TypeError(f"generations = {N} not be allowed. It must be between 0 and {max}" )


    @staticmethod
    def normalize_gen(data,N,metric):
        vet=[]
        for i in data:
            vet.append(i.get_METRIC_gen().get_arr_Metric_gen()[metric][N[0]:N[1]])
        max = 0
        for i in vet:
            if max < len(i):
                max = len(i)
        analyse_metric_gen.allowed_gen(max,N)
        vet_pt=[]
        for b in vet:
            row = b.reshape(b.shape[0],1)
            pad = np.full((max-row.shape[0],1), np.nan)
            arr = np.vstack([row,pad])
            vet_pt.append(arr.flatten())
        return vet_pt    
        
       
    @staticmethod
    def DATA(args,generations,metrics):
        data  = [b[0] for i in args for b in i.result.get_elements()]
        bench = [b[1] for i in args for b in i.result.get_elements()]
        evaluate = [np.arange(1,generations+1) for _ in range(len(data))]
        metric=analyse_metric_gen.normalize_gen(data,generations ,metrics)
        title = f'for {bench[0].get_BENCH()}'
        return [evaluate,metric],title
      
    
    @staticmethod
    def IPL_plot_Hypervolume(args,generations, val_metric,experiments):
        try:
            analyse_metric_gen.allowed_gen(generations)
            markers,title = analyse_metric_gen.DATA(args,generations,val_metric)
            plot_g = analyse_metric_gen(markers,experiments,title,  metric = ['Hypervolume','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)

    
    @staticmethod
    def IPL_plot_GD(args,generations, val_metric,experiments):
        try:
            markers,title = analyse_metric_gen.DATA(args,generations,val_metric)
            plot_g = analyse_metric_gen(markers,experiments,title,  metric = ['GD','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)


    @staticmethod
    def IPL_plot_GDplus(args,generations, val_metric,experiments):
        try:
            markers,title = analyse_metric_gen.DATA(args,generations,val_metric)
            plot_g = analyse_metric_gen(markers,experiments,title,metric = ['GD plus','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)

    
    @staticmethod
    def IPL_plot_IGD(args,generations, val_metric,experiments):
        try:
            markers,title = analyse_metric_gen.DATA(args,generations,val_metric)
            plot_g = analyse_metric_gen(markers,experiments,title,  metric = ['IGD','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)

    
    @staticmethod
    def IPL_plot_IGDplus(args,generations, val_metric,experiments):
        try:
            markers,title = analyse_metric_gen.DATA(args,generations,val_metric)
            plot_g = analyse_metric_gen(markers,experiments,title,  metric = ['IGD plus','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)


