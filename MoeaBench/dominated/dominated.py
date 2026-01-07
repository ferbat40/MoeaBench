from MoeaBench import dominated

class front:

    def __init__(self, cls_result_dominated, result, rounds):
        self.cls_result_dominated = cls_result_dominated()
        self.result = result
        self.rounds = rounds


    def objectives(self, generation = None):
        try:
            dm = dominated.objectives(self.cls_result_dominated, self.result, generation)
            dm(self.result, generation)
            return dm
        except Exception as e:
            print(e)
    

    def round(self, index):
        return self.rounds[index].front 