import MoeaBench.CACHE as cache_module


M_register = {}

class my_new_moea:
      """
        - accesses in memory an implementation of a user evolutionary algorithm.
        Click on the links for more:
        ...
                - Informations:
                      - sinxtase:
                      experiment.benchmark = moeabench.moeas.my_new_moea(args)
                      - [my_new_moea](https://moeabench-rgb.github.io/MoeaBench/implement_moea/memory/memory/) information about the method, 
                     
        """
      
      def __init__(self,population = 160 ,generations = 300):
            self._population=population   
            self._generations=generations      
            self.result = None  


      def __call__(self, problem, default = None):
        self.problem = problem
        try:
             result = cache_module.CACHE()
             my_moea = get_moea()
             result.get_DATA_conf().set_DATA_MOEA(my_moea(problem,self._population,self._generations),problem)
             self.result = result
             return result
        except Exception as e:
             print(e)


      @property
      def generations(self):
        return self._generations
    

      @generations.setter
      def generations(self,value):
        self._generations = value   
        if hasattr(self,"problem"):
           self.result.edit_DATA_conf().get_DATA_MOEA().generations=value
           print(self.result.edit_DATA_conf().get_DATA_MOEA().generations)


      @property
      def population(self):
        return self._population
    

      @population.setter
      def population(self,value):
        self._population = value   
        if hasattr(self,"problem"):
           self.result.edit_DATA_conf().get_DATA_MOEA().population=value 


@staticmethod    
def register_moea():
        def decorator(cls):
            try:
                name = cls.__name__
                M_register[name] = cls
            except Exception as e:
                 print(e)
            return cls
        return decorator
    

def get_moea():
        return next(iter(M_register.values())) if len(M_register.values()) > 0 else None
        
