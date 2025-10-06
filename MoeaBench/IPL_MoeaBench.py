from .I_MoeaBench import I_MoeaBench

class IPL_MoeaBench(I_MoeaBench):

    def change_axis(self):
        raise NotImplementedError("Not implemented")

   
    def IPL_objectives(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_plot_obj(self):
        raise NotImplementedError("Not implemented")
    
    
    def PLT(self):
        raise NotImplementedError("Not implemented")  
    
    
    def allowed_obj(self):
        raise NotImplementedError("Not implemented")
    
    
    def configure(self):
        raise NotImplementedError("Not implemented")
    
    
    def pareto(self):
        raise NotImplementedError("Not implemented")
    

    def  IPL_GD(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_GDplus(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_IGD(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_IGDplus(self):
        raise NotImplementedError("Not implemented")
      
    
    def IPL_hypervolume(self):
        raise NotImplementedError("Not implemented")
    

    def IPL_display(self):
        raise NotImplementedError("Not implemented")
    

    def allowed_gen(self):
        raise NotImplementedError("Not implemented")

        
    def RUN(self):
        self.Moea.MOEA_execute(self.result)




