from .RESULT import RESULT
import numpy as np


class result_metric(RESULT):

    def IPL_hypervolume(self, result, N):
        try:
            N=N+1
        except Exception as e:
            pass
        mtc = self.DATA(result,N,1)
        return mtc.reshape(mtc.shape[0],1)
    

    def IPL_GD(self, result, N):
        try:
            N=N+1
        except Exception as e:
            pass
        mtc = self.DATA(result,N,2)
        return mtc.reshape(mtc.shape[0],1)
    

    def IPL_GDplus(self, result, N):
        try:
            N=N+1
        except Exception as e:
            pass
        mtc = self.DATA(result,N,3)
        return mtc.reshape(mtc.shape[0],1)
    

    def IPL_IGD(self, result, N):
        try:
            N=N+1
        except Exception as e:
            pass
        mtc = self.DATA(result,N,4)
        return mtc.reshape(mtc.shape[0],1)
    

    def IPL_IGDplus(self, result, N):
        try:
            N=N+1
        except Exception as e:
            pass
        mtc = self.DATA(result,N,5)
        return mtc.reshape(mtc.shape[0],1)
    
    
    def IPL_display(self,objectives):
       
        try:
            for idx, i in enumerate(objectives, start = 0):
                if i[0] > 0:
                    print(f'generation {idx}  {i}')
        except Exception as e:
            print(e)