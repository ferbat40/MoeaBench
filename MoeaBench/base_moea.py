from .I_BaseMoea import I_BaseMoea

class BaseMoea(I_BaseMoea):

     def __init__(self, problem, population=50, generations=100):
          self.problem=problem
          self.population=population
          self.generations=generations

      

