from .moea_algorithm import moea_algorithm


class NSGAIII:
    """
        - **genetic algorithm:**
        Click on the links for more
        ...
                - **NSGA-III:**
                      - sinxtase:
                      experiment.moea = moeabench.MOEA.NSGA_III(args)  
                      - [general](https://moeabench-rgb.github.io/MoeaBench/algorithms/NSGA3/) references and more...
                      - ([arguments](https://moeabench-rgb.github.io/MoeaBench/algorithms/arguments/)) custom and default settings problem
                      - [configurations](https://moeabench-rgb.github.io/MoeaBench/algorithms/configuration/) algorithm configuration adopted by MoeaBench
        
        """

    def __init__(self,population = 150, generations = 300, seed = 1):
        self.population=population
        self.generations=generations
        self.seed = seed
        
        
    def __call__(self, problem, default = None):
        moea = moea_algorithm()
        algoritm = moea.get_MOEA(self.__class__.__name__)
        class_algoritm = getattr(algoritm[0],algoritm[1].name)
        instance = class_algoritm(problem,self.population,self.generations,self.seed)
        result = moea.get_CACHE()
        result.get_DATA_conf().set_DATA_MOEA(instance,problem)
        return result     
