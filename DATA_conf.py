from I_DATA_conf import I_DATA_conf
from METRIC_gen import METRIC_gen


class DATA_conf(I_DATA_conf):

    def set(self,description,generations,population,arr_DATA):
        self.__description=description
        self.__generations=generations
        self.__population=population
        self.__arr_DATA=arr_DATA
    

    def get_description(self):
        return self.__description


    def get_population(self):
        return self.__population


    def get_generations(self):
        return self.__generations
    
    
    def get_arr_DATA(self):
        return self.__arr_DATA
    
    
    def set_METRIC_gen(self,M_GEN):
        self.__METRIC_gen=METRIC_gen(M_GEN)


    def get_METRIC_gen(self):
        return self.__METRIC_gen
    


    

    

    

    
    

    






