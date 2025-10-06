from .RESULT import RESULT


class result_obj(RESULT):
    

    def DATA(self,result, I,  N):
        return [[idx,obj[:,I-1:I]] for idx, obj in enumerate(result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[7][0:N])]
     

    def IPL_objectives(self, result, I,  N):
        return self.DATA(result, I,  N)
        
    
    def IPL_display(self,objectives,I):
        
        try:
            for i in objectives:
                if len(i[1]>0):
                    print(f'\ngeneration {i[0]} for objective {I}\n')
                    for f in i[1]:
                        print(f)
        except Exception as e:
            print(e)
       
      