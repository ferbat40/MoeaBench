from .moea_algorithm import moea_algorithm


class MOEAD:

    def __init__(self,population = 150, generations = 300, seed = 1):
        self.population=population
        self.generations=generations
        self.seed = seed


    def set_problem(self,problem):
        """
        - genetic algorithm:
        Click on the links for more
        ...
                - MOEA/D:
                      - sinxtase:
                      experiment.moea = moeabench.MOEA.MOEAD(args)  
                      - [general](https://moeabench-rgb.github.io/MoeaBench/algorithms/MOEAD/) references and more...
                      - ([arguments](https://moeabench-rgb.github.io/MoeaBench/algorithms/arguments/)) custom and default settings problem
                      - [configurations](https://moeabench-rgb.github.io/MoeaBench/algorithms/configuration/) algorithm configuration adopted by MoeaBench
        
        """
        moea = moea_algorithm(self.__class__.__name__)
        algorithm = moea.get_MOEA(problem,self.population,self.generations,self.seed)
        result = moea.get_CACHE()
        result.get_DATA_conf().set_DATA_MOEA(algorithm,problem)
        return result 
                 