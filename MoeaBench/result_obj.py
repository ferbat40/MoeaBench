from .result import result


class result_obj(result):
      
    def IPL_objectives(self, result, generation):
        return self.DATA([dt.get_F_GEN() 
                          for data in result.get_elements() 
                          for dt in data 
                          if hasattr(dt,"get_F_GEN")][0],generation)
        
    

