from DTLZ1 import DTLZ1


class P_DTLZ1(DTLZ1):

    def __init__(self, ENGINE, M, K , P, CACHE, **kwargs):
        self.ENGINE=ENGINE
        self.CACHE=CACHE
        self.M = M
        self.K = K
        self.P = P
        ENGINE.allowed_call(self)
        super().__init__(ENGINE=ENGINE,CACHE=CACHE, **kwargs)

    
    def get_ENGINE(self):
        return self.ENGINE
    

    def get_CACHE(self):
        return self.CACHE


    def set_BENCH_conf(self):
        self.set_Penalty_param(0.65)   
        self.get_CACHE().set_BENCH_CI(self.M,0,10,self.P,self.K,1,1) 
        self.get_CACHE().get_BENCH_CI().set_Nvar()
        self.get_ENGINE().set_Point()
        self.get_ENGINE().set_POF(0.5)
        self.set_Pareto(0.5)
        self.set_lower((self.get_Penalty_param()-self.get_Pareto())-((self.get_Penalty_param()-self.get_Pareto())*2))
        self.set_upper((self.get_Penalty_param()-self.get_Pareto()))
        self.set_Constraits(0.5)
         

    def POFsamples(self):  
        """  
        - Método: dtlz1.POFsamples().
        - Gera amostras da frente ótima de Pareto.
        - NOTES:
         - Para obter informações detalhadas sobre a classe ENGINE, acesse:
         https://evobench.github.io/benchmark/problems/DTLZ1/inPOF/

        """   
        try:
            if self.get_ENGINE().K_validate(self.get_CACHE().get_BENCH_CI().get_K()) == True and self.get_ENGINE().M_validate(self.get_CACHE().get_BENCH_CI().get_M()) == True:
                F,X = self.minimize()
                for key,value in F.items():
                    self.get_CACHE().SAMPLES_add(key,0,0,value,X,0,self)  
            return self.get_CACHE()
        except Exception as e:
            print(e)
                                          

    def samples(self):
        """  
        - Método: dtlz1.samples().
        - Gera amostras longe da frente ótima de Pareto.
        - NOTES:
         - Para obter informações detalhadas sobre a método:
         https://evobench.github.io/benchmark/problems/DTLZ1/outPOF/

        """  
        try:
            if self.get_ENGINE().K_validate(self.get_CACHE().get_BENCH_CI().get_K()) == True and self.get_ENGINE().M_validate(self.get_CACHE().get_BENCH_CI().get_M()) == True:
                F,X = self.maximize()
                for key,value in F.items():
                    self.get_ENGINE().SAMPLES_add(key,0,0,value,X,0) 
        except Exception as e:
            print(e)


  
       


    
       
        
        


    







       