from .RESULT import RESULT


class result_obj(RESULT):


    def DATA(self,result, I,  N, mtc):
        return [[idx,obj[:,I-1:I]] for idx, obj in enumerate(result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[mtc][N[0]:N[1]])]
     

    def IPL_objectives(self, result, I,  N, mtc = 7):
        self.allowed_gen(N)
        self.allowed_obj(result, mtc, I)
        self.allowed_gen_max(result, mtc, N)
        return self.DATA(result, I,  N, mtc)
        
    

       