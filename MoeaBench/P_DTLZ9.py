from .DTLZ9 import DTLZ9


class P_DTLZ9(DTLZ9):

    def __init__(self, M, N, P, CACHE, **kwargs):
        self.CACHE=CACHE
        self.N=N
        self.M = M
        self.P = P
        super().__init__(CACHE=CACHE, **kwargs)
    

    def get_CACHE(self):
        return self.CACHE


    def set_BENCH_conf(self):   
        self.get_CACHE().set_BENCH_CI(self.M,0,90,self.P,0,self.M-1,9) 
        self.get_CACHE().get_BENCH_CI().set_Nvar(self.N)
        self.set_Point()


    def POFsamples(self):
        try:
            if  self.N_validate(self.get_CACHE().get_BENCH_CI().get_Nvar()) == True and self.M_validate(self.get_CACHE().get_BENCH_CI().get_M()) == True:
                F , X = self.minimize()
                for key,value in F.items():
                    self.get_CACHE().DATA_store(key,0,0,value,[0],[0],self,[0])  
        except Exception as e:
            print(e)


