from MoeaBench import moeas

from typing import TYPE_CHECKING
if TYPE_CHECKING: from kernel_moea import NSGA_pymoo, SPEA_pymoo, UNSGA_pymoo, RVEA_pymoo, MOEAD_pymoo
if TYPE_CHECKING: from MoeaBench.CACHE import CACHE


class moea_algorithm:

    def __init__(self,name):
        self.__memory=moeas.CACHE()
        self.__name = name
    

    def MOEAD(self, problem,population,generations,seed):
        return moeas.MOEAD_pymoo(problem,population,generations,seed)


    def NSGAIII(self, problem,population,generations,seed):
        return moeas.NSGA_pymoo(problem,population,generations,seed)
       

    def SPEAII(self, problem,population,generations,seed):
        return moeas.SPEA_pymoo(problem,population,generations,seed)


    def U_NSGAIII(self, problem,population,generations,seed):
        return moeas.UNSGA_pymoo(problem,population,generations,seed)


    def RVEA(self, problem,population,generations,seed):
        return moeas.RVEA_pymoo(problem,population,generations,seed)
        

    def dict_data(self):
        return {moeas.E_MOEA.NSGAIII : self.NSGAIII,
                moeas.E_MOEA.SPEAII : self.SPEAII,
                moeas.E_MOEA.U_NSGAIII : self.U_NSGAIII,
                moeas.E_MOEA.MOEAD : self.MOEAD,
                moeas.E_MOEA.RVEA: self.RVEA,
                }


    def get_CACHE(self):
        return self.__memory
    

    def get_MOEA(self, problem = None ,population = None ,generations = None ,seed = None):
        moea = [moea for moea in list(moeas.E_MOEA) if moea.name == self.__name][0]
        return self.dict_data()[moea](problem,population,generations,seed)


