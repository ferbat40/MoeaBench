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
    def hypervolume(self):
        pass
  
    
    @abstractmethod
    def objective(self):
        pass


    @abstractmethod
    def variable(self):
        pass


    @abstractmethod
    def load(self):
        pass


    @abstractmethod
    def save(self):
        pass
