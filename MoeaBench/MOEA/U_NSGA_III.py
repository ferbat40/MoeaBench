from .moea_algorithm import moea_algorithm


@staticmethod
def U_NSGA_III(problem, *, population = 100, generations = 300, seed = 1):
        moea = moea_algorithm(U_NSGA_III.__name__)
        algorithm = moea.get_MOEA(problem,population,generations,seed)
        result = moea.get_CACHE()
        result.get_DATA_conf().set_DATA_MOEA(algorithm,problem)
        return result       

