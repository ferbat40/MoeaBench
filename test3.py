from MoeaBench.base_benchmark import BaseBenchmark
from MoeaBench.base_moea import BaseMoea
from MoeaBench import moeabench
import os







os.system("cls") 


exp2 = moeabench()
exp3 = moeabench()
experiment = moeabench()

from enum import Enum


  

@experiment.benchmark.register_benchmark()
class my_dtlz5(BaseBenchmark):
    
    from enum import Enum
    import numpy as np
    
    
    class E_DTLZ(Enum):
       F1   = 1
       F2   = 2
       F3   = 3
       Fm   = 5
    
    
    def __init__(self,CACHE,M=3,P=150,K=5,n_ieq_constr=1):
        self.M=M
        self.P=P
        self.K=K
        self.n_ieq_constr=n_ieq_constr
        self.llist_E_DTLZ = list(self.E_DTLZ)
        self.N=self.K+self.M-1
        self.CACHE=CACHE


    def get_CACHE(self):
       return self.CACHE


    def constraits(self,f,parameter = 1,f_c=[]):
        f_constraits=self.np.array(f)
        f_c = self.np.array([self.np.sum([ f_c**2  for  f_c in f_constraits[linha,0:f_constraits.shape[1]]])-parameter for index,linha in enumerate(range(f_constraits.shape[0]))  ])
        return f_c

    
    def eval_cons(self,f):
        const_in=[]
        M_constraits = self.constraits(f)
        for (fc,fo) in zip(M_constraits,f):
            if float(fc) == 0:
                const_in.append(fo)
        return self.np.array(const_in)


    def get_Points(self):
        return self.np.array([*self.np.random.random((self.P, self.N))*1.0])
    

    def F1(self,M,th,Gxm): 
       theta = list(map(lambda TH: self.np.cos(TH), th[0:(M-1)]))
       return (1+Gxm)*self.np.prod(self.np.column_stack(theta ), axis = 1).reshape(Gxm.shape[0],1)
   

    def F2(self,M,th,Gxm):
        theta = list(map(lambda TH: self.np.cos(TH), th[0:(M-2)]))
        return (1+Gxm)*self.np.prod(self.np.column_stack(theta ), axis = 1).reshape(Gxm.shape[0],1)*self.np.column_stack(self.np.sin(th[(M-2):(M-1)]))
           

    def F3(self,M,th,Gxm):
        theta = list(map(lambda TH: np.cos(TH), th[0:(M-3)]))
        return (1+Gxm)*self.np.prod(self.np.column_stack(theta ), axis = 1).reshape(Gxm.shape[0],1)*self.np.column_stack(self.np.sin(th[(M-3):(M-2)]))
    

    def Fm(self,M,th,Gxm):
        return (1+Gxm)*self.np.column_stack(self.np.sin(th[0:1]))
    
    
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
        return [X[:,Xi:Xi+1]*self.np.pi/2 if Xi == 0 else (self.np.pi/(4*(1+Gxm))*(1+2*Gxm*X[:,Xi:Xi+1]))  for Xi in range(0,M-1)]
       

    def calc_f(self,X,G):
        vet_F_M = [self.calc_F_M(F,self.M) for F, i in enumerate(range(0,self.M), start = 1)]
        return self.np.column_stack(list(map(lambda Key: self.param_F()[Key](self.M,self.calc_TH(X,G,self.M),G),vet_F_M)))


    def calc_g(self,X):
        return self.np.sum((X[:,self.M-1:]-0.5)**2, axis = 1).reshape(X.shape[0],1)


    def POFsamples(self):
        X = self.get_Points()
        X[:,self.M-1:self.N]=0.5
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
            result["feasible"] = self.np.any((result["G"] <-0.00000000001)  | (result["G"] > 0.00000000001) )        
        return result


