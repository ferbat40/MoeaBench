from .plot_gen import plot_gen
import numpy as np

class analyse_metric_gen(plot_gen):
       
    @staticmethod
    def DATA(args,generations,metrics):
        data  = [b[0] for i in args for b in i.result.get_elements()]
        bench = [b[1] for i in args for b in i.result.get_elements()]
        evaluate = [np.arange(1,generations+1) for _ in range(len(data))]
        metric = [np.array(i.get_METRIC_gen().get_arr_Metric_gen()[metrics][0:generations]).flatten() for i in data]
        title = f'for {bench[0].get_BENCH()}'
        return [evaluate,metric],title
    
    
    @staticmethod
    def IPL_plot_Hypervolume(args,generations, val_metric,experiments):
        markers,title = analyse_metric_gen.DATA(args,generations,val_metric)
        plot_g = analyse_metric_gen(markers,experiments,title,  metric = ['Hypervolume','Generations'])
        plot_g.PLT()

    
    @staticmethod
    def IPL_plot_GD(args,generations, val_metric,experiments):
        markers,title = analyse_metric_gen.DATA(args,generations,val_metric)
        plot_g = analyse_metric_gen(markers,experiments,title,  metric = ['GD','Generations'])
        plot_g.PLT()


    @staticmethod
    def IPL_plot_GDplus(args,generations, val_metric,experiments):
        markers,title = analyse_metric_gen.DATA(args,generations,val_metric)
        plot_g = analyse_metric_gen(markers,experiments,title,metric = ['GD plus','Generations'])
        plot_g.PLT()

    
    @staticmethod
    def IPL_plot_IGD(args,generations, val_metric,experiments):
        markers,title = analyse_metric_gen.DATA(args,generations,val_metric)
        plot_g = analyse_metric_gen(markers,experiments,title,  metric = ['IGD','Generations'])
        plot_g.PLT()

    
    @staticmethod
    def IPL_plot_IGDplus(args,generations, val_metric,experiments):
        markers,title = analyse_metric_gen.DATA(args,generations,val_metric)
        plot_g = analyse_metric_gen(markers,experiments,title,  metric = ['IGD plus','Generations'])
        plot_g.PLT()


