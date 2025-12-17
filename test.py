from MoeaBench import mb
import os, importlib
import numpy as np


os.system("cls")  


def stop(experiment):
    metric = mb.hypervolume.trace(experiment)
    hv = metric[0]
    if len(hv)  % 20 == 0:
        gen = np.diff(hv[ -21:  ])
        mean = np.mean(np.abs(gen))
        std_gen = np.std(gen)
        return mean < 1e-3 and std_gen < 1e-3 
 
       

exp = mb.experiment()
exp.benchmark = mb.benchmarks.DTLZ1()
exp.moea = mb.moeas.MOEAD(generations = 10, population = 150)
exp.moea.generations=300
#exp.moea.seed = 4
exp.stop = stop
exp.run()

var = exp.variables() 
#print(var)

#exp.save('crof')
#exp.load('crof')
#hv  = mb.hypervolume(exp) 
#print(hv)
#print(hv)


#exp.save("machine")
#exp.load("machine")





#exp2 = mb.experiment()
#exp2.benchmark = mb.benchmarks.DTLZ1()
#exp2.moea = mb.moeas.SPEA2(generations = 50, population = 50)
#exp2.run()

#ref = [exp, exp2]
#h = mb.hypervolume.trace(exp, reference=ref)
#print(h)


#hv  = mb.hypervolume(exp)   
#print(hv)
#ref = [exp, exp2]

#mb.plot_GD(exp, generations = [0,90], objectives = [1,4])
#mb.plot_IGDplus(exp, generations = [0,90], objectives = [1,3])
#mb.hypervolume.timeplot (exp, reference = ref)
#mb.hypervolume.timeplot (exp)

#mb.spaceplot(exp.optimal.front(), exp2, exp.objectives(), exp2.front(generations = 100),exp,exp2,exp2.optimal.front(), exp.objectives(), exp)

#print(exp.objectives().__class__.__name__)


#hy_arr_ref = mb.hypervolume.trace(exp, objectives = [1,3],  reference = ref)
#print(hy_arr_ref)


#hy_arr = mb.hypervolume.trace(exp, objectives = [1,3] )
#print(hy_arr)




#hv = mb.hypervolume(hy_arr_ref, generation = 90)
#print(hv)


#hv = mb.hypervolume(hy_arr, generation = 90)
#print(hv)


#hv_obj = mb.hypervolume(exp)
#print(hv_obj)