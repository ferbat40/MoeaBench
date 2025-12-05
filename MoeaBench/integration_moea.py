from abc import ABC, abstractmethod


class integration_moea(ABC):
     
     @abstractmethod
     def __init__(self, module_moea : object = None, population : int = 160, generations :int = 300):
          self.population = population
          self.generations = generations
          self.module_moea = module_moea


     def __call__(self, problem, moea):
          self._moea = moea.repository(self.module_moea(problem,self.get_population(),self.get_generations()))
          return self.execute()
     

     def execute(self):
          self._moea = self._moea()
          return self._moea
     

     def get_population(self):
          return self.population
     

     def get_generations(self):
          return self.generations
     
     
     @property
     def generations(self):
         return self._generations
        

     @generations.setter
     def generations(self, value):
          self._generations = value  
          if hasattr(self,"_moea"):
               self._moea[0].edit_DATA_conf().get_DATA_MOEA().generations=value


     @property
     def population(self):
         return self._population
        

     @population.setter
     def population(self, value):
          self._population = value
          if hasattr(self,"_moea"):
               self._moea[0].edit_DATA_conf().get_DATA_MOEA().population=value