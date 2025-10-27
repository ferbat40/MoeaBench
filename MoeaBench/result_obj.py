from .result_obj_var import result_obj_var


class result_obj(result_obj_var):
      
    def allowed_obj(self,result, objective):
        max = [b[1].get_M() for b in result.get_elements()][0]
        if not objective <= max:
            raise TypeError(f"Objective = {objective} not be allowed. It must be between 1 and {max}" )


    def IPL_objectives(self, result, generation, objective):
        self.allowed_obj(result, objective)
        return self.DATA(result,generation, objective)[0]
        
        
    

