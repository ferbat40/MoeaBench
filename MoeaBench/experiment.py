from .RUN import RUN
from .RUN_user import RUN_user
from .result_metric import result_metric
from .result_obj import result_obj
from .result_front import result_front
from .result_var import result_var
from .result_set import result_set
from .save import save
from .loader import loader
from .I_UserExperiment import I_UserExperiment
import inspect
import numpy as np


class experiment(I_UserExperiment):

    def __init__(self, imports):
        self.pof=None
        self.result=None
        self.imports = imports
        self.result_obj=result_obj()
        self.result_front=result_front()
        self.result_var=result_var()
        self.result_set=result_set()
        self.hist_M_user = []
    
    
    @property
    def round(self):
        return self._round
    

    @round.setter
    def round(self, value):
        if not hasattr(self,'_round'):
            self._round = []
        self._round.extend(value)


    @property
    def stop(self):
        return self._stop
    

    @stop.setter
    def stop(self, value):
        self._stop = value


    @property
    def optimal(self):
        return self.imports.optimal.optimal(self)
    

    @property
    def dominated(self):
        return self.imports.dominated.dominated(self)


    @optimal.setter
    def optimal(self, value):
        self._optimal = value


    @property
    def moea(self):
        return self._moea
    

    @moea.setter
    def moea(self,value):  
        stop = self.stop if hasattr(self,'_stop') else None
        self.result = value(self, self.imports.moeas, stop) if callable(value) else value
        self._moea = value


    @property
    def benchmark(self):
        return self._benchmark
      

    @benchmark.setter
    def benchmark(self,value):
        self._benchmark=value(self.imports.benchmarks) if callable(value) else value
        self.pof=self._benchmark 


    def GD(self, generations = [], objectives = []):
        """
        - **array with GD in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.GD(args)  
                      - [GD](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/GD/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return result_metric.IPL_GD(self.result, generations, objectives)
        except Exception as e:
            print(e)


    def GDplus(self, generations = [], objectives = []):
        """
        - **array with GD+ in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.GDplus(args)  
                      - [GDplus](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/GDplus/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return result_metric.IPL_GDplus(self.result, generations, objectives)
        except Exception as e:
            print(e)
    

    def IGD(self, generations = [], objectives = []):
        """
        - **array with IGD in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.IGD(args)  
                      - [IGD](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/IGD/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return result_metric.IPL_IGD(self.result, generations, objectives)
        except Exception as e:
            print(e)
    

    def IGDplus(self, generations = [], objectives = []):
        """
        - **array with IGD+ in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.IGDplus(args)  
                      - [IGDplus](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/IGDplus/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return result_metric.IPL_IGDplus(self.result, generations, objectives)
        except Exception as e:
            print(e)

            
    def objectives(self, generation = None):
        """
        - **array with objectives in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.objective(args)  
                      - [objective](https://moeabench-rgb.github.io/MoeaBench/analysis/objectives/data/objective/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return self.result_obj.IPL_objectives(self.result, generation)
        except Exception as e:
            print(e)


    def front(self, generation = None):
        try:
            return self.result_front.IPL_front(self.result, generation)
        except Exception as e:
            print(e)


    def variables(self, generation = None):
        """
        - **array with decision variables in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.variable(args)  
                      - [variable](https://moeabench-rgb.github.io/MoeaBench/analysis/variables/data/variable/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return self.result_var.IPL_variables(self.result, generation)
        except Exception as e:
            print(e)
    

    def set(self, generation = None):
        try:
            return self.result_set.IPL_set(self.result, generation)
        except Exception as e:
            print(e)


    def load(self,file):
        """
        - **Loads a user experiment into MoeaBench:**
        Click on the links for more
        ...
                - Informations:
                      - sinxtase:
                      experiment.load(nameFile)  
                      - [load](https://moeabench-rgb.github.io/MoeaBench/experiments/load_experiment/load_experiment/) information about the method, 
                     
        """
        try:
            loader.IPL_loader(self,file)    
            if isinstance(self.result,tuple):
                self.result = self.result[0]  
        except Exception as e:
            print(e)


    def save(self, file):
        """
        - **save the user's experiment in a zip file:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.save(nameFile)  
                      - [save](https://moeabench-rgb.github.io/MoeaBench/experiments/save_experiment/save_experiment/) information about the method, 
                     
        """
        algoritm = None
        if (hasattr(self,'_moea')):
            moea_found = self.imports.moeas.moea_algorithm()
            algoritm = moea_found.get_MOEA(self.moea.__class__.__name__)
        try:
            if isinstance(algoritm,tuple) and inspect.isclass(algoritm[0]):
                raise ValueError("experiments using the methods @mb.benchmarks.register_benchmark() and @mb.moeas.register_moea() cannot be saved.")
            save.IPL_save(self,file)
        except Exception as e:
            print(e)
   

    def run_moea(self, seed):

        if isinstance(self.result,tuple):
            name_moea = self.result[2]
        else:
            name_moea = self.result.edit_DATA_conf().get_DATA_MOEA().__class__.__name__       
        try:
            moea_found = self.imports.moeas.moea_algorithm()
            algoritm = moea_found.get_MOEA(self.moea.__class__.__name__)
            execute = RUN() if not isinstance(algoritm, bool ) and not inspect.isclass(algoritm[0]) else RUN_user()
            
            if isinstance(execute, RUN_user):
                self.hist_M_user.append(self.benchmark.M)
                self.result = self.moea(self.benchmark, self.imports.moeas) if not len(set(self.hist_M_user)) == 1 else self.result
                         
            elif isinstance(execute, RUN):
                stop = self.stop if hasattr(self,'_stop') else None
                self.result = self.moea(self, None, stop, seed) 
            
            self.result_moea = self.result[0] if isinstance(self.result,tuple) else self.result
            try:
                name_benchmark = self.benchmark.__class__.__name__.split("_")[1]
            except Exception as e:
                name_benchmark = self.benchmark.__class__.__name__
                
            return execute.MOEA_execute(self.result_moea,name_moea,name_benchmark)
        except Exception as e:
            print(e)

    
    def run(self, repeat = 0):
        """
        - **run the genetic algorithm:**
        Click on the links for more
        ...
               - **Informations:**
                      - sinxtase:
                      experiment.run()   
                      - [run()](https://moeabench-rgb.github.io/MoeaBench/experiments/combinations/combinations/#moeabench-run-the-experiment) Information about the method and return variables.

        """
        try:
            generator = np.random.default_rng()
            if not isinstance(repeat,int):
                raise TypeError('Only integers are allowed as parameters for the run() method.')
       
            execution = repeat-1 if repeat > 0 else 0
            for exe in range(0,execution):
                self.run_moea(generator)
                self.round = [b.get_F_GEN()[-1] for i in self.result.get_elements() for b in i if hasattr(b,'get_F_GEN')]
            seed_moea = generator if self.moea.seed == 0 else self.moea.seed
            self.run_moea(seed_moea)
            self.round = [b.get_F_gen_non_dominate()[-1] for i in self.result.get_elements() for b in i if hasattr(b,'get_F_GEN')]
        except Exception as e:
            print(e)


           
           