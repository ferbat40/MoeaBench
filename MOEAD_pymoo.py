from pymoo.optimize import minimize
import numpy as np
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PolynomialMutation
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.moead import MOEAD
from pymoo.decomposition.pbi import PBI



class MOEADpymoo(Problem):
    def __init__(self,benchmark,population,generations,seed):
        self.benchmark=benchmark
        self.population=population
        self.generations=generations
        self.seed=seed
        self.Nvar=self.benchmark.get_ENGINE().get_BENCH_CI().get_Nvar()
        self.M=self.benchmark.get_ENGINE().get_BENCH_CI().get_M()
        self.BENCH_Nvar=self.benchmark.get_ENGINE().get_BENCH_CI().get_BENCH_Nvar()
        xl = np.full(self.Nvar,0)
        xu = np.full(self.Nvar,1)
        self.objectives = self.M
        super(). __init__(n_var=self.Nvar, n_obj=  self.objectives, xl=xl, xu=xu)

         
    def _evaluate(self, x, out, *args, **kwargs):   
        N_Bench = self.BENCH_Nvar
         
        if N_Bench <=7 or N_Bench >= 10:
            Gxm=self.benchmark.calc_g(x)
            F=self.benchmark.calc_f(x,Gxm)
            out["F"]=F
            

        elif N_Bench==8 or N_Bench==9:
            F=self.benchmark.calc_gijx(x)


    def exec(self):
        ref_dirs = get_reference_directions("energy", self.objectives, self.population, seed = self.seed)  
        muttation_prob = 1/self.Nvar
        muttation=PolynomialMutation(prob=muttation_prob, eta = 20)
        crossover = SBX(prob=1.0, eta=15)
        algorithm_MOEAD = MOEAD(ref_dirs, crossover=crossover,mutation=muttation, decomposition=PBI(eps=0.0, theta=5))      
        res_MOEAD = minimize(
            MOEADpymoo(self.benchmark,self.population, self.generations,self.seed),
            algorithm_MOEAD,
            termination=('n_gen', self.generations),
    
            seed=self.seed,
            save_history=True,
            verbose=False
            )          
        MOEAD_algorithm={
            "MOEAD" :np.column_stack([res_MOEAD.F])
        }    
        return (MOEAD_algorithm,self.generations,self.population,res_MOEAD.history,res_MOEAD.X)
    

    def SOLVER(self):
        raise NotImplementedError("Not implemented")