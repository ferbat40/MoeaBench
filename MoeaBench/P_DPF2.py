from .DPF2 import DPF2


class P_DPF2(DPF2):

    def __init__(self, M, K, D, P , CACHE, **kwargs):
        self.CACHE=CACHE
        self.M = M
        self.K = K
        self.D = D 
        self.P = P
        super().__init__(CACHE=CACHE, **kwargs)


    def get_CACHE(self):
        return self.CACHE


    def set_BENCH_conf(self): 
        self.get_CACHE().set_BENCH_CI(self.M,self.D,12,self.P,self.K,0,11)
        self.get_CACHE().get_BENCH_CI().set_Nvar()
        self.set_Point()
        self.set_POF(0.0)
        

    def POFsamples(self):
        try:
            if self.K_validate(self.get_CACHE().get_BENCH_CI().get_K()) == True and self.MN_validate(self.get_CACHE().get_BENCH_CI().get_K(),self.get_CACHE().get_BENCH_CI().get_M(),self.get_CACHE().get_BENCH_CI().get_D()) == True and self.MN1_validate(self.get_CACHE().get_BENCH_CI().get_M(),self.get_CACHE().get_BENCH_CI().get_D()) == True:
                F , X = self.minimize()
                for key,value in F.items():
                    self.get_CACHE().DATA_store(key,0,0,value,[0],[0],self,[0]) 
        except Exception as e:
            print(e)


