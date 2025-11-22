from abc import ABC, abstractmethod


class integration_moea(ABC):
     
     @abstractmethod
     def __init__(self,population : int = 160, generations :int = 300):
          pass


     @abstractmethod
     def __call__(self):
          pass