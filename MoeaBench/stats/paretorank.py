class paretorank_instance:

    def __init__(self, experiment):
        self.experiment = experiment
        self.ranking = []


    def __call__(self):
        self.ranking = [i.shape[0] for i in self.experiment.round]
    

    def rank(self):
        return self.ranking
    

def paretorank(experiment):
    pr = paretorank_instance(experiment)
    pr()
    return pr