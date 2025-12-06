from .result import result


class result_var(result):
  
    def IPL_variables(self, result, generation):
        return self.DATA([dt.get_X_GEN() 
                          for data in result.get_elements() 
                          for dt in data 
                          if hasattr(dt,"get_X_GEN")][0],generation)
      

       

    