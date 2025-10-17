from .plot_gen_result import plot_gen_result
import numpy as np


class analyse_obj_gen(plot_gen_result):
    

    @staticmethod
    def allowed_obj(data,mtc,objective):
        if not isinstance(objective, (int)):
            raise TypeError("Only int are allowed in 'objectives'")
        min=0
        for i in data:
          min = i.get_arr_DATA().shape[1] if i.get_arr_DATA().shape[1] < min or min == 0  else min
        if  objective > min:
            raise ValueError (f'Objective {objective} can´t be greather than {min}') 
    
    
    @staticmethod
    def IPL_plot_3D(*args, experiments, generations , objective, mtc, type ):  
      #try: 
        data  = [b[0] for i in args for b in i.result.get_elements()]
        #bench = [b[1] for i in args for b in i.result.get_elements()]
        analyse_obj_gen.allowed_gen(generations)
        analyse_obj_gen.allowed_gen_max(data, 7, generations[1])
        analyse_obj_gen.allowed_obj(data,mtc,objective)
        gen_moea=analyse_obj_gen.normalize_gen(data,generations,mtc,objective)
        generation = [generations[0]+i  for i in range(0,len(gen_moea)+1)  ]
        
        plot_gen_result =  analyse_obj_gen(gen_moea,experiments,generations,metric = ['objectives','Generations'])
        plot_gen_result.configure()

        for gn_moea, gen in zip (gen_moea,generation):
            for exp, pts in enumerate(gn_moea, start = 0):
                print(pts.shape,"  ",experiments[exp],"  ",gen)
        

        
      #except Exception as e:
        #print(e)