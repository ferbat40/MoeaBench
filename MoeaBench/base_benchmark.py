from abc import ABC, abstractmethod

class BaseBenchmark(ABC):
     
     @abstractmethod
     def __init__(self,CACHE):
        self.M=3
        self.P=150
        self.K=5
        self.n_ieq_constr=1
        self.N=0
        self.CACHE=CACHE


     @abstractmethod
     def evaluation(self):
          pass
     

     @abstractmethod
     def POFsamples(self):
          pass
     

     @abstractmethod
     def get_CACHE(self):
          pass

