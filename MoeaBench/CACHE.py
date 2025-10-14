import numpy as np
from .BENCH_conf import BENCH_conf
from .DATA_conf import DATA_conf
from .DATA_arr import DATA_arr
from .GEN_history import GEN_history
from .GEN_hypervolume import GEN_hypervolume
from .GEN_gd import GEN_gd
from .GEN_gdplus import GEN_gdplus
from .GEN_igd import GEN_igd
from .GEN_igdplus import GEN_igdplus


class CACHE(DATA_arr):
  
  def __init__(self,**kwargs):
       self.data_conf=None
       super().__init__(list_g=[],**kwargs)


  def set_BENCH_CI(self,M,D,BENCH,P,K,n_ieq_constr,BENCH_Nvar):
        BENk=self.get_BENCH_conf()
        BENk.set(M,D,BENCH,P,K,n_ieq_constr,BENCH_Nvar)
        self.__BENCH_CI=BENk

  
  def get_BENCH_CI(self):
        return self.__BENCH_CI 
  

  def DATA_store(self,name_moea,generations,population,F,F_gen,X_gen,problem,evals,name_benchmaark):
        DT_CONF=self.get_DATA_conf()
        DT_CONF.set(name_moea,generations,population,F)
        try:
             DT_CONF.set_METRIC_gen(self.METRIC_gen_evalue(F,F_gen,X_gen,evals))   
        except Exception as e:
             print(e)
        BENCH=self.get_BENCH_conf()
        BENCH.set(problem.get_CACHE().get_BENCH_CI().get_M(),
                                  problem.get_CACHE().get_BENCH_CI().get_D(),
                                  name_benchmaark,
                                  problem.get_CACHE().get_BENCH_CI().get_P(),
                                  problem.get_CACHE().get_BENCH_CI().get_K(),
                                  problem.get_CACHE().get_BENCH_CI().get_n_ieq_constr(),
                                  problem.get_CACHE().get_BENCH_CI().get_BENCH_Nvar())
        BENCH.set_Nvar(problem.get_CACHE().get_BENCH_CI().get_Nvar())
        self.clear()
        self.add_T([DT_CONF,BENCH])


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
  

  def allowed_DATA(self,LIST):
        DATA = [self.DATA_conf_recursive(OBJ) for OBJ in LIST] 
        INF = [f'{IDATA.get_description()}' for IDATA in DATA if np.isinf(IDATA.get_arr_DATA()).any()] 
        if len(INF) > 0:
            raise ValueError(f'There are matrices with invalid values: '+",".join(f'{i}' for i in INF))