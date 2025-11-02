from .moea_algorithm import moea_algorithm


@staticmethod
def MOEAD(problem, *, population = 100, generations = 300, seed = 1):
        moea = moea_algorithm(MOEAD.__name__)
        algorithm = moea.get_MOEA(problem,population,generations,seed)
        result = moea.get_CACHE()
        result.get_DATA_conf().set_DATA_MOEA(algorithm,problem)
        return result
                 