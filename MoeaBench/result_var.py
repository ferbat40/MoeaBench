from .RESULT import RESULT

class result_var(RESULT):
      
      def allowed_obj(self,result, mtc, I):
        max = result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[mtc][0].shape[1]
        if not I <= max:
            raise TypeError(f"variables = {I} not be allowed. It must be between 0 and {max}" )
    

      def IPL_variables(self, result, I,  N, mtc = 8):
        self.allowed_gen(N)
        self.allowed_obj(result, mtc, I)
        self.allowed_gen_max(result, mtc, N)
        return self.DATA(result, I,  N, mtc)
      

       

    