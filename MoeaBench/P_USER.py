
from .P_DTLZ1 import P_DTLZ1

class P_USER(P_DTLZ1):

    def __init__(self, description ,my_bk, CACHE):
        self.description=description
        self.CACHE=CACHE
        self.my_bk=my_bk
        
    
    def M_validate(self,M):
        raise NotImplementedError("Not implemented")


    def POFsamples(self):
       F = self.my_bk.simulate_POF()
       self.CACHE.DATA_store(self.my_bk.__class__.__name__,self.description,self.my_bk.M,self.my_bk.N,self.my_bk.n_ieq_constr,F)