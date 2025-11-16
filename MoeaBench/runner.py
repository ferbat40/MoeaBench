from .I_MOEA import I_MOEA
from .GEN_history import GEN_history
from .CACHE import CACHE


class runner(I_MOEA):

    def __init__(self):
        self.result=CACHE()


    def get_history(self,history,F):
         return GEN_history(history,F)
    
    
  


    

    

       
           
    

    
   
    
                     
  
