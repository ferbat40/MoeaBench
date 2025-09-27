from DTLZ8 import DTLZ8


class P_DTLZ8(DTLZ8):

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
        self.get_ENGINE().set_BENCH_CI(self.M,0,80,self.P,0,self.M,8)
        self.get_ENGINE().get_BENCH_CI().set_Nvar(self.N)
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
            if self.get_ENGINE().N_validate(self.get_ENGINE().get_BENCH_CI().get_Nvar()) == True and self.get_ENGINE().M_validate(self.get_ENGINE().get_BENCH_CI().get_M()) == True:
                F, X = self.minimize()
                for key,value in F.items():
                    self.get_ENGINE().SAMPLES_add(key,0,0,value,X,0) 
        except Exception as e:
             print(e)


    def samples(self):
        """  
        - Método: dtlz1.samples().
        - Gera amostras longe da frente ótima de Pareto.
        - NOTES:
         - Para obter informações detalhadas sobre a método:
         https://evobench.github.io/benchmark/problems/DTLZ8/outPOF/

        """  
        try:
            if self.get_ENGINE().N_validate(self.get_ENGINE().get_BENCH_CI().get_Nvar()) == True and self.get_ENGINE().M_validate(self.get_ENGINE().get_BENCH_CI().get_M()) == True:
                F , X = self.maximize()
                for key,value in F.items():
                    self.get_ENGINE().SAMPLES_add(key,0,0,value,X,0) 
        except Exception as e:
            print(e)