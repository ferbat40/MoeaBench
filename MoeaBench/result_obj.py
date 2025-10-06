from .RESULT import RESULT


class result_obj(RESULT):

    def allowed_gen(result,N,mtc):
        print(len(result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[mtc]))
        if not max == N:
            raise TypeError(f"generations = {N} not be allowed. It must be between 0 and {max}" )


    def DATA(self,result, I,  N, mtc):
        return [[idx,obj[:,I-1:I]] for idx, obj in enumerate(result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[mtc][0:N])]
     

    def IPL_objectives(self, result, I,  N):
        return self.DATA(result, I,  N, 7)
        
    
    def IPL_display(self,objectives,I):
        
        try:
            for i in objectives:
                if len(i[1]>0):
                    print(f'\ngeneration {i[0]} for objective {I}\n')
                    for f in i[1]:
                        print(f)
        except Exception as e:
            print(e)
       
      