@experiment.Moea.register_moea()
class NSGA2deap(BaseMoea):

  import random
  from deap import base, creator, tools, algorithms
  import array
  import numpy as np
  
  def __init__(self,problem=None,population=0,generations=0):
    self.problem=problem
    self.generations=generations
    self.population = population
    self.temp=None
    self.n_ieq= self.problem.get_CACHE().get_BENCH_CI().get_n_ieq_constr()

    self.creator.create("FitnessMin", self.base.Fitness, weights=(-1.0,) * self.problem.get_CACHE().get_BENCH_CI().get_M())
    self.creator.create("Individual", self.array.array, typecode='d', fitness=self.creator.FitnessMin)
    self.toolbox = self.base.Toolbox()
    self.toolbox.register("attr_float", self.uniform, 0, 1,self.problem.get_CACHE().get_BENCH_CI().get_Nvar())
    self.toolbox.register("individual", self.tools.initIterate, self.creator.Individual, self.toolbox.attr_float)
    self.toolbox.register("population", self.tools.initRepeat, list, self.toolbox.individual)
    self.toolbox.register("evaluate",self.evaluate)
    self.evalue = self.toolbox.evaluate
    self.random.seed(None)
    self.toolbox.decorate("evaluate", self.tools.DeltaPenality(self.feasible,1000))
    self.toolbox.register("mate", self.tools.cxSimulatedBinaryBounded, low=0, up=1, eta=20)
    self.toolbox.register("mutate", self.tools.mutPolynomialBounded, low=0, up=1, eta=20, indpb=1/self.problem.get_CACHE().get_BENCH_CI().get_Nvar())
    self.toolbox.register("select", self.tools.selNSGA2)
    

  def uniform(self,low, up, size=None):
    try:
      return [self.random.uniform(a,b) for a,b in zip(low,up)]
    except TypeError as e:
      return [self.random.uniform(a,b) for a,b in zip([low]*size,[up]*size)]


  def evaluate(self,X):
    self.resul = self.problem.evaluation(self.np.array([X]),self.n_ieq)
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
    F_gen_all.append(self.np.column_stack([self.np.array([ind.fitness.values for ind in pop ])]))
    X_gen_all.append(self.np.column_stack([self.np.array([self.np.array(ind) for ind in pop ])]))
    pop = self.toolbox.select(pop, len(pop))
    for gen in range(1, self.generations):
      offspring = self.tools.selTournamentDCD(pop, len(pop))
      offspring = [self.toolbox.clone(ind) for ind in offspring]
      for ind1, ind2 in zip(offspring[::2], offspring[1::2]):
        if self.random.random() <= 0.9:
          self.toolbox.mate(ind1, ind2)
        self.toolbox.mutate(ind1)
        self.toolbox.mutate(ind2)
        del ind1.fitness.values, ind2.fitness.values
      invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
      fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)
      for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit
      pop = self.toolbox.select(pop + offspring, len(pop))
      F_gen_all.append(self.np.column_stack([self.np.array([ind.fitness.values for ind in pop ])]))
      X_gen_all.append(self.np.column_stack([self.np.array([self.np.array(ind) for ind in pop ])]))
    F = self.np.column_stack([self.np.array([ind.fitness.values for ind in pop ])])
    return F_gen_all,X_gen_all,F,self.generations,self.population


experiment.problem = experiment.benchmark.my_new_benchmark()
experiment.moea = experiment.Moea.my_new_moea(problem = experiment.problem,population = 160 ,generations = 300)
experiment.run()


exp3.problem = moeabench.benchmark.DPF5(M=3)
exp3.moea = moeabench.Moea.NSGA3(problem=exp3.problem, population = 100, generations = 200)
exp3.run()



moeabench.plot_hypervolume (experiment.result, exp3.result, generations = [80,300], objectives = [1,3])
#moeabench.pareto(experiment.result, exp3.result, objectives = [1,7,3])

#experiment.save("gavan")
#experiment.load("gavan")

