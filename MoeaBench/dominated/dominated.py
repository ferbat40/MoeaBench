from ..result import result

class dominated(result):

    def __init__(self, experiment):
        self.experiment = experiment


    def objectives(self, generations = None):
        return self.DATA([dt.get_F_gen_dominate() 
                          for data in self.experiment.result.get_elements() 
                          for dt in data 
                          if hasattr(dt,"get_F_gen_dominate")][0],generations)    


    def variables(self, generations = None):
        return self.DATA([dt.get_X_gen_dominate() 
                          for data in self.experiment.result.get_elements() 
                          for dt in data 
                          if hasattr(dt,"get_X_gen_dominate")][0],generations)    