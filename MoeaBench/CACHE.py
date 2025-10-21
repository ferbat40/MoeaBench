from .memory import memory


class CACHE(memory):
  
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
             pass
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


  
  

 