# I_ENGINE import I_ENGINE
from .ALLOWED import ALLOWED
import numpy as np
import datetime as dt
import pandas as pd



class ENGINE(ALLOWED):

    
    
    def __init__(self,CACHE,**kwargs):

        self.CACHE=CACHE
        
    

    def ENGINE_full(self):
        return self.__ENGINE_full
    
       
    def ENGINE_lite(self):
        return self.__ENGINE_lite

       
       
    def get_Point_in_G(self):
        return self.__Point_in_G 
    
    
    def get_Point_out_G(self):
        return self.__Point_out_G
    

    def set_Point(self):
        self.__Point_in_G=np.array([*np.random.random((self.CACHE.get_BENCH_CI().get_P(),self.CACHE.get_BENCH_CI().get_Nvar()))*1.0])
        self.__Point_out_G=np.array([*np.random.random((self.CACHE.get_BENCH_CI().get_P(),self.CACHE.get_BENCH_CI().get_Nvar()))*1.0])
        

    def set_POF(self,POF):
        N_Bench = self.CACHE.get_BENCH_CI().get_BENCH_Nvar()
        if N_Bench <=7:
            self.__Point_in_G[:,self.CACHE.get_BENCH_CI().get_M()-1:self.CACHE.get_BENCH_CI().get_Nvar()]=POF
            self.__POF=POF
        elif N_Bench >= 10 and  N_Bench < 14:
            self.__Point_in_G[:,self.CACHE.get_BENCH_CI().get_D()-1:self.CACHE.get_BENCH_CI().get_Nvar()]=POF
            self.__POF=POF
        elif N_Bench == 14:
            self.__Point_in_G[:,self.CACHE.get_BENCH_CI().get_M()-1:self.CACHE.get_BENCH_CI().get_Nvar()]=POF
            self.__POF=POF

    
    def get_POF(self):
        return self.__POF
    

    

    
    

