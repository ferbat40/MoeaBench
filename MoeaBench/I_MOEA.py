from abc import ABC, abstractmethod

class I_MOEA(ABC):

    @abstractmethod 
    def NSGA3(self):
        pass
   

    @abstractmethod 
    def U_NSGA3(self):
        pass
    

    @abstractmethod 
    def SPEA2(self):
        pass
        

    @abstractmethod 
    def MOEAD(self):
        pass
 
 
    @abstractmethod 
    def RVEA(self):
        pass
   

    @abstractmethod
    def MOEA_execute(self):
        pass

    
    @abstractmethod
    def register_moea(self):
        pass
    

    @abstractmethod
    def get_moea(self):
        pass


    @abstractmethod
    def my_new_moea(self):
        pass

    
    @abstractmethod
    def my_implemented_moea(self):
        pass

    







    
 


    



    
            

    