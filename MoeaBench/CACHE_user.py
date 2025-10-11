from .CACHE import CACHE
from .GEN_history import GEN_history
from .GEN_hypervolume import GEN_hypervolume
from .GEN_gd import GEN_gd
from .GEN_gdplus import GEN_gdplus
from .GEN_igd import GEN_igd
from .GEN_igdplus import GEN_igdplus


class CACHE_user(CACHE):

     def DATA_store(self,name_moea,generations,population,F,F_gen,X_gen,problem):
        evals = [population *gen  for gen in range(0,generations)]
        DT_CONF=self.get_DATA_conf()
        DT_CONF.set(name_moea,generations,population,F)
        DT_CONF.set_METRIC_gen(self.METRIC_gen_evalue(F,F_gen,X_gen,evals))      
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


     def METRIC_gen_evalue(self,F,F_gen,X_gen,evals):
        M_GEN=None
        try:
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
        except Exception as e:
            pass
        return M_GEN