import MoeaBench.CACHE as cache_module

M_register = {}


class my_new_moea:
      
      def __init__(self,population = 160 ,generations = 300):
            self.population=population   
            self.generations=generations         


      def set_problem(self,problem):
        """
        - accesses in memory an implementation of a user evolutionary algorithm.
        Click on the links for more:
        ...
                - Informations:
                      - sinxtase:
                      experiment.problem = experiment.MOEA.my_new_moea(args)
                      - [my_new_moea](https://moeabench-rgb.github.io/MoeaBench/implement_moea/memory/memory/) information about the method, 
                     
        """
        try:
             result = cache_module.CACHE()
             my_moea = get_moea()
             result.get_DATA_conf().set_DATA_MOEA(my_moea(problem,self.population,self.generations),problem)
             return result
        except Exception as e:
             print(e)


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
        
