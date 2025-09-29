from .DPF4 import DPF4


class P_DPF4(DPF4):

    def __init__(self, ENGINE, M, K, D, P, **kwargs):
        self.ENGINE=ENGINE
        self.M = M
        self.K = K
        self.D = D 
        self.P = P
        ENGINE.allowed_call(self)
        super().__init__(ENGINE=ENGINE, **kwargs)


    def get_ENGINE(self):
        return self.ENGINE


    def set_BENCH_conf(self):
        self.set_Penalty_param(1.25)
        self.get_ENGINE().set_BENCH_CI(self.M,self.D,14,self.P,self.K,1,13) 
        self.get_ENGINE().get_BENCH_CI().set_Nvar()
        self.get_ENGINE().set_Point()
        self.get_ENGINE().set_POF(0.5)
        self.set_Pareto(1)
        self.set_lower((self.get_Penalty_param()-self.get_Pareto())-((self.get_Penalty_param()-self.get_Pareto())*2))
        self.set_upper((self.get_Penalty_param()-self.get_Pareto()))


    def POFsamples(self):
        try:
            if self.get_ENGINE().K_validate(self.get_ENGINE().get_BENCH_CI().get_K()) == True and self.get_ENGINE().MN_validate(self.get_ENGINE().get_BENCH_CI().get_K(),self.get_ENGINE().get_BENCH_CI().get_M(),self.get_ENGINE().get_BENCH_CI().get_D()) == True and self.get_ENGINE().MN1_validate(self.get_ENGINE().get_BENCH_CI().get_M(),self.get_ENGINE().get_BENCH_CI().get_D()) == True:
                F , X = self.minimize()
                for key,value in F.items():
                    self.get_ENGINE().DATA_store(key,0,0,value,X,0)
        except Exception as e:
            print(e)


    def samples(self):
        try:
            if self.get_ENGINE().K_validate(self.get_ENGINE().get_BENCH_CI().get_K()) == True and self.get_ENGINE().MN_validate(self.get_ENGINE().get_BENCH_CI().get_K(),self.get_ENGINE().get_BENCH_CI().get_M(),self.get_ENGINE().get_BENCH_CI().get_D()) == True and self.get_ENGINE().MN1_validate(self.get_ENGINE().get_BENCH_CI().get_M(),self.get_ENGINE().get_BENCH_CI().get_D()) == True:
                F , X = self.maximize()
                for key,value in F.items():
                    self.get_ENGINE().DATA_store(key,0,0,value,X,0)
        except Exception as e:
            print(e)