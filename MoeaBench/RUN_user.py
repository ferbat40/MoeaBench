from .runner import runner



class RUN_user(runner):

     def MOEA_execute(self,result,problem,name_moea,name_benchmark):
          data = result.edit_DATA_conf().get_DATA_MOEA().evaluation()
          result.DATA_store(name_moea,
                            result.edit_DATA_conf().get_DATA_MOEA().generations,
                            result.edit_DATA_conf().get_DATA_MOEA().population,
                            data[2],
                            data[0],
                            data[1],
                            problem,
                            name_benchmark,
                            data[3])
      
    
         
           

        