#experiment.save("teste_x")
#exp2.problem = moeabench.benchmark.DPF5(M=3)
#exp2.moea = moeabench.Moea.MOEAD(problem=exp2.problem, population = 130, generations = 200)
#exp2.run()


#exp3.problem = moeabench.benchmark.DPF5(M=3)
#exp3.moea = moeabench.Moea.MOEAD(problem=exp2.problem, population = 130, generations = 200)
#exp3.run()

#



#moeabench.plot_IGDplus(experiment,exp2, exp3, generations = [190,300])

#exp2.problem = moeabench.benchmark.DPF5(M=3)
#exp2.moea = moeabench.Moea.MOEAD(problem=exp2.problem, population = 130, generations = 300)
#exp2.run()

#exp3 = moeabench()
#exp3.problem = moeabench.benchmark.DPF5(M=3)
#exp3.moea = moeabench.Moea.NSGA3(problem=exp3.problem, population = 130, generations = 200)
#exp3.run()
#exp3.save('exp3')
#exp3.load('exp3')


#moeabench.plot_GD(exp2, exp3,  generations = [0,250])

#moeabench.plot_hypervolume(exp, exp3, generations = [89,300])

#test1 so instancias em memoria e não salva

#exp.problem = exp.benchmark.my_new_benchmark()
#exp.moea = exp.Moea.my_new_moea(problem = exp.problem,population = 160 ,generations = 300)
#exp.run()
#exp.save_class()

#exp.save('teste1')
#exp.load('teste1')


#test2 uma instancia moeabench e uma instancia em memoria moea (salvando a classe). Salvando o objeto


#exp.problem = moeabench.benchmark.DTLZ5()
#exp.moea = exp.Moea.my_new_moea(problem = exp.problem,population = 160 ,generations = 500)
#exp.run()
#exp.save_class()

#exp.save('test2')
#exp.load('test2')


#test3 uma instancia moeabench e uma instancia em memoria benchmark (salvando a classe). Salvando o objeto

#exp.problem = exp.benchmark.my_new_benchmark()
#exp.moea = moeabench.Moea.MOEAD(problem=exp.problem, population = 130, generations = 400)
#exp.run()
#exp.save_class()

#exp.save('test3')
#exp.load('test3')



#test4 duas instancias em memoria benchmark e moea (salvando as classes). Salvando o objeto



#experiment.problem = experiment.benchmark.my_new_benchmark()
#experiment.moea = experiment.Moea.my_new_moea(problem = experiment.problem,population = 160 ,generations = 500)
#experiment.run()
#exp.save_class()

#experiment.save('test4')
#exp.load('test4')



#test5 instanciando uma classe benchmark do Moeabench e outra do Moea do usuario e salvando o objeto

#exp = moeabench()

#exp.problem = exp.benchmark.my_implemented_benchmark('my_dtlz5',m = 3, p = 1200, k = 10)
#exp.moea = moeabench.Moea.MOEAD(problem=exp.problem, population = 130, generations = 400)
#exp.run()


#exp.save('test5')
#exp.load('test5')


#test6 instanciando uma classe moea do usuario e outra do benchmark do Moeabench e salvando o objeto

#exp.problem = moeabench.benchmark.DTLZ5()
#exp.moea = moeabench.Moea.my_implemented_moea('NSGA2deap',problem=exp.problem, population = 160, generations = 400)
#exp.run()


#exp.save('test6')
#exp.load('test6')


#test7 instanciando uma classe moea do usuario e outra do benchmark do usuario e salvando o objeto

#exp = moeabench()
#exp.problem = exp.benchmark.my_implemented_benchmark('my_dtlz5',m = 3, p = 1200, k = 10)
#exp.moea = moeabench.Moea.my_implemented_moea('NSGA2deap',problem=exp.problem, population = 160, generations = 400)
#exp.run()


#exp.save('test7')
#exp.load('test7')








#exp.load('test4')
