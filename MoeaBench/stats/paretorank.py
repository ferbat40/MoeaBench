from .allowed_stats import allowed_stats
import plotly.express as px


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
            self.ranking = [i.shape[0] for i in self.experiment.round]
        except Exception as e:
            print(e)
    

    def rank(self):
        return self.ranking
    

    def plot(self):
        fig = px.histogram(
            x = self.ranking,
            title = "histogram of ranks"
        )
        fig.show()
    

def paretorank(experiment):
    pr = paretorank_instance(experiment)
    pr()
    return pr