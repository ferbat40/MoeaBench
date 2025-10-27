from .RESULT import RESULT

class result_var(RESULT):
      

    

      def IPL_variables(self, result, I,  N, mtc = 8):
        self.allowed_gen(N)
        self.allowed_obj(result, mtc, I)
        self.allowed_gen_max(result, mtc, N)
        return self.DATA(result, I,  N, mtc)
      

       

    