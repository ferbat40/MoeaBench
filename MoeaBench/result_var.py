from .result_obj import result_obj

class result_var(result_obj):

      def IPL_variables(self, result, I,  N):
        return self.DATA(result, I,  N, 8)
      

      def IPL_display(self,objectives,I):
        
        try:
            for i in objectives:
                if len(i[1]>0):
                    print(f'\ngeneration {i[0]} for variable {I}\n')
                    for f in i[1]:
                        print(f)
        except Exception as e:
            print(e)


    