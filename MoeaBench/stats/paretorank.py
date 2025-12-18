class paretorank:

    def __init__(self, experiment):
        for i in experiment.round:
            print(i.shape)


def mwtest(experiment):
    pr = paretorank(experiment)
    pr()
    return pr