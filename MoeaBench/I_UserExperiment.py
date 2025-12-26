from abc import ABC, abstractmethod


class I_UserExperiment(ABC):

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
