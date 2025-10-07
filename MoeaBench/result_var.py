from .result_obj import result_obj

class result_var(result_obj):
      
      def allowed_obj(self,result, mtc, I):
        max = result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[mtc][0].shape[1]
        if not I <= max:
            raise TypeError(f"variables = {I} not be allowed. It must be between 0 and {max}" )
    

      def IPL_variables(self, result, I,  N, mtc = 8):
        N = len(result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[mtc])  if N is None  else N
        self.allowed_obj(result, mtc, I)
        self.allowed_gen(result, mtc, N)
        return self.DATA(result, I,  N, mtc)
      

      def IPL_display(self,objectives,I):
          for i in objectives:
              if len(i[1]>0):
                print(f'\ngeneration {i[0]} for variable {I}\n')
                for f in i[1]:
                   print(f)
       

    