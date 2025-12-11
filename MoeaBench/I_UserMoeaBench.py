from abc import ABC, abstractmethod


class I_UserMoeaBench(ABC):
       
    @abstractmethod
    def plot_GD(self):
        pass


    @abstractmethod
    def plot_GDplus(self):
        pass

    
    @abstractmethod
    def plot_IGD(self):
        pass


    @abstractmethod
    def plot_IGDplus(self):
        pass


    @abstractmethod
    def spaceplot(self):
        pass


    @abstractmethod
    def surfaceplot(self):
        pass
        
  
    @abstractmethod
    def add_benchmark(self):
        pass


    @abstractmethod
    def add_moea(self):
        pass


    
