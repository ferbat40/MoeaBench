# I_ENGINE import I_ENGINE
from .ALLOWED import ALLOWED
import numpy as np
import datetime as dt
import pandas as pd
#from ENGINE_external import ENGINE_external
#from ENGINE_external_lite import ENGINE_external_lite


class ENGINE(ALLOWED):#(ALLOWED,FILE,I_ENGINE):

    """  
    - Instância:    
      engine = ENGINE()  
    - ENGINE implementa diversos métodos usados por outras classes do Evobench, 
    inserido por parametro:
    - NOTES:
      - Para obter informações detalhadas sobre a classe:
      https://evobench.github.io/Benchmark/main/engine/

    """   
    
    def __init__(self,CACHE,**kwargs):
        #self.__ENGINE_full=ENGINE_external(ENGINE=self)
        #self.__ENGINE_lite=ENGINE_external_lite(ENGINE=self)
        self.CACHE=CACHE
        
    

    def ENGINE_full(self):
        return self.__ENGINE_full
    
       
    def ENGINE_lite(self):
        return self.__ENGINE_lite
    

    #def memory(self):
       # return self.__memory
       
       
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
    

    def CREATE(self,DATA,BENCH, G = 0, P = 0,metric = ['X',
                                                       'Hypervolume',
                                                       'GD',
                                                       'GD plus',
                                                       'IGD',
                                                       'IGD plus',
                                                       'EVALS'], 
                                                        extension = '.xlsx'):
        try:
            with pd.ExcelWriter(self.FIle_name(DATA,BENCH, G, P, extension),engine='openpyxl') as writer:
                df = pd.DataFrame(DATA.get_arr_DATA())
                df.to_excel(writer, sheet_name="F",index=False)
                for imetric, ivalues in zip(metric,DATA.get_METRIC_gen().get_arr_Metric_gen()):
                    df = pd.DataFrame(ivalues)
                    df.to_excel(writer, sheet_name=imetric,index=False)
        except Exception as e:
            print(e)
    

    def FIle_name(self,DATA,BENCH, G, P, extension):
        date = dt.datetime.now()

        try:
            R = list(map(lambda key_refer: self.STR_refer()[key_refer],[str(DATA.get_description())]))[0]
        except Exception as e:
            R = DATA.get_description()
     
        try:
            B = list(map(lambda Key_benc:  self.STR_bench()[Key_benc],[BENCH.get_BENCH()]))[0]
        except Exception as e:
            B = BENCH.get_BENCH()
        
        try:
            G = f'G{DATA.get_generations()}P{DATA.get_population()}' if int(DATA.get_generations()) > 0 else f'G{G}P{P}'
        except Exception as e:
            pass     
        return f'analysis/R{R}_B{B}{G}M{BENCH.get_M()}K{BENCH.get_K()}D{BENCH.get_D()}N{BENCH.get_Nvar()}t{date.strftime("%m%M%S")}{extension}'

    
    

