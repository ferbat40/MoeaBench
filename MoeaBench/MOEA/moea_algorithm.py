from MoeaBench import MOEA


class moea_algorithm:

    def __init__(self,name):
        self.__memory=MOEA.CACHE()
        self.__name = name
    

    def MOEAD(self, problem,population,generations,seed):
        return MOEA.MOEAD_pymoo(problem,population,generations,seed)


    def NSGA_III(self, problem,population,generations,seed):
        return MOEA.NSGA_pymoo(problem,population,generations,seed)
       

    def SPEA_II(self, problem,population,generations,seed):
        return MOEA.SPEA_pymoo(problem,population,generations,seed)


    def U_NSGA_III(self, problem,population,generations,seed):
        return MOEA.UNSGA_pymoo(problem,population,generations,seed)


    def RVEA(self, problem,population,generations,seed):
        return MOEA.RVEA_pymoo(problem,population,generations,seed)
        

    def dict_data(self):
        return {MOEA.E_MOEA.NSGA_III : self.NSGA_III,
                MOEA.E_MOEA.SPEA_II : self.SPEA_II,
                MOEA.E_MOEA.U_NSGA_III : self.U_NSGA_III,
                MOEA.E_MOEA.MOEAD : self.MOEAD,
                MOEA.E_MOEA.RVEA: self.RVEA,
                }


    def get_CACHE(self):
        return self.__memory
    

    def get_MOEA(self, problem = None ,population = None ,generations = None ,seed = None):
        moea = [moea for moea in list(MOEA.E_MOEA) if moea.name == self.__name][0]
        return self.dict_data()[moea](problem,population,generations,seed)


