
from abc import ABC, abstractmethod
class base_repository(ABC):
     
     @abstractmethod
     def __init__(self,population,generations):
          self.__population=population
          self.__generations=generations

     @abstractmethod
     def instance(self):
          raise NotImplementedError('The evaluation() method must be implemented by the user')