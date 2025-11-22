from MoeaBench.base_benchmark import BaseBenchmark
from enum import Enum
import numpy as np
import os
from MoeaBench import moeabench




os.system("cls")  






class E_DTLZ(Enum):
       F1   = 1
       F2   = 2
       F3   = 3 
       Fm   = 5

@moeabench.benchmarks.register_benchmark()
class dtlz5(BaseBenchmark):

    def __init__(self, type : str = None, M : int = 3, P : int = 700, K : int = 10, N : int = 0, D : int = 2, n_ieq_constr : int = 1):
        N=K+M-1
        super().__init__(type, M, P, K, N, n_ieq_constr)
        self.llist_E_DTLZ = list(E_DTLZ)


    def constraits(self,f,parameter = 1,f_c=[]):
        f_constraits=np.array(f)
        f_c = np.array([np.sum([ f_c**2  for  f_c in f_constraits[linha,0:f_constraits.shape[1]]])-parameter for index,linha in enumerate(range(f_constraits.shape[0]))  ])
        return f_c


    def eval_cons(self,f):
        M_constraits = self.constraits(f)
        eval = M_constraits == 0
        return f[eval]


    def get_Points(self):
        return np.array([*np.random.random((self.get_P(), self.get_N()))*1.0])


    def F1(self,M,th,Gxm):
       theta = list(map(lambda TH: np.cos(TH), th[0:(M-1)]))
       return (1+Gxm)*np.prod(np.column_stack(theta ), axis = 1).reshape(Gxm.shape[0],1)


    def F2(self,M,th,Gxm):
        theta = list(map(lambda TH: np.cos(TH), th[0:(M-2)]))
        return (1+Gxm)*np.prod(np.column_stack(theta ), axis = 1).reshape(Gxm.shape[0],1)*np.column_stack(np.sin(th[(M-2):(M-1)]))


    def F3(self,M,th,Gxm):
        theta = list(map(lambda TH: np.cos(TH), th[0:(M-3)]))
        return (1+Gxm)*np.prod(np.column_stack(theta ), axis = 1).reshape(Gxm.shape[0],1)*np.column_stack(np.sin(th[(M-3):(M-2)]))


    def Fm(self,M,th,Gxm):
        return (1+Gxm)*np.column_stack(np.sin(th[0:1]))


    def get_method(self,enum):
        return self.llist_E_DTLZ[enum]


    def param_F(self):
        dict_F = {
                    self.get_method(0) : self.F1,
                    self.get_method(1) : self.F2,
                    self.get_method(2) : self.F3,
                    self.get_method(3) : self.Fm
                  }
        return dict_F


    def calc_F_M(self,Fi,M):
        if Fi == 1:
            return self.get_method(0)
        elif Fi == 2 and M > 2:
            return self.get_method(1)
        elif Fi >= 3 and Fi <= M-1 and M > 3:
            return self.get_method(2)
        elif Fi == M:
            return self.get_method(3)


    def calc_TH(self,X,Gxm,M):
        return [X[:,Xi:Xi+1]*np.pi/2 if Xi == 0 else (np.pi/(4*(1+Gxm))*(1+2*Gxm*X[:,Xi:Xi+1]))  for Xi in range(0,M-1)]


    def calc_f(self,X,G):
        vet_F_M = [self.calc_F_M(F,self.get_M()) for F, i in enumerate(range(0,self.get_M()), start = 1)]
        return np.column_stack(list(map(lambda Key: self.param_F()[Key](self.get_M(),self.calc_TH(X,G,self.get_M()),G),vet_F_M)))


    def calc_g(self,X):
        return np.sum((X[:,self.get_M()-1:]-0.5)**2, axis = 1).reshape(X.shape[0],1)


    def POFsamples(self):
        X = self.get_Points()
        X[:,self.get_M()-1:self.get_N()]=0.5
        G = self.calc_g(X)
        F = self.eval_cons(self.calc_f(X,G))
        return F


    def evaluation(self,x,n_ieq):
        G=self.calc_g(x)
        F=self.calc_f(x,G)
        result =  {"F" : F}
        if n_ieq != 0:
            cons = self.constraits(F,1.25)
            const  = cons.reshape(cons.shape[0],1)
            result["G"] = const
            result["feasible"] = np.any((result["G"] <-0.00000000001)  | (result["G"] > 0.00000000001) )
        return result




