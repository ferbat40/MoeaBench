from .plot_gen import plot_gen
import numpy as np
from .GEN_hypervolume import GEN_hypervolume
from .GEN_gd import GEN_gd
from .GEN_gdplus import GEN_gdplus
from .GEN_igd import GEN_igd
from .GEN_igdplus import GEN_igdplus



class analyse_metric_gen(plot_gen):

    @staticmethod
    def slicing_arr(slc,arr):
        return np.hstack([arr[:,i:j]  for i,j in slc])
       

    @staticmethod
    def DATA(args,generation, objective, experiments, bench):
        gen_f_test = [b[0].get_F_GEN() for i in args for b in i.get_elements()]
        gen_f_max = max([len(gen)  for gen in gen_f_test])
        generations = [0,gen_f_max] if isinstance(generation, (list)) and len(generation) == 0 else generation
        analyse_metric_gen.allowed_gen(generations)
        analyse_metric_gen.allowed_gen_max(gen_f_max,generations[1])
        objectives = [1,2,3] if isinstance(objective, (list)) and  len(objective) == 0 else objective  
        analyse_metric_gen.allowed_obj(bench,bench[0],experiments,objectives)
        gen_f_valid = [b[0].get_F_GEN()[generations[0]:generations[1]] for i in args for b in i.get_elements()]
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
    def IPL_plot_Hypervolume(args,generations, experiments, objectives, bench):
        try:
            evaluate,F_GEN,F = analyse_metric_gen.DATA(args,generations , objectives, experiments, bench)
            hv_gen = [GEN_hypervolume(fgen,f.shape[1],f.min(axis=0),f.max(axis=0)) for fgen,f in zip(F_GEN,F)]
            hypervolume_gen = [hv.evaluate() for hv in hv_gen]
            plot_g = analyse_metric_gen([evaluate,hypervolume_gen],experiments,metric = ['Hypervolume','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)
            
    
    @staticmethod
    def IPL_plot_GD(args,generations, experiments, objectives, bench):
        try:
            evaluate,F_GEN,F = analyse_metric_gen.DATA(args,generations , objectives, experiments, bench)
            gd_gen = [GEN_gd(fgen,f) for fgen,f in zip(F_GEN,F)]
            GD__gen = [hv.evaluate() for hv in gd_gen]
            plot_g = analyse_metric_gen([evaluate,GD__gen],experiments,metric = ['GD','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)
       

    @staticmethod
    def IPL_plot_GDplus(args,generations, experiments, objectives, bench):
        try:
            evaluate,F_GEN,F = analyse_metric_gen.DATA(args,generations , objectives, experiments, bench)
            gdplus_gen = [GEN_gdplus(fgen,f) for fgen,f in zip(F_GEN,F)]
            GDplus__gen = [hv.evaluate() for hv in gdplus_gen]
            plot_g = analyse_metric_gen([evaluate, GDplus__gen],experiments,metric = ['GD plus','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)

    
    @staticmethod
    def IPL_plot_IGD(args,generations, experiments, objectives, bench):
        try:
            evaluate,F_GEN,F = analyse_metric_gen.DATA(args,generations , objectives, experiments, bench)
            igd_gen = [GEN_igd(fgen,f) for fgen,f in zip(F_GEN,F)]
            IGD__gen = [hv.evaluate() for hv in igd_gen]
            plot_g = analyse_metric_gen([evaluate,IGD__gen],experiments,metric = ['IGD','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)
        
    
    @staticmethod
    def IPL_plot_IGDplus(args,generations, experiments, objectives, bench):
        try:
            evaluate,F_GEN,F = analyse_metric_gen.DATA(args,generations , objectives, experiments, bench)
            igdplus_gen = [GEN_igdplus(fgen,f) for fgen,f in zip(F_GEN,F)]
            IGDplus__gen = [hv.evaluate() for hv in igdplus_gen]
            plot_g = analyse_metric_gen([evaluate,IGDplus__gen],experiments,metric = ['IGD plus','Generations'])
            plot_g.configure()
        except Exception as e:
            print(e)


