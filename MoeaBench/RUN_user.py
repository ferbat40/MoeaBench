from .RUN import RUN
from .GEN_hypervolume import GEN_hypervolume
from .GEN_gd import GEN_gd
from .GEN_gdplus import GEN_gdplus 
from .GEN_igd import GEN_igd
from .GEN_igdplus import GEN_igdplus


class RUN_user(RUN):


     def MOEA_execute(self,name_moea,problem):
          data = self.result.edit_DATA_conf().get_DATA_MOEA().evaluation()
          self.result.DATA_store_user(name_moea,data[3],data[4],data[2],data[0],data[1],problem)
      
    
         
           

        