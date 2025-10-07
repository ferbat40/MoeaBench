import numpy as np
from .H_DTLZ import H_DTLZ


class DTLZ6(H_DTLZ):

    def __init__(self, ENGINE, CACHE, **kwargs):
        self.ENGINE=ENGINE
        self.CACHE=CACHE
        super().__init__(metodhs=set([1,2,3,5]),
                         **kwargs)
   
    
    def F1(self,M,th,Gxm): 
       theta = list(map(lambda TH: np.cos(TH), th[0:(M-1)]))
       return (1+Gxm)*np.prod(np.column_stack(theta ), axis = 1).reshape(Gxm.shape[0],1)
   

    def F2(self,M,th,Gxm):
        theta = list(map(lambda TH: np.cos(TH), th[0:(M-2)]))
        return (1+Gxm)*np.prod(np.column_stack(theta ), axis = 1).reshape(Gxm.shape[0],1)*np.column_stack(np.sin(th[(M-2):(M-1)]))
           

    def F3(self,M,th,Gxm):
        theta = list(map(lambda TH: np.cos(TH), th[0:(M-3)]))
        return (1+Gxm)*np.prod(np.column_stack(theta ), axis = 1).reshape(Gxm.shape[0],1)*np.column_stack(np.sin(th[(M-3):(M-2)]))


    def Fm(self,M,th,Gxm):
        return (1+Gxm)*np.column_stack(np.sin(th[0:1]))
    

    def param_F(self):
        dict_F = {
                    self.get_method(0) : self.F1,
                    self.get_method(1) : self.F2,
                    self.get_method(2) : self.F3,
                    self.get_method(3) : self.Fm
                  }
        return dict_F
    

    def calc_TH(self,X,Gxm,M):
        return [X[:,Xi:Xi+1]*np.pi/2 if Xi == 0 else (np.pi/(4*(1+Gxm))*(1+2*Gxm*X[:,Xi:Xi+1]))  for Xi in range(0,M-1)]
       
    
    def calc_f(self,X,G):
        M =  self.CACHE.get_BENCH_CI().get_M() 
        vet_F_M = [self.calc_F_M(F,M) for F, i in enumerate(range(0,M), start = 1)]
        return np.column_stack(list(map(lambda Key: self.param_F()[Key](M,self.calc_TH(X,G,M),G),vet_F_M)))


    def calc_g(self,X):
        return np.sum(X[:, self.CACHE.get_BENCH_CI().get_M()-1:]**0.1, axis = 1).reshape(X.shape[0],1)
    

    def minimize(self):
        X =  self.ENGINE.get_Point_in_G()
        return self.show_in(self.eval_cons(self.calc_f(X,self.calc_g(X)))),X
      


        