import MoeaBench as statics

class stats:

    def __init__(self, result_population, fff):
        self.result_population = result_population


    def indice(self, experiment = None, generation = None):
        ind  = statics.stats.indice_instance(self.result_population, experiment, generation)
        return ind()