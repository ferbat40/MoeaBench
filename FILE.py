from GEN_history import GEN_history
from GEN_hypervolume import GEN_hypervolume
from GEN_gd import GEN_gd
from GEN_gdplus import GEN_gdplus
from GEN_igd import GEN_igd
from GEN_igdplus import GEN_igdplus
from FILE_reference import FILE_reference



class FILE(FILE_reference):

    def __init__(self,CACHE,**kwargs):
        self.__CACHE=CACHE
        super().__init__(**kwargs)


    def SAMPLES_add(self,KEY,GEN,POP,F,X,history):
        DT_CONF=self.__CACHE.get_DATA_conf()
        DT_CONF.set(KEY,GEN,POP,F)
        DT_CONF.set_METRIC_gen(self.METRIC_gen_evalue(F,X,history))      
        BENCH=self.__CACHE.get_BENCH_conf()
        BENCH.set(self.get_BENCH_CI().get_M(),
                                  self.get_BENCH_CI().get_D(),
                                  [key for key,value in self.STR_bench().items() if value == self.get_BENCH_CI().get_BENCH()][0],
                                  self.get_BENCH_CI().get_P(),
                                  self.get_BENCH_CI().get_K(),
                                  self.get_BENCH_CI().get_n_ieq_constr(),
                                  self.get_BENCH_CI().get_BENCH_Nvar())
        BENCH.set_Nvar(self.get_BENCH_CI().get_Nvar())
        self.CREATE(DT_CONF,BENCH)


    def METRIC_gen_evalue(self,F,X,history):
        M_GEN=[X,[0],[0],[0],[0],[0],[0]]
        try:
            GEN_Hist = GEN_history(history,F)
            approx_ideal,approx_nadir,hist_F,n_evals = GEN_Hist.evaluate()
            GEN_HV=GEN_hypervolume(hist_F,self.get_BENCH_CI().get_M(),approx_ideal,approx_nadir)
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
                                n_evals])        
        except Exception as e:
            pass
        return M_GEN