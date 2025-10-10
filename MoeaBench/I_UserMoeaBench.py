from abc import ABC, abstractmethod


class I_UserMoeaBench(ABC):
       
    @abstractmethod
    def plot_obj(self):
        pass


    @abstractmethod
    def plot_var(self):
        pass
    

    @abstractmethod
    def plot_hypervolume(self):
        pass


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
    def pareto(self):
        pass


    @abstractmethod
    def pareto_surface(self):
        pass
        

    @abstractmethod  
    def run(self):
        pass

    
    @abstractmethod
    def hypervolume(self):
        pass


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
    def objectives(self):
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


    @abstractmethod
    def my_new_moea(self):
        pass


    @abstractmethod
    def my_new_benchmark(self):
        pass