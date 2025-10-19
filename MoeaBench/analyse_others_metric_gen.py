from .plot_gen import plot_gen
import numpy as np


class analyse_others_metric_gen(plot_gen):

    @staticmethod
    def IPL_plot_3D(*args, experiments, generations , objective, mtc, stead = False, mean = False ):  
      try: 
        others = [i for i in [stead,mean]  if i is True]
        if not len(others) == 1:
           raise ValueError("only one metric should be chosen")
        data  = [b[0] for i in args for b in i.result.get_elements()]
        analyse_others_metric_gen.allowed_gen(generations)
        analyse_others_metric_gen.allowed_gen_max(data, mtc, generations[1])
        analyse_others_metric_gen.allowed_obj(data, objective)
        gen_moea=analyse_others_metric_gen.normalize_gen(data,generations,mtc,objective)
        evaluate = [np.arange(generations[0],generations[1]+1) for _ in range(len(data))] 
        vet_aux = np.array([[np.nanstd(b) if stead is True else np.nanmean(b) for b in i] for i in gen_moea])
        metric = [vet_aux[:,i:idx].flatten() for idx, i in enumerate(range(0,vet_aux.shape[1]), start = 1)]
        metrics = [ 'objective mean' if i is True else 'objective stead' for i in others]  
        metrics.append('Generations')
        plot_g = analyse_others_metric_gen([evaluate,metric],experiments,"",  metric = metrics) 
        plot_g.configure()   
      except Exception as e:
         print(e)

  