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