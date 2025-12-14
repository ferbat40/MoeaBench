from ..result_population import result_population

class dominated(result_population):

    def __init__(self, experiment):
        self.experiment = experiment


    def objectives(self, generation = None):
        return self.DATA([dt.get_F_gen_dominate() 
                          for data in self.experiment.result.get_elements() 
                          for dt in data 
                          if hasattr(dt,"get_F_gen_dominate")][0],generation)    


    def variables(self, generation = None):
        return self.DATA([dt.get_X_gen_dominate() 
                          for data in self.experiment.result.get_elements() 
                          for dt in data 
                          if hasattr(dt,"get_X_gen_dominate")][0],generation)    