from .plot_gen_result import plot_gen_result
import numpy as np


class analyse_others_metric_gen(plot_gen_result):


    @staticmethod
    def IPL_plot_3D(*args, experiments, generations , objective, mtc, stead = False, mean = False ):  
      try: 
        data  = [b[0] for i in args for b in i.result.get_elements()]
        analyse_others_metric_gen.allowed_gen(generations)
        analyse_others_metric_gen.allowed_gen_max(data, mtc, generations[1])
        analyse_others_metric_gen.allowed_obj(data, objective)
        gen_moea=analyse_others_metric_gen.normalize_gen(data,generations,mtc,objective)
        evaluate = [np.arange(generations[0],generations[1]) for _ in range(len(data))] 
        vet_aux = np.array([[np.mean(b) for b in i] for i in gen_moea])
        metric = [vet_aux[:,i:idx] for idx, i in enumerate(range(0,vet_aux.shape[1]), start = 1)]
        plot_g = analyse_others_metric_gen([evaluate,metric],experiments,"",  metric = ['objective mean','Generations'])
        plot_g.configure()   
      except Exception as e:
         print(e)
