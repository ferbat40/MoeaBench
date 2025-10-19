from .RESULT import RESULT
import numpy as np


class result_metric(RESULT):

    def IPL_hypervolume(self, result, N, vmtc = 1):
        self.allowed_gen(N)
        self.allowed_gen_max(result, vmtc, N)
        mtc = self.DATA(result,N,1)
        return mtc.reshape(mtc.shape[0],1)
    

    def IPL_GD(self, result, N, vmtc = 2):
        self.allowed_gen(N)
        self.allowed_gen_max(result, vmtc, N)
        mtc = self.DATA(result,N,2)
        return mtc.reshape(mtc.shape[0],1)
    

    def IPL_GDplus(self, result, N, vmtc = 3):
        self.allowed_gen(N)
        self.allowed_gen_max(result, vmtc, N)
        mtc = self.DATA(result,N,3)
        return mtc.reshape(mtc.shape[0],1)
    

    def IPL_IGD(self, result, N, vmtc = 4):
        self.allowed_gen(N)
        self.allowed_gen_max(result, vmtc, N)
        mtc = self.DATA(result,N,4)
        return mtc.reshape(mtc.shape[0],1)
    

    def IPL_IGDplus(self, result, N, vmtc = 5):
        self.allowed_gen(N)
        self.allowed_gen_max(result, vmtc, N)
        mtc = self.DATA(result,N,5)
        return mtc.reshape(mtc.shape[0],1)
    
    
    