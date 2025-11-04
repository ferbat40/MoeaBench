from abc import ABC, abstractmethod
from MoeaBench.CACHE_bk_user import CACHE_bk_user

class BaseBenchmark(ABC):
     
     @abstractmethod
     def __init__(self, types: str, M: int, P: int, K : int = None, N  : int = None, D : int = None, n_ieq_constr :int =1):
        self.benchmark = self
        self.__M=M
        self.__P=P
        self.__K=K
        self.__D=D
        self.__N=N
        self.__n_ieq_constr=n_ieq_constr
        self.__CACHE=CACHE_bk_user()
        self.__type=types
    


     def get_CACHE(self):
          return self.__CACHE
     

     def get_M(self):
          return self.__M
     

     def get_P(self):
          return self.__P
     

     def get_K(self):
          return self.__K
     

     def get_N(self):
          return self.__N
     

     def get_D(self):
          return self.__D
     

     def get_n_ieq_constr(self):
          return self.__n_ieq_constr
     

     def get_type(self):
          return self.__type


     @abstractmethod
     def evaluation(self):
          pass
     

     @abstractmethod
     def POFsamples(self):
          pass
      

     def add_benchmark(self):
          samples = self.benchmark.POFsamples()
          self.get_CACHE().DATA_store(self.benchmark.__class__.__name__,self.get_type(),self.get_M(),self.get_N(),self.get_n_ieq_constr(),samples,self.get_P() ,self.get_K())
          

     



