from .DTLZ1 import DTLZ1


class P_DTLZ1(DTLZ1):

    def __init__(self, M, K , P, CACHE, **kwargs):
        self.CACHE=CACHE
        self.M = M
        self.K = K
        self.P = P
        super().__init__(CACHE=CACHE, **kwargs)


    def get_CACHE(self):
        return self.CACHE


    def set_BENCH_conf(self):
        self.set_Penalty_param(0.65)   
        self.get_CACHE().set_BENCH_CI(self.M,0,10,self.P,self.K,1,1) 
        self.get_CACHE().get_BENCH_CI().set_Nvar()
        self.set_Point()
        self.set_POF(0.5)
        self.set_Pareto(0.5)
        self.set_Constraits(0.5)
         

    def POFsamples(self):  
        """  
        - Método: dtlz1.POFsamples().
        - Gera amostras da frente ótima de Pareto.
        - NOTES:
         https://evobench.github.io/benchmark/problems/DTLZ1/inPOF/

        """   
        try:
            if self.K_validate(self.get_CACHE().get_BENCH_CI().get_K()) == True and self.M_validate(self.get_CACHE().get_BENCH_CI().get_M()) == True:
                F,X = self.minimize()
                for key,value in F.items():
                    self.get_CACHE().DATA_store(key,0,0,value,[0],[0],self,self.__class__.__name__.split("_")[1]) 
        except Exception as e:
           print(e)
                                          



  
       


    
       
        
        


    







       