from .runner import runner

class RUN(runner):    

    def MOEA_execute(self,result,problem = None, name_moea = None, name_benchmark=None): 
            data = result.edit_DATA_conf().get_DATA_MOEA().exec()
            problem = result.edit_DATA_conf().get_problem()
            GEN_Hist = self.get_history(data[3],[value for key,value in data[0].items()][0])
            approx_ideal,approx_nadir,hist_F,n_evals,hist_n, hist_F_non_dominate, hist_X_non_dominate = GEN_Hist.evaluate()         
            result.DATA_store([key for key,value in data[0].items()][0],
                              data[1],
                              data[2],
                              [value for key,value in data[0].items()][0],
                              hist_F,
                              hist_n,
                              problem,
                              name_benchmark,
                              hist_F_non_dominate,
                              hist_X_non_dominate
                              )
            
        
            

    


        





    