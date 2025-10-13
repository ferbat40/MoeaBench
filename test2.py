from MoeaBench.base_moea import BaseMoea
from deap import base, creator, tools, algorithms
import numpy as np
import array
import random
from MoeaBench import moeabench
import os



os.system("cls")  

exp  = moeabench()

@exp.Moea.register_moea()
class NSGA2deap(BaseMoea):
  def __init__(self,problem,population,generations):
    self.problem=problem
    self.generations=generations
    self.population = population
    self.temp=None
    self.n_ieq= self.problem.get_CACHE().get_BENCH_CI().get_n_ieq_constr()
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,) * self.problem.get_CACHE().get_BENCH_CI().get_M())
    creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin)
    self.toolbox = base.Toolbox()
    self.toolbox.register("attr_float", self.uniform, 0, 1,self.problem.get_CACHE().get_BENCH_CI().get_Nvar())
    self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.attr_float)
    self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
    self.toolbox.register("evaluate",self.evaluate)
    self.evalue = self.toolbox.evaluate
    random.seed(None)
    self.toolbox.decorate("evaluate", tools.DeltaPenality(self.feasible,1000))
    self.toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=0, up=1, eta=20)
    self.toolbox.register("mutate", tools.mutPolynomialBounded, low=0, up=1, eta=20, indpb=1/self.problem.get_CACHE().get_BENCH_CI().get_Nvar())
    self.toolbox.register("select", tools.selNSGA2)
    

  def uniform(self,low, up, size=None):
    try:
      return [random.uniform(a,b) for a,b in zip(low,up)]
    except TypeError as e:
      return [random.uniform(a,b) for a,b in zip([low]*size,[up]*size)]


  def evaluate(self,X):
    self.resul = self.problem.evaluation(np.array([X]),self.n_ieq)
    return self.resul['F'][0]


  def feasible(self,X):
    self.evaluate(X)
    if 'G' in self.resul:
      if self.resul["feasible"]:
       return True
    return False


  def evaluation(self):
    pop = self.toolbox.population(n=self.population)
    invalid_ind = [ind for ind in pop if not ind.fitness.valid]
    fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)
    F_gen_all=[]
    X_gen_all=[]
    for ind, fit in zip(invalid_ind, fitnesses):
      ind.fitness.values = fit
    F_gen_all.append(np.column_stack([np.array([ind.fitness.values for ind in pop ])]))
    X_gen_all.append(np.column_stack([np.array([np.array(ind) for ind in pop ])]))
    pop = self.toolbox.select(pop, len(pop))
    for gen in range(1, self.generations):
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
    return F_gen_all,X_gen_all,F,self.generations,self.population
 

exp.problem = moeabench.benchmark.DTLZ1()
exp.moea = exp.Moea.my_new_moea(problem = exp.problem,population = 160 ,generations = 500)
#exp.moea = moeabench.Moea.NSGA3(problem=exp.problem, population = 130, generations = 500)
exp.run()



