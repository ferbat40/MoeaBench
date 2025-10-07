from .DTLZ7 import DTLZ7


class P_DTLZ7(DTLZ7):

    def __init__(self, ENGINE, M, K, P, **kwargs):
        self.ENGINE=ENGINE
        self.M = M
        self.K = K
        self.P = P
        ENGINE.allowed_call(self)
        super().__init__(ENGINE=ENGINE, **kwargs)

    
    def get_ENGINE(self):
        return self.ENGINE


    def set_BENCH_conf(self): 
        self.get_ENGINE().set_BENCH_CI(self.M,0,70,self.P,self.K,0,7)
        self.get_ENGINE().get_BENCH_CI().set_Nvar()
        self.get_ENGINE().set_Point()
        self.get_ENGINE().set_POF(0.0)
          

    def POFsamples(self):
        try:
            if self.get_ENGINE().K_validate(self.get_ENGINE().get_BENCH_CI().get_K()) == True and self.get_ENGINE().M_validate(self.get_ENGINE().get_BENCH_CI().get_M()) == True:
                F, X = self.minimize()
                for key,value in F.items():
                    self.get_ENGINE().DATA_store(key,0,0,value,X,0)  
        except Exception as e:
            print(e)


