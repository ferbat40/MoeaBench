from abc import ABC, abstractmethod
from  MoeaBench.CACHE import CACHE
import numpy as np


class BaseMoea(ABC):
     
     @abstractmethod
     def __init__(self,moea, problem,population,generations):
          self.__problem=problem
          self.__population=population
          self.__generations=generations
          self.__moea=moea
          self.__CACHE = CACHE()


     @abstractmethod
     def evaluation(self):
          raise NotImplementedError('The evaluation() method must be implemented by the user')
     

     def get_CACHE(self):
          return self.__CACHE
     
     
     def get_MOEA(self):
          return self.__moea
     

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
     

     def evaluation(self,X):
          return self.get_problem().evaluation(np.array([X]),self.get_n_ieq_constr())
     

     def add_MOEA(self):
          moea =  self.get_CACHE().get_DATA_conf() 
          moea.set_DATA_MOEA(self.get_MOEA(),self.get_problem()) 
          return (moea,self.get_MOEA().__class__,self.get_MOEA().__class__.__name__)

     


     


