from .RUN import RUN
from .RUN_user import RUN_user


class experiment:

    def __init__(self, imports):
        self.pof=None
        self.result=None
        self.imports = imports


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
            name_benchmark=None
            execute = RUN() if self.moea.__module__.find(".moea") >= 0 else RUN_user()
            self.result = self.result[0] if isinstance(self.result,tuple) else self.result

            try:
                name_benchmark = self.benchmark.__class__.__name__.split("_")[1]
            except Exception as e:
                name_benchmark = self.benchmark.__class__.__name__
                
            return execute.MOEA_execute(self.result,self.benchmark,name_moea,name_benchmark)
        except Exception as e:
            print(e)
