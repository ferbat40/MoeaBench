import numpy as np
from BENCH_conf import BENCH_conf
from DATA_conf import DATA_conf
from DATA_arr import DATA_arr


class CACHE(DATA_arr):
  
  def __init__(self,**kwargs):
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
  

  def get_DATA_conf(self):
       return DATA_conf()
  

  def get_BENCH_conf(self):
       return BENCH_conf()
  

  def allowed_DATA(self,LIST):
        DATA = [self.DATA_conf_recursive(OBJ) for OBJ in LIST] 
        INF = [f'{IDATA.get_description()}' for IDATA in DATA if np.isinf(IDATA.get_arr_DATA()).any()] 
        if len(INF) > 0:
            raise ValueError(f'There are matrices with invalid values: '+",".join(f'{i}' for i in INF))