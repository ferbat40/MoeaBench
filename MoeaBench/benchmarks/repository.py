class repository:
        
        def add_benchmark(self, bench):
          samples = bench.benchmark.POFsamples()
          bench.get_CACHE().DATA_store(bench.__class__.__name__,bench.get_type(),bench.get_M(),bench.get_N(),bench.get_n_ieq_constr(),samples,bench.get_P() ,bench.get_K())
          return bench
        
         
  

        

    