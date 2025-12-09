from .plot_gen import plot_gen
import numpy as np


class analyse_metric_gen(plot_gen):
       
    @staticmethod
    def DATA(args,generation, objective, experiments, bench):
        gen_f_test = [b[0].get_F_gen_non_dominate() for i in args for b in i.get_elements()]
        gen_f_max = max([len(gen)  for gen in gen_f_test])
        generations = [0,gen_f_max] if isinstance(generation, (list)) and len(generation) == 0 else generation
        analyse_metric_gen.allowed_gen(generations)
        analyse_metric_gen.allowed_gen_max(gen_f_max,generations[1])
        objectives = [1,2,3] if isinstance(objective, (list)) and  len(objective) == 0 else objective  
        analyse_metric_gen.allowed_obj(objectives)
        analyse_metric_gen.allowed_obj_equal(bench,bench[0],experiments,objectives)
        gen_f_valid = [b[0].get_F_gen_non_dominate()[generations[0]:generations[1]] for i in args for b in i.get_elements()]
        slicing = [[i-1,i]  for i in objectives]
        F_gen = []
        for i in range(len(gen_f_valid)):
            vet_aux = []
            for z in range(len(gen_f_valid[i])):
                vet_aux.append(analyse_metric_gen.slicing_arr(slicing,gen_f_valid[i][z]))
            F_gen.append(vet_aux)           
        F = [b[0].get_arr_DATA() for i in args for b in i.get_elements()]
        F_slice = [np.hstack( [b[:,i:j]  for i,j in slicing]) for b in F ]        
        evaluate = [np.arange(generations[0],generations[1]) for _ in range(len(gen_f_valid))]
        return evaluate,F_gen,F_slice 
      
    
    @staticmethod
    def IPL_plot_Hypervolume(args,generations, experiments, objectives, reference, bench):
        #try:
            evaluate,F_GEN,F = analyse_metric_gen.DATA(args,generations , objectives, experiments, bench)

            min_non = []
            max_non = []

            if not isinstance(reference,list):
                raise TypeError("Only arrays are allowed in 'references'")
        
            if len(reference) > 0:  
                min_non, max_non = analyse_metric_gen.normalize(reference)
    
            min_slice = [float(min_non[i-1]) for i in objectives] if len(min_non) > 0 else np.min(F[0], axis = 0)
            max_slice = [float(max_non[i-1]) for i in objectives] if len(max_non) > 0 else np.max(F[0], axis = 0)
    


            hv_gen = analyse_metric_gen.set_hypervolume(F_GEN,F, min_slice, max_slice)
            hypervolume_gen = [hv.evaluate() for hv in hv_gen]
            plot_g = analyse_metric_gen([evaluate,hypervolume_gen],experiments,metric = ['Hypervolume','Generations'])
            plot_g.configure()
        #except Exception as e:
           #print(e)
            
    
    @staticmethod
    def IPL_plot_GD(args,generations, experiments, objectives, bench):
        try:
            evaluate,F_GEN,F = analyse_metric_gen.DATA(args,generations , objectives, experiments, bench)
            gd_gen = analyse_metric_gen.set_GD(F_GEN,F)
            GD__gen = [hv.evaluate() for hv in gd_gen]
            plot_g = analyse_metric_gen([evaluate,GD__gen],experiments,metric = ['GD','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)
       

    @staticmethod
    def IPL_plot_GDplus(args,generations, experiments, objectives, bench):
        try:
            evaluate,F_GEN,F = analyse_metric_gen.DATA(args,generations , objectives, experiments, bench)
            gdplus_gen = analyse_metric_gen.set_GDplus(F_GEN,F)
            GDplus__gen = [hv.evaluate() for hv in gdplus_gen]
            plot_g = analyse_metric_gen([evaluate, GDplus__gen],experiments,metric = ['GD plus','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)

    
    @staticmethod
    def IPL_plot_IGD(args,generations, experiments, objectives, bench):
        try:
            evaluate,F_GEN,F = analyse_metric_gen.DATA(args,generations , objectives, experiments, bench)
            igd_gen = analyse_metric_gen.set_IGD(F_GEN,F)
            IGD__gen = [hv.evaluate() for hv in igd_gen]
            plot_g = analyse_metric_gen([evaluate,IGD__gen],experiments,metric = ['IGD','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)
        
    
    @staticmethod
    def IPL_plot_IGDplus(args,generations, experiments, objectives, bench):
        try:
            evaluate,F_GEN,F = analyse_metric_gen.DATA(args,generations , objectives, experiments, bench)
            igdplus_gen = analyse_metric_gen.set_IGD_plus(F_GEN,F)
            IGDplus__gen = [hv.evaluate() for hv in igdplus_gen]
            plot_g = analyse_metric_gen([evaluate,IGDplus__gen],experiments,metric = ['IGD plus','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)


