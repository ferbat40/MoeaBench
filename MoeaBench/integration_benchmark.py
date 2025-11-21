from abc import ABC, abstractmethod


class integration_benchmark(ABC):
     
     @abstractmethod
     def __init__(self, type : str = None, M : int = 3, P : int = 700, K : int = 10, N : int = 0, D : int = 2, n_ieq_constr : int = 1):
          pass


     @abstractmethod
     def instance(self):
          pass