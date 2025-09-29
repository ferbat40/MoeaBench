from .I_METRIC_gen import I_METRIC_gen


class METRIC_gen(I_METRIC_gen):

    def __init__(self,arr_Metric_gen,**kwargs):
        self.arr_Metric_gen=arr_Metric_gen
        super().__init__(**kwargs)


    def get_arr_Metric_gen(self):
        return self.arr_Metric_gen
    

    

    