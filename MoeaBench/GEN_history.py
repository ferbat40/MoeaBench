import numpy as np


class GEN_history:

    def __init__(self,history,F,**kwargs):
        self.history=history
        self.F=F
        super().__init__(**kwargs)
     

    def evaluate(self):
        n_evals = []            
        hist_F = []             
        hist_cv = []            
        hist_cv_avg = []  
        hist_N = []
        for i in self.history:
            n_evals.append(i.evaluator.n_eval)
            opt = i.opt
            hist_cv.append(opt.get("CV").min())
            hist_cv_avg.append(i.pop.get("CV").mean())
            feas = np.where(opt.get("feasible"))[0]
            hist_F.append(opt.get("F")[feas])  
            hist_N.append(opt.get("X")[feas])    
        return self.F.min(axis=0),self.F.max(axis=0),hist_F,n_evals,hist_N
    

        
        
     
