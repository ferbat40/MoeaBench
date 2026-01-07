class objectives:

    def __init__(self, cls_result_dominated):
        self.result_dominated = cls_result_dominated()


    def __call__(self, result, generation):
       self.result_dominated.IPL_dominated_objectives(result, generation)