from MoeaBench.base_moea import BaseMoea
import random
from deap import base, creator, tools, algorithms
import array
import numpy as np

@moeabench.moeas.register_moea()
class NSGA2deap(BaseMoea):

  def __init__(self,problem=None,population = 160 ,generations = 300):
    super().__init__(problem,population,generations)
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,) * self.get_M())
    creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin)
    self.toolbox = base.Toolbox()
    self.toolbox.register("attr_float", self.uniform, 0, 1, self.get_N())
    self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.attr_float)
    self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
    self.toolbox.register("evaluate",self.evaluate)
    self.evalue = self.toolbox.evaluate
    random.seed(None)
    self.toolbox.decorate("evaluate", tools.DeltaPenality(self.feasible,1000))
    self.toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=0, up=1, eta=20)
    self.toolbox.register("mutate", tools.mutPolynomialBounded, low=0, up=1, eta=20, indpb=1/self.get_N())
    self.toolbox.register("select", tools.selNSGA2)


  def uniform(self,low, up, size=None):
    try:
      return [random.uniform(a,b) for a,b in zip(low,up)]
    except TypeError as e:
      return [random.uniform(a,b) for a,b in zip([low]*size,[up]*size)]


  def evaluate(self,X):
    self.resul = self.evaluation_benchmark(X)
    return self.resul['F'][0]


  def feasible(self,X):
    self.evaluate(X)
    if 'G' in self.resul:
      if self.resul["feasible"]:
       return True
    return False


  def evaluation(self):
    pop = self.toolbox.population(n=self.get_population())
    invalid_ind = [ind for ind in pop if not ind.fitness.valid]
    fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)
    F_gen_all=[]
    X_gen_all=[]
    for ind, fit in zip(invalid_ind, fitnesses):
      ind.fitness.values = fit
    F_gen_all.append(np.column_stack([np.array([ind.fitness.values for ind in pop ])]))
    X_gen_all.append(np.column_stack([np.array([np.array(ind) for ind in pop ])]))
    pop = self.toolbox.select(pop, len(pop))
    for gen in range(1, self.get_generations()):
      offspring = tools.selTournamentDCD(pop, len(pop))
      offspring = [self.toolbox.clone(ind) for ind in offspring]
      for ind1, ind2 in zip(offspring[::2], offspring[1::2]):
        if random.random() <= 0.9:
          self.toolbox.mate(ind1, ind2)
        self.toolbox.mutate(ind1)
        self.toolbox.mutate(ind2)
        del ind1.fitness.values, ind2.fitness.values
      invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
      fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)
      for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit
      pop = self.toolbox.select(pop + offspring, len(pop))
      F_gen_all.append(np.column_stack([np.array([ind.fitness.values for ind in pop ])]))
      X_gen_all.append(np.column_stack([np.array([np.array(ind) for ind in pop ])]))
    F = np.column_stack([np.array([ind.fitness.values for ind in pop ])])
    return F_gen_all,X_gen_all,F,self.get_generations(),self.get_population()
  
#exp = moeabench()
#exp.benchmark = moeabench.benchmarks.DTLZ8()
#exp.moea = moeabench.moeas.NSGAIII()
#exp.run()
#exp.save("dragon")


#exp.load("dragon")


exp2 = moeabench()
exp2.benchmark= moeabench.benchmarks.my_new_benchmark()
exp2.moea = moeabench.moeas.my_new_moea()
exp2.run()
exp2.save("pegasu")
exp2.load("pegasu")

#experiment10.save("gav")
#kamen = moeabench()
#kamen.load("gav")



#HV_all = kamen.hypervolume()
#print(HV_all)

#print(len(obj), "   ",len(obj[1]F))
#IGD_2_3 = exp3.IGD(generations = [50,60], objectives =  [2,3,3,3])







