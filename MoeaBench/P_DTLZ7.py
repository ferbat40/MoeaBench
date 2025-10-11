from .DTLZ7 import DTLZ7


class P_DTLZ7(DTLZ7):

    def __init__(self, ENGINE, M, K, P, CACHE, **kwargs):
        self.ENGINE=ENGINE
        self.CACHE=CACHE
        self.M = M
        self.K = K
        self.P = P
        super().__init__(ENGINE=ENGINE, CACHE=CACHE, **kwargs)
    

    def get_CACHE(self):
        return self.CACHE
    
    
    def get_ENGINE(self):
        return self.ENGINE


    def set_BENCH_conf(self): 
        self.get_CACHE().set_BENCH_CI(self.M,0,70,self.P,self.K,0,7)
        self.get_CACHE().get_BENCH_CI().set_Nvar()
        self.get_ENGINE().set_Point()
        self.get_ENGINE().set_POF(0.0)
          

    def POFsamples(self):
        try:
            if self.get_ENGINE().K_validate(self.get_CACHE().get_BENCH_CI().get_K()) == True and self.get_ENGINE().M_validate(self.get_CACHE().get_BENCH_CI().get_M()) == True:
                F, X = self.minimize()
                for key,value in F.items():
                    self.get_CACHE().DATA_store(key,0,0,value,[0],[0],self,[0])  
        except Exception as e:
            print(e)


