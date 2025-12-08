from abc import ABC, abstractmethod


class I_UserExperiment(ABC):

    @abstractmethod
    def GD(self):
        pass

    
    @abstractmethod
    def GDplus(self):
        pass


    @abstractmethod
    def IGD(self):
        pass


    @abstractmethod
    def IGDplus(self):
        pass


    @abstractmethod  
    def run(self):
        pass

    
    @abstractmethod
    def objectives(self):
        pass

    
    @abstractmethod
    def front(self):
        pass
        

    @abstractmethod
    def set(self):
        pass
    

    @abstractmethod
    def variables(self):
        pass


    @abstractmethod
    def load(self):
        pass


    @abstractmethod
    def save(self):
        pass
