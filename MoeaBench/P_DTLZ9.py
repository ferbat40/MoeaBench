from .DTLZ9 import DTLZ9


class P_DTLZ9(DTLZ9):

    def __init__(self, ENGINE, M, N, P, **kwargs):
        self.ENGINE=ENGINE
        self.N=N
        self.M = M
        self.P = P
        ENGINE.allowed_call(self)
        super().__init__(ENGINE=ENGINE, **kwargs)


    def get_ENGINE(self):
        return self.ENGINE


    def set_BENCH_conf(self):   
        self.get_ENGINE().set_BENCH_CI(self.M,0,90,self.P,0,self.M-1,9) 
        self.get_ENGINE().get_BENCH_CI().set_Nvar(self.N)
        self.get_ENGINE().set_Point()


    def POFsamples(self):
        try:
            if  self.get_ENGINE().N_validate(self.get_ENGINE().get_BENCH_CI().get_Nvar()) == True and self.get_ENGINE().M_validate(self.get_ENGINE().get_BENCH_CI().get_M()) == True:
                F , X = self.minimize()
                for key,value in F.items():
                    self.get_ENGINE().DATA_store(key,0,0,value,X,0)  
        except Exception as e:
            print(e)


