from .runner import runner


class RUN_user(runner):

     def MOEA_execute(self,result,problem,name_moea,name_benchmark):
          data = result.edit_DATA_conf().get_DATA_MOEA().evaluation()
          result.DATA_store(name_moea,
                            data[3],
                            data[4],
                            data[2],
                            data[0],
                            data[1],
                            problem,
                            name_benchmark)
      
    
         
           

        