from abc import ABC, abstractmethod

class I_DATA_conf(ABC):
    

    @abstractmethod
    def get_arr_DATA(self):
        pass


    @abstractmethod
    def get_description(self):
        pass


    @abstractmethod
    def get_generations(self):
        pass


    @abstractmethod
    def get_population(self):
        pass


    @abstractmethod
    def get_METRIC_gen(self):
        pass


    @abstractmethod
    def get_problem(self):
        pass

    
    @abstractmethod
    def set_DATA_MOEA(self):
        pass


    @abstractmethod
    def get_DATA_MOEA(self):
        pass


   

    
   