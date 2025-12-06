from pymoo.algorithms.moo.unsga3 import UNSGA3
from pymoo.optimize import minimize
import numpy as np
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PolynomialMutation
from pymoo.core.problem import Problem


class UNSGA_pymoo(Problem):
    def __init__(self,benchmark,population,generations,seed):
        self.benchmark=benchmark
        self.population=population
        self.generations=generations
        self.seed=seed
        self.n_ieq=self.benchmark.get_CACHE().get_BENCH_CI().get_n_ieq_constr()
        self.Nvar=self.benchmark.get_CACHE().get_BENCH_CI().get_Nvar()
        self.M=self.benchmark.get_CACHE().get_BENCH_CI().get_M()
        xl = np.full(self.Nvar,0)
        xu = np.full(self.Nvar,1)
        super(). __init__(n_var=self.Nvar, n_obj=self.M, n_ieq_constr=self.n_ieq, xl=xl, xu=xu)
       
       
    def _evaluate(self, x, out, *args, **kwargs):   
        result = self.benchmark.evaluation(x,self.n_ieq)
        out["F"]=result['F']
        if "G" in result:
            out["G"]=result['G']
           
       
    def exec(self):
        ref_dirs = get_reference_directions("energy", self.M, self.population, seed = self.seed)
        muttation_prob = 1/self.Nvar
        muttation=PolynomialMutation(prob=muttation_prob, eta = 20)
        crossover = SBX(prob=1.0, eta=15)
        AUNSGA = UNSGA3(ref_dirs=ref_dirs, pop_size=self.population, crossover=crossover,mutation=muttation)     
        res_UNSGA = minimize(
            UNSGA_pymoo(self.benchmark,self.population, self.generations,self.seed),
            AUNSGA,
            termination=('n_gen', self.generations),
            seed=self.seed,
            save_history=True,
            verbose=False
            )  

        UNSGA_algorithm={
            "U-NSGA3" :np.column_stack([res_UNSGA.F])
        }    
        return(UNSGA_algorithm,self.generations,self.population,res_UNSGA.history,res_UNSGA.X)
    
