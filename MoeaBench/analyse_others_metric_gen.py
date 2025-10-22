from .plot_gen import plot_gen
import numpy as np


class analyse_others_metric_gen(plot_gen):
     
    @staticmethod
    def std(gen_moea):
      return np.array([np.nanstd(i) for i in gen_moea]),'std'

    
    @staticmethod
    def mean(gen_moea):
      return np.array([np.nanmean(i) for i in gen_moea]),'mean'

    
    @staticmethod
    def min(gen_moea):
      return np.array([np.nanmin(i) for i in gen_moea]),'minimum'

    
    @staticmethod
    def max(gen_moea):
      return np.array([np.nanmax(i) for i in gen_moea]),'maximum'
    
    
    @staticmethod
    def dict_metric():
      return  {
        0: analyse_others_metric_gen.std,
        1: analyse_others_metric_gen.mean,
        2: analyse_others_metric_gen.min,
        3: analyse_others_metric_gen.max
        }


    @staticmethod
    def IPL_plot_3D(*args, experiments, generations , objective, mtc, val_metric, type ):  
      label=[]
      data  = [b[0] for i in args for b in i.result.get_elements()]
      analyse_others_metric_gen.allowed_gen(generations)
      analyse_others_metric_gen.allowed_gen_max(data, mtc, generations[1])
      gen_moea=analyse_others_metric_gen.normalize_gen(data,generations,mtc,objective)
      evaluate = [np.arange(generations[0],generations[1]+1) for _ in range(len(data))] 
      vet_aux = list(map(lambda key: analyse_others_metric_gen.dict_metric()[key](gen_moea),val_metric))
      metrics = vet_aux[0][1]
      vet_aux = vet_aux[0][0].reshape(vet_aux[0][0].shape[0],1)
      metric = [vet_aux[:,i:idx].flatten() for idx, i in enumerate(range(0,vet_aux.shape[1]), start = 1)]
      label.append(metrics)
      label.append('Generations')
      plot_g = analyse_others_metric_gen([evaluate,metric],experiments, metric = label) 
      plot_g.configure()   
     

  