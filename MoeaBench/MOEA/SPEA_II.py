from .moea_algorithm import moea_algorithm


@staticmethod
def SPEA_II(problem, *, population = 100, generations = 300, seed = 1):
        moea = moea_algorithm(SPEA_II.__name__)
        algorithm = moea.get_MOEA(problem,population,generations,seed)
        result = moea.get_CACHE()
        result.get_DATA_conf().set_DATA_MOEA(algorithm,problem)
        return result      