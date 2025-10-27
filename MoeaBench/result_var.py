from .result_obj_var import result_obj_var


class result_var(result_obj_var):
  
    def allowed_obj(self,result, variable):
        max = [b[1].get_Nvar() for b in result.get_elements()][0]
        if not variable <= max:
            raise TypeError(f"Variable = {variable} not be allowed. It must be between 1 and {max}" )
         

    def IPL_variables(self, result, generation, variable):
        self.allowed_obj(result, variable)
        return self.DATA(result,generation, variable, 1)[0]
      

       

    