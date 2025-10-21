from .RESULT import RESULT


class result_obj(RESULT):


    def IPL_objectives(self, result, I,  N, mtc = 7):
        self.allowed_gen(N)
        self.allowed_obj(result, mtc, I)
        self.allowed_gen_max(result, mtc, N)
        return self.DATA(result, I,  N, mtc)
        
    

       