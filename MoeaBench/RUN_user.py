from .RUN import RUN


class RUN_user(RUN):

     def MOEA_execute(self,result,problem,name_moea):
          data = result.edit_DATA_conf().get_DATA_MOEA().evaluation()
          result.DATA_store(name_moea,
                            data[3],
                            data[4],
                            data[2],
                            data[0],
                            data[1],
                            problem,
                            [data[4] *gen  for gen in range(0,data[3])])
      
    
         
           

        