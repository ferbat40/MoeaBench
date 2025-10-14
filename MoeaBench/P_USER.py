


class P_USER():

    def __init__(self, description ,my_bk, CACHE):
        self.description=description
        self.CACHE=CACHE
        self.my_bk=my_bk
        
    
    def get_CACHE(self):
        return self.CACHE
    

    def POFsamples(self):
       F = self.simulate_POF()
       self.get_CACHE().DATA_store(self.my_bk.__class__.__name__,self.description,self.my_bk.M,self.my_bk.N,self.my_bk.n_ieq_constr,F,self.my_bk.P,self.my_bk.K)