from .RUN import RUN
from .RUN_user import RUN_user
from .result_metric import result_metric
from .result_obj import result_obj
from .result_var import result_var
from .save import save
from .loader import loader
from .I_UserExperiment import I_UserExperiment
import inspect


class experiment(I_UserExperiment):

    def __init__(self, imports):
        self.pof=None
        self.result=None
        self.imports = imports
        self.result_metric=result_metric()
        self.result_obj=result_obj()
        self.result_var=result_var()
    

    @property
    def moea(self):
        return self._moea
    

    @moea.setter
    def moea(self,value):  
        self.result = value(self.benchmark, self.imports.moeas) if callable(value) else value
        self._moea = value


    @property
    def benchmark(self):
        return self._benchmark
    

    @benchmark.setter
    def benchmark(self,value):
        self._benchmark=value(self.imports.benchmarks) if callable(value) else value
        self.pof=self._benchmark 
      

    def hypervolume(self, generations = [], objectives = []):
        """
        - **array with hypervolume in generations:**
        Click on the links for more
        ...
                - **Informations:**
                      - sinxtase:
                      experiment.hypervolume(args)  
                      - [hypervolume](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/hypervolume/) information about the method, examples and more...   
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types

        """
        try:
            return self.result_metric.IPL_hypervolume(self.result, generations, objectives)
        except Exception as e:
            print(e)
     

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
            return self.result_metric.IPL_GD(self.result, generations, objectives)
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
            return self.result_metric.IPL_GDplus(self.result, generations, objectives)
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
            return self.result_metric.IPL_IGD(self.result, generations, objectives)
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
            return self.result_metric.IPL_IGDplus(self.result, generations, objectives)
        except Exception as e:
            print(e)

            
    def objective(self, objective = 1, generations = []):
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
            return self.result_obj.IPL_objectives(self.result, generations, objective)
        except Exception as e:
            print(e)


    def variable(self, variable = 1, generations = []):
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
            return self.result_var.IPL_variables(self.result, generations, variable)
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
        #try:
        save.IPL_save(self,file)
        #except Exception as e:
           # print(e)


    def run(self):
        """
        - **run the genetic algorithm:**
        Click on the links for more
        ...
               - **Informations:**
                      - sinxtase:
                      experiment.run()   
                      - [run()](https://moeabench-rgb.github.io/MoeaBench/experiments/combinations/combinations/#moeabench-run-the-experiment) Information about the method and return variables.

        """
        if isinstance(self.result,tuple):
            name_moea = self.result[2]
        else:
            name_moea = self.result.edit_DATA_conf().get_DATA_MOEA().__class__.__name__       
        try:
            moea_found = self.imports.moeas.moea_algorithm()
            algoritm = moea_found.get_MOEA(self.moea.__class__.__name__)
            execute = RUN() if not isinstance(algoritm, bool ) and not inspect.isclass(algoritm[0]) else RUN_user()
            print(execute)
            result_moea = self.result[0] if isinstance(self.result,tuple) else self.result
            name_benchmark=None
            print(result_moea.get_elements()," sdf")
            try:
                name_benchmark = self.benchmark.__class__.__name__.split("_")[1]
            except Exception as e:
                name_benchmark = self.benchmark.__class__.__name__
                
            return execute.MOEA_execute(result_moea,self.benchmark,name_moea,name_benchmark)
        except Exception as e:
            print(e)
