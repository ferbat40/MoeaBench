from .RUN import RUN

class RUN_user(RUN):


     def MOEA_execute(self,result):
          data = result.edit_DATA_conf().get_DATA_MOEA().evaluation()
          print(data[2].shape)
          #for idx, i in enumerate(data[1], start = 0):
               
               #print(i.shape," gen ",idx)
               #for b in i:
                    #print(b,"  gen ",idx)
          
          #nome,
          #GEN,
          # POP,
          # F,
          # X,
          # history,
          # problem