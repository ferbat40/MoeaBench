from abc import ABC, abstractmethod


class integration_moea(ABC):
     
     @abstractmethod
     def __init__(self, population : int = 160, generations :int = 300):
          self.population = population
          self.generations = generations
     

     def get_population(self):
          return self.population
     

     def get_generations(self):
          return self.generations
     

     @abstractmethod
     def __call__(self):
          pass

     
     @property
     def generations(self):
         return self._generations
        

     @generations.setter
     def generations(self, value):
          self._generations = value
          if hasattr(self,"problem"):
               self.result[0].edit_DATA_conf().get_DATA_MOEA().generations=value


     @property
     def population(self):
         return self._population
        

     @population.setter
     def population(self, value):
          self._population = value
          if hasattr(self,"problem"):
               self.result[0].edit_DATA_conf().get_DATA_MOEA().population=value