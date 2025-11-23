from MoeaBench import moea


from typing import TYPE_CHECKING
if TYPE_CHECKING: from kernel_moea import NSGA_pymoo, SPEA_pymoo, UNSGA_pymoo, RVEA_pymoo, MOEAD_pymoo
if TYPE_CHECKING: from MoeaBench.CACHE import CACHE


class moea_algorithm:

    def __init__(self):
        self.__memory=moea.CACHE()
    

    def MOEAD(self):
        return moea.kernel_moea.MOEAD_pymoo, moea.E_MOEA_algorithm.MOEAD_pymoo
               

    def NSGAIII(self):
        return moea.kernel_moea.NSGA_pymoo, moea.E_MOEA_algorithm.NSGA_pymoo
    

    def SPEAII(self,):
        return moea.kernel_moea.SPEA_pymoo, moea.E_MOEA_algorithm.SPEA_pymoo
            

    def U_NSGAIII(self):
        return moea.kernel_moea.UNSGA_pymoo, moea.E_MOEA_algorithm.UNSGA_pymoo,


    def RVEA(self):
        return moea.kernel_moea.RVEA_pymoo, moea.E_MOEA_algorithm.RVEA_pymoo
    

    def my_new_moea(self):
        return moea.my_new_moea, moea.my_new_moea.__name__


    def dict_data(self):
        return {moea.E_MOEA.NSGAIII : self.NSGAIII,
                moea.E_MOEA.SPEAII : self.SPEAII,
                moea.E_MOEA.U_NSGAIII : self.U_NSGAIII,
                moea.E_MOEA.MOEAD : self.MOEAD,
                moea.E_MOEA.RVEA: self.RVEA,
                moea.E_MOEA.my_new_moea: self.my_new_moea
                }


    def get_CACHE(self):
        return self.__memory
    

    def get_MOEA(self,name):
        moea_list = [moea for moea in list(moea.E_MOEA) if moea.name == name]
        return self.dict_data()[moea_list[0]]() if len(moea_list) > 0 else False

