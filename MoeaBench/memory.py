from .DATA_arr import DATA_arr
from .BENCH_conf import BENCH_conf
from .DATA_conf import DATA_conf
from .DATA_arr import DATA_arr
from .GEN_hypervolume import GEN_hypervolume
from .GEN_gd import GEN_gd
from .GEN_gdplus import GEN_gdplus
from .GEN_igd import GEN_igd
from .GEN_igdplus import GEN_igdplus
from .I_memory import I_memory


class memory(DATA_arr,I_memory):
        
    def __init__(self,**kwargs):
          self.data_conf=None
          super().__init__(list_g=[],**kwargs)
          

    def METRIC_gen_evalue(self,F,F_gen,X_gen,evals):
            GEN_HV=GEN_hypervolume(F_gen,F.shape[1],F.min(axis=0),F.max(axis=0))
            GEN_GD=GEN_gd(F_gen,F)
            GEN_GDplus=GEN_gdplus(F_gen,F)
            GEN_IGD=GEN_igd(F_gen,F)
            GEN_IGDplus=GEN_igdplus(F_gen,F)    
            M_GEN = ([[0],
                      GEN_HV.evaluate(),
                      GEN_GD.evaluate(),
                      GEN_GDplus.evaluate(),
                      GEN_IGD.evaluate(),
                      GEN_IGDplus.evaluate(),
                      evals,
                      F_gen,
                      X_gen])        
            return M_GEN
  
  
    def get_DATA_conf(self):
          self.data_conf=DATA_conf()
          return self.data_conf
  

    def edit_DATA_conf(self):
          return self.data_conf
       

    def get_BENCH_conf(self):
          return BENCH_conf()