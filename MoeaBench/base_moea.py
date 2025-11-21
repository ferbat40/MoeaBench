from abc import ABC, abstractmethod
from  MoeaBench.CACHE import CACHE
import numpy as np


class BaseMoea(ABC):
     
     @abstractmethod
     def __init__(self,problem,population,generations):
          self.__problem=problem
          self.__population=population
          self.__generations=generations
          self.__CACHE = CACHE()


     @abstractmethod
     def evaluation(self):
          raise NotImplementedError('The evaluation() method must be implemented by the user')
     

     def get_CACHE(self):
          return self.__CACHE
     

     def get_generations(self):
          return self.__generations
     

     def get_population(self):
          return self.__population


     def get_problem(self):
          return self.__problem
     

     def get_M(self):
          return self.get_problem().get_CACHE().get_BENCH_CI().get_M()
     

     def get_N(self):
          return self.get_problem().get_CACHE().get_BENCH_CI().get_Nvar()
     

     def get_n_ieq_constr(self):
          return self.get_problem().get_CACHE().get_BENCH_CI().get_n_ieq_constr()
     

     def evaluation_benchmark(self,X):
          return self.get_problem().evaluation(np.array([X]),self.get_n_ieq_constr())
     

  

     


     


