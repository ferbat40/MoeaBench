class BaseMoea:

     def __init__(self, problem, population=50, generations=100):
          self.problem=problem
          self.population=population
          self.generations=generations

      
     def MOEA_execute(self):
          raise NotImplementedError('The evaluation() method must be implemented by the user')
