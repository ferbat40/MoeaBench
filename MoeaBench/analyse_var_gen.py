from .plot_gen_result import plot_gen_result
import numpy as np


class analyse_var_gen(plot_gen_result):

    @staticmethod
    def allowed_obj(data,variable,metric):
        if not isinstance(variable, (int)):
            raise TypeError("Only int are allowed in 'variables'")
        min=0
        for i in data:
          min = i.get_METRIC_gen().get_arr_Metric_gen()[metric][0].shape[1] if i.get_METRIC_gen().get_arr_Metric_gen()[metric][0].shape[1] < min or min == 0  else min
        if  variable > min:
            raise ValueError (f'Variable {variable} can´t be greather than {min}') 
    
    
    @staticmethod
    def IPL_plot_3D(*args, experiments, generations , variable, mtc, type ):  
      try: 
        data  = [b[0] for i in args for b in i.result.get_elements()]
        analyse_var_gen.allowed_gen(generations)
        analyse_var_gen.allowed_gen_max(data, mtc, generations[1])
        analyse_var_gen.allowed_obj(data, variable,mtc)
        gen_moea=analyse_var_gen.normalize_gen(data,generations,mtc,variable)
        generation = [generations[0]+i  for i in range(0,len(gen_moea)+1)  ]      
        plot_gen_result =  analyse_var_gen(gen_moea,experiments,generation,metric = ['variables','Generations'])
        plot_gen_result.configure()      
      except Exception as e:
        print(e)