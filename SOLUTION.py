class SOLUTION:


    def SOLVER(self,
               problem,
               Benckmark,
               M,
               D,
               K,
               N,
               MOEA,
               metrics,
               generations,
               population):
          
          try:
              problem.get_ENGINE().allowed_result(MOEA,metrics[0],generations,population) 
              DT_CONF=problem.get_ENGINE().memory().get_DATA_conf()
              DT_CONF.set(MOEA,generations,population,metrics[0])
              problem.get_ENGINE().allowed_bench(Benckmark,D,K,N)
              BENCH=problem.get_ENGINE().memory().get_BENCH_conf()
              BENCH.set(M,D,Benckmark,0,K,0,0)
              BENCH.set_Nvar(N)
              M_GEN=[metrics[i] for i in range(1,8)]
              DT_CONF.set_METRIC_gen(M_GEN)
              problem.get_ENGINE().CREATE(DT_CONF,BENCH)    
          except Exception as e:
              print(e)


    def exec(self):
        raise NotImplementedError("Not implemented")


    
    