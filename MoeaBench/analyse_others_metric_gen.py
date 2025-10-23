from .plot_gen import plot_gen
import numpy as np
from .E_metric import E_metric
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

class analyse_others_metric_gen(plot_gen):
     
    @staticmethod
    def std(value):
      return np.nanstd(value) 

    
    @staticmethod
    def mean(value):  
      return  np.nanmean(value)

    
    @staticmethod
    def min(value):
      return  np.nanmin(value) 


    @staticmethod
    def max(value):
      return np.nanmax(value) 

      
    @staticmethod
    def dict_metric():
      return  {
        0: analyse_others_metric_gen.std,
        1: analyse_others_metric_gen.mean,
        2: analyse_others_metric_gen.min,
        3: analyse_others_metric_gen.max
        }
    

    @staticmethod
    def dict_metric_label():
      return  {
        0: E_metric.std,
        1: E_metric.mean,
        2: E_metric.min,
        3: E_metric.max
        }


    @staticmethod
    def IPL_plot_3D(*args, experiments, generations , objective, mtc, val_metric, types ):  
      label=[]
      data  = [b[0] for i in args for b in i.result.get_elements()]   
      analyse_others_metric_gen.allowed_gen(generations)
      analyse_others_metric_gen.allowed_gen_max(data, mtc, generations[1])
      gen_moea=analyse_others_metric_gen.normalize_gen(data,generations,mtc,objective)
      evaluate = [np.arange(generations[0],generations[1]+1) for _ in range(len(data))] 
      metric = np.array([[ analyse_others_metric_gen.dict_metric()[val_metric[0]](np.array(line[i])) for i in [0,len(evaluate)-1]] for line in gen_moea])
      name_metric =analyse_others_metric_gen.dict_metric_label()[val_metric[0]]
      label.append(name_metric.name)
      label.append('Generations')
      label.append(types)
      plot_g = analyse_others_metric_gen([evaluate,metric],experiments, metric = label) 
      plot_g.configure() 
     

  