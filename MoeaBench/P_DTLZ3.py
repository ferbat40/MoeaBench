from .DTLZ3 import DTLZ3


class P_DTLZ3(DTLZ3):

    def __init__(self, M, K, P, CACHE, **kwargs):
        self.CACHE=CACHE
        self.M = M
        self.K = K
        self.P = P
        super().__init__(CACHE = CACHE, **kwargs)
    

    def get_CACHE(self):
        return self.CACHE


    def set_BENCH_conf(self): 
        self.set_Penalty_param(1.2)
        self.get_CACHE().set_BENCH_CI(self.M,0,30,self.P,self.K,1,3)
        self.get_CACHE().get_BENCH_CI().set_Nvar()
        self.set_Point()
        self.set_POF(0.5)
        self.set_Pareto(1)
        self.set_lower((self.get_Penalty_param()-self.get_Pareto())-((self.get_Penalty_param()-self.get_Pareto())*2))
        self.set_upper((self.get_Penalty_param()-self.get_Pareto()))
        

    def POFsamples(self):
        try:
            if self.K_validate(self.get_CACHE().get_BENCH_CI().get_K()) == True and self.M_validate(self.get_CACHE().get_BENCH_CI().get_M()) == True:
                F, X = self.minimize()
                for key,value in F.items():
                    self.get_CACHE().DATA_store(key,0,0,value,[0],[0],self,[0]) 
        except Exception as e:
            print(e)



    