from .moea_algorithm import moea_algorithm
    

@staticmethod

def RVEA(problem, *, population = 100, generations = 300, seed = 1):
        """
        - genetic algorithm:
        Click on the links for more
        ...
                - RVEA:
                      - sinxtase:
                      experiment.moea = moeabench.MOEA.RVEA(args)  
                      - [general](https://moeabench-rgb.github.io/MoeaBench/algorithms/RVEA/) references and  more...
                      - ([arguments])(https://moeabench-rgb.github.io/MoeaBench/algorithms/arguments/) custom and default settings problem
                      - [configurations](https://moeabench-rgb.github.io/MoeaBench/algorithms/configuration/) algorithm configuration adopted by MoeaBench
        
        """
        moea = moea_algorithm(RVEA.__name__)
        algorithm = moea.get_MOEA(problem,population,generations,seed)
        result = moea.get_CACHE()
        result.get_DATA_conf().set_DATA_MOEA(algorithm,problem)
        return result