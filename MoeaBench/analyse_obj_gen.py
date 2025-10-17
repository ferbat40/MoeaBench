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
        plot_gen_result =  analyse_obj_gen(gen_moea,experiments,generation,metric = ['objectives','Generations'])
        plot_gen_result.configure()

        #print(generation)
        #for   gen, pts  in zip(generation,gen_moea):
               # for pts_moea,exp in zip(pts,experiments):
                    #print(pts_moea.shape,"  ",exp,"  ",gen)
       
       
        #for gen,pts in zip(range(0,len(vet_pt)),  vet_pt):
        #for i in vet_pt:
              #for b in i:
                # print(b)
           
        #if not len([b for i in vet_pt for b in i if not np.all(np.isnan(b)) and len(b) > 0]) > 0:   
            #raise ValueError (f'No results found for plot')

        #axis =  [i for i in range(0,3)]    if len(objectives) == 0 else [i-1 if i > 0 else 0 for i in objectives] 
        
        #plot_gen_3D_obj =  analyse_obj_gen(bench,vet_pt,generations,experiments,axis,type)
        #plot_gen_3D_obj.configure()
      #except Exception as e:
        #print(e)