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

  
  def BENCH_conf_recursive(self,OBJ):
       if isinstance(OBJ,BENCH_conf):
            return OBJ
       elif isinstance(OBJ,tuple):
            for b in OBJ:
                result = self.BENCH_conf_recursive(b)
                if result is not None:
                    return result
       return None
    

  def DATA_conf_recursive(self,OBJ):
       if isinstance(OBJ,DATA_conf):
            return OBJ
       elif isinstance(OBJ,tuple):
            for b in OBJ:
                result = self.DATA_conf_recursive(b)
                if result is not None:
                    return result
       return None


  def set_BENCH_CI(self,M,D,BENCH,P,K,n_ieq_constr,BENCH_Nvar):
        BENk=self.get_BENCH_conf()
        BENk.set(M,D,BENCH,P,K,n_ieq_constr,BENCH_Nvar)
        self.__BENCH_CI=BENk

  
  def get_BENCH_CI(self):
        return self.__BENCH_CI 
  

  def DATA_store(self,KEY,GEN,POP,F,X,history,problem=None):
        DT_CONF=self.get_DATA_conf()
        DT_CONF.set(KEY,GEN,POP,F)
        DT_CONF.set_METRIC_gen(self.METRIC_gen_evalue(F,X,history,problem))      
        BENCH=self.get_BENCH_conf()
        BENCH.set(problem.get_CACHE().get_BENCH_CI().get_M(),
                                  problem.get_CACHE().get_BENCH_CI().get_D(),
                                  problem.__class__.__name__.split("_")[1],
                                  problem.get_CACHE().get_BENCH_CI().get_P(),
                                  problem.get_CACHE().get_BENCH_CI().get_K(),
                                  problem.get_CACHE().get_BENCH_CI().get_n_ieq_constr(),
                                  problem.get_CACHE().get_BENCH_CI().get_BENCH_Nvar())
        BENCH.set_Nvar(problem.get_CACHE().get_BENCH_CI().get_Nvar())
        self.add_T([DT_CONF,BENCH])


  def METRIC_gen_evalue(self,F,X,history,problem):
        M_GEN=[X,[0],[0],[0],[0],[0],[0],[0],[0]]
        try:
            GEN_Hist = GEN_history(history,F)
            approx_ideal,approx_nadir,hist_F,n_evals,hist_n = GEN_Hist.evaluate()
            GEN_HV=GEN_hypervolume(hist_F,problem.get_CACHE().get_BENCH_CI().get_M(),approx_ideal,approx_nadir)
            GEN_GD=GEN_gd(hist_F,F)
            GEN_GDplus=GEN_gdplus(hist_F,F)
            GEN_IGD=GEN_igd(hist_F,F)
            GEN_IGDplus=GEN_igdplus(hist_F,F)    
            M_GEN = ([X,
                                GEN_HV.evaluate(),
                                GEN_GD.evaluate(),
                                GEN_GDplus.evaluate(),
                                GEN_IGD.evaluate(),
                                GEN_IGDplus.evaluate(),
                                n_evals,
                                hist_F,
                                hist_n])        
        except Exception as e:
            pass
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