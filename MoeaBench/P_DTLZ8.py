from .DTLZ8 import DTLZ8


class P_DTLZ8(DTLZ8):

    def __init__(self, ENGINE, M, N, P, CACHE, **kwargs):
        self.ENGINE=ENGINE
        self.CACHE=CACHE
        self.N=N
        self.M = M
        self.P = P
        super().__init__(ENGINE=ENGINE, CACHE=CACHE, **kwargs)


    def get_CACHE(self):
        return self.CACHE
    

    def get_ENGINE(self):
        return self.ENGINE

    
    def set_BENCH_conf(self): 
        self.get_CACHE().set_BENCH_CI(self.M,0,80,self.P,0,self.M,8)
        self.get_CACHE().get_BENCH_CI().set_Nvar(self.N)
        self.get_ENGINE().set_Point()
   

    def POFsamples(self):
        """  
        - Método: dtlz1.samples().
        - Gera amostras dentro da frente ótima de Pareto.
        - NOTES:
         - Para obter informações detalhadas sobre a método:
         https://evobench.github.io/benchmark/problems/DTLZ8/inPOF/

        """  
        try:
            if self.get_ENGINE().N_validate(self.get_CACHE().get_BENCH_CI().get_Nvar()) == True and self.get_ENGINE().M_validate(self.get_CACHE().get_BENCH_CI().get_M()) == True:
                F, X = self.minimize()
                for key,value in F.items():
                    self.get_CACHE().DATA_store(key,0,0,value,X,0,self) 
        except Exception as e:
             print(e)


