class dominated:

    def __init__(self, benchmark):
        self.benchmark = benchmark


    def objectives(self):
        return [pof.get_arr_DATA() for pof_benchmark in self.benchmark.pof.get_CACHE().get_elements() for pof in pof_benchmark if hasattr(pof,'get_arr_DATA')][0]
    

    def variables(self):
        return [pof.get_arr_DATA() for pof_benchmark in self.benchmark.pof.get_CACHE().get_elements() for pof in pof_benchmark if hasattr(pof,'get_arr_DATA')][0]
    