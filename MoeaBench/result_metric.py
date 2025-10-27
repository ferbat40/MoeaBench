from .RESULT import RESULT
import numpy as np


class result_metric(RESULT):


    def IPL_hypervolume(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        hv_gen = result_metric.set_hypervolume(F_GEN,F)
        hypervolume_gen = np.array([hv.evaluate() for hv in hv_gen]).flatten()
        return hypervolume_gen.reshape(hypervolume_gen.shape[0],1)
            

    def IPL_GD(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        gd_gen = result_metric.set_GD(F_GEN,F)
        GD__gen = np.array([hv.evaluate() for hv in gd_gen]).flatten()
        return GD__gen.reshape(GD__gen.shape[0],1)
    

    def IPL_GDplus(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        gdplus_gen = result_metric.set_GDplus(F_GEN,F)
        GDplus__gen = np.array([hv.evaluate() for hv in gdplus_gen]).flatten()
        return GDplus__gen.reshape(GDplus__gen.shape[0],1)
    

    def IPL_IGD(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        igd_gen = result_metric.set_IGD(F_GEN,F)
        IGD__gen = np.array([hv.evaluate() for hv in igd_gen]).flatten()
        return IGD__gen.reshape(IGD__gen.shape[0],1)
    

    def IPL_IGDplus(self, result, generation, objective):
        F_GEN, F =  self.DATA(result,generation, objective)
        igdplus_gen = result_metric.set_IGD_plus(F_GEN,F)
        IGDplus__gen = np.array([hv.evaluate() for hv in igdplus_gen]).flatten()
        return IGDplus__gen.reshape(IGDplus__gen.shape[0],1)
    
    
    