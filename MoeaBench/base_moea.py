from abc import ABC, abstractmethod


class BaseMoea(ABC):
     
     @abstractmethod
     def __init__(self, problem, population=50, generations=100):
          self.problem=problem
          self.population=population
          self.generations=generations


     @abstractmethod
     def evaluation(self):
          raise NotImplementedError('The evaluation() method must be implemented by the user')
