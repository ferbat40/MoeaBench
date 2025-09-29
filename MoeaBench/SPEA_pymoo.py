from pymoo.algorithms.moo.spea2 import SPEA2
from pymoo.optimize import minimize
import numpy as np
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PolynomialMutation
from pymoo.core.problem import Problem
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.indicators.hv import HV


class SPEAPymoo(Problem):
    def __init__(self,benchmark,population,generations,seed):
        self.benchmark=benchmark
        self.population=population
        self.generations=generations
        self.seed=seed
        self.n_ieq=self.benchmark.get_ENGINE().get_BENCH_CI().get_n_ieq_constr()
        self.Nvar=self.benchmark.get_ENGINE().get_BENCH_CI().get_Nvar()
        self.M=self.benchmark.get_ENGINE().get_BENCH_CI().get_M()
        self.BENCH_Nvar=self.benchmark.get_ENGINE().get_BENCH_CI().get_BENCH_Nvar()
        xl = np.full(self.Nvar,0)
        xu = np.full(self.Nvar,1)
        super().__init__(n_var=self.Nvar, n_obj=self.M, n_ieq_constr=self.n_ieq, xl=xl, xu=xu)
    
    def _evaluate(self, x, out, *args, **kwargs):   
        N_Bench = self.BENCH_Nvar
   
        if N_Bench <=7 or N_Bench >= 10:
            Gxm=self.benchmark.calc_g(x)
            F=self.benchmark.calc_f(x,Gxm)
            out["F"]=F
            if self.n_ieq != 0:  
                out["G"]=self.benchmark.constraints(F)


        elif N_Bench==8 or N_Bench==9:
            F=self.benchmark.calc_f(x)
            out["F"]=F
            G = self.benchmark.calc_gijx(F)
            out["G"]=-G


    def exec(self):
        ref_dirs = get_reference_directions("energy", self.M, self.population, seed = self.seed)
        mutation_prob=1/self.Nvar
        mutation = PolynomialMutation(prob=mutation_prob, eta=20)
        crossover = SBX(prob=1.0, eta=15)
        algorithm_spea = SPEA2(ref_dirs=ref_dirs,pop_size=self.population,crossover=crossover,mutation=mutation)
            
        res_SPEA = minimize(
            SPEAPymoo(self.benchmark,self.population, self.generations,self.seed),
            algorithm_spea,
            termination=('n_gen', self.generations),
            seed=self.seed,
            save_history=True,
            verbose=False
            )      
        

        SPEA_algorithm={
            "SPEA-2" :np.column_stack([res_SPEA.F])
        }   
        return (SPEA_algorithm,self.generations,self.population,res_SPEA.history,res_SPEA.X)
    
    
    def SOLVER(self):
        raise NotImplementedError("Not implemented")
