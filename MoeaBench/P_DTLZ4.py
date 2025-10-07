from .DTLZ4 import DTLZ4


class P_DTLZ4(DTLZ4):
    
    def __init__(self, ENGINE, M, K, P, CACHE, **kwargs):
        self.ENGINE=ENGINE
        self.CACHE=CACHE
        self.M = M
        self.K = K
        self.P = P
        super().__init__(ENGINE=ENGINE, CACHE = CACHE, **kwargs)


    def get_CACHE(self):
        return self.CACHE


    def get_ENGINE(self):
        return self.ENGINE
      
        
    def set_BENCH_conf(self): 
        self.set_Penalty_param(1.2)
        self.get_CACHE().set_BENCH_CI(self.M,0,40,self.P,self.K,1,4) 
        self.get_CACHE().get_BENCH_CI().set_Nvar()
        self.get_ENGINE().set_Point()
        self.get_ENGINE().set_POF(0.5)
        self.set_Pareto(1)
        self.set_lower((self.get_Penalty_param()-self.get_Pareto())-((self.get_Penalty_param()-self.get_Pareto())*2))
        self.set_upper((self.get_Penalty_param()-self.get_Pareto()))
        

    def POFsamples(self):
        try:
            if self.get_ENGINE().K_validate(self.get_CACHE().get_BENCH_CI().get_K()) == True and self.get_ENGINE().M_validate(self.get_CACHE().get_BENCH_CI().get_M()) == True:
                F, X = self.minimize()
                for key,value in F.items():
                    self.get_CACHE().DATA_store(key,0,0,value,X,0,self)  
        except Exception as e:
            print(e)

    