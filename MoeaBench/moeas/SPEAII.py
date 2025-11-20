from .moea_algorithm import moea_algorithm


class SPEAII:

    def __init__(self,population = 100, generations = 300, seed = 1):
        self.population=population
        self.generations=generations
        self.seed = seed


    def set_problem(self,problem):
        """
        - genetic algorithm:
        Click on the links for more
        ...
                - SPEA-II:
                      - sinxtase:
                      experiment.moea = moeabench.MOEA.SPEA_II(args)  
                      - [general](https://moeabench-rgb.github.io/MoeaBench/algorithms/SPEA2/) references and  more...
                      - ([arguments](https://moeabench-rgb.github.io/MoeaBench/algorithms/arguments/)) custom and default settings problem
                      - [configurations](https://moeabench-rgb.github.io/MoeaBench/algorithms/configuration/) algorithm configuration adopted by MoeaBench
        
        """
        moea = moea_algorithm(self.__class__.__name__)
        algorithm = moea.get_MOEA(problem,self.population,self.generations,self.seed)
        result = moea.get_CACHE()
        result.get_DATA_conf().set_DATA_MOEA(algorithm,problem)
        return result      