from .CACHE import CACHE
from .BENCH_conf import BENCH_conf


class CACHE_bk_user(CACHE):


    def get_BENCH_conf(self,name_benchmark = None,M = 0, N=0,n_ieq_constr=0):
       self.bench_conf=BENCH_conf(name_benchmark ,M , N , n_ieq_constr)
       return self.bench_conf

    
    def DATA_store(self,name_benchmark,description,M,N,n_ieq_constr,F):
        DT_CONF=self.get_DATA_conf()
        DT_CONF.set(description,0,0,F)
        BENCH=self.get_BENCH_conf(name_benchmark,M, N,n_ieq_constr)
        self.clear()
        self.add_T([DT_CONF,BENCH])
    

