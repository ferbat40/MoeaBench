from .allowed_stats import allowed_stats
import plotly.express as px
from ..moea_round import moea_round


class paretorank_instance(allowed_stats):

    def __init__(self, experiment):
        self.experiment = experiment
        self.ranking = []


    def allowed(self, exp):
        if not hasattr(exp,'result'):
            raise ValueError("only experiment data types are allowed.")    


    def __call__(self):
        try:
            self.allowed(self.experiment)
            rank = [i for i in self.experiment.round]
            self.ranking = sorted(rank, key = lambda pop: pop.front.shape[0], reverse = True)
        except Exception as e:
            print(e)
    

    def rank(self):
        return [round.name for round in self.ranking]
    


    def plot(self):
        fig = px.bar(
            x = [nd.front.shape[0] for nd in self.ranking],
            y = [round.name for round in self.ranking],
            labels = {'x' : "nom dominated", 'y' : 'ranking'},
            title = "histogram of ranks"
        )
        fig.show()
    

    #def plot(self):
        #fig = px.histogram(
           # x = [i.front.shape[0] for i in self.ranking],
            #title = "histogram of ranks"
       # )
       # fig.show()
    

def paretorank(experiment):
    pr = paretorank_instance(experiment)
    pr()
    return pr