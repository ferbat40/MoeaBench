from .moea_algorithm import moea_algorithm


@staticmethod
def NSGA_III(problem, *, population = 100, generations = 300, seed = 1):
        """
        - genetic algorithm:
        Click on the links for more
        ...
                - NSGA-III:
                      - sinxtase:
                      experiment.moea = moeabench.MOEA.NSGA_III(args)  
                      - [general](https://moeabench-rgb.github.io/MoeaBench/algorithms/NSGA3/) references ane more...
                      - ([arguments](https://moeabench-rgb.github.io/MoeaBench/algorithms/arguments/) custom and default settings problem
                      - [configurations](https://moeabench-rgb.github.io/MoeaBench/algorithms/configuration/) algorithm configuration adopted by MoeaBench
        
        """
        moea = moea_algorithm(NSGA_III.__name__)
        algorithm = moea.get_MOEA(problem,population,generations,seed)
        result = moea.get_CACHE()
        result.get_DATA_conf().set_DATA_MOEA(algorithm,problem)
        return result     
