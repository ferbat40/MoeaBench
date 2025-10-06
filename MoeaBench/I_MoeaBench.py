from abc import ABC, abstractmethod


class I_MoeaBench(ABC):
   
    @abstractmethod
    def allowed_gen(self):
        pass
    
    
    @abstractmethod
    def allowed_obj(self):
        pass


    @abstractmethod
    def IPL_plot_obj(self):  
        pass
            
    
    @abstractmethod
    def pareto(self):
        pass

        
    @abstractmethod
    def change_axis(self):
        pass
      

    @abstractmethod   
    def RUN(self):
        pass

    
    @abstractmethod 
    def IPL_hypervolume(self):
        pass
    
    
    @abstractmethod 
    def IPL_GD(self):
        pass
    
    
    @abstractmethod 
    def IPL_GDplus(self):
        pass
    
    
    @abstractmethod 
    def IPL_IGD(self):
        pass
    
    
    @abstractmethod
    def IPL_IGDplus(self):
        pass
    
    
    @abstractmethod
    def IPL_objectives(self):
        pass
    
    
    @abstractmethod
    def IPL_display(self):
        pass
       
    
    @abstractmethod
    def DATA(self):
        pass

       
    @abstractmethod 
    def configure(self):
       pass
      
    
    @abstractmethod 
    def PLT(self):  
        pass


    @abstractmethod 
    def IPL_plot_hypervolume(self):
        pass

    
    @abstractmethod 
    def IPL_plot_GD(self):
        pass

    
    @abstractmethod 
    def IPL_plot_GDplus(self):
        pass

    
    @abstractmethod 
    def IPL_plot_IGD(self):
        pass

    
    @abstractmethod 
    def IPL_plot_IGDplus(self):
        pass

    
    @abstractmethod 
    def IPL_plot_obj(self):
        pass


    @abstractmethod 
    def normalize_gen(self):
        pass