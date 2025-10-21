from .memory import memory


class CACHE_bk_user(memory):

    def set_BENCH_CI(self,name_benchmark = None,M = 0, N=0,n_ieq_constr=0,P=0,K=0):
       BENk=self.get_BENCH_conf()
       BENk.set_user(name_benchmark ,M , N , n_ieq_constr,P,K) 
       self.__BENCH_CI=BENk
    

    def get_BENCH_CI(self):
        return self.__BENCH_CI 

    
    def DATA_store(self,name_benchmark,description,M,N,n_ieq_constr,F,P,K):
        DT_CONF=self.get_DATA_conf()
        DT_CONF.set(description,0,0,F)
        self.set_BENCH_CI(name_benchmark,M, N,n_ieq_constr,P,K)
        BENCH=self.get_BENCH_CI()
        self.clear()
        self.add_T([DT_CONF,BENCH])
    

