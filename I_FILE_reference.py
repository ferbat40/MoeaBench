from abc import ABC, abstractmethod


class I_FILE_reference(ABC):


    @abstractmethod
    def STR_param(self):
        pass
         

    @abstractmethod
    def STR_rntfound(self):
        pass

    
    @abstractmethod
    def STR_refer(self):
        pass
    
    
    @abstractmethod
    def STR_bntfound(self):
        pass
     
    
    @abstractmethod
    def STR_bench(self):
        pass
    
    
    @abstractmethod
    def DIGIT_allow(self):
        pass