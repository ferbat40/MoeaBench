from .RESULT import RESULT
import numpy as np


class result_metric(RESULT):

    def IPL_hypervolume(self, result, N, vmtc = 1):
        N = len(result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[vmtc])  if N is None  else N
        self.allowed_gen(result, vmtc, N)
        mtc = self.DATA(result,N,1)
        return mtc.reshape(mtc.shape[0],1)
    

    def IPL_GD(self, result, N, vmtc = 2):
        N = len(result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[vmtc])  if N is None  else N
        self.allowed_gen(result, vmtc, N)
        mtc = self.DATA(result,N,2)
        return mtc.reshape(mtc.shape[0],1)
    

    def IPL_GDplus(self, result, N, vmtc = 3):
        N = len(result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[vmtc])  if N is None  else N
        self.allowed_gen(result, vmtc, N)
        mtc = self.DATA(result,N,3)
        return mtc.reshape(mtc.shape[0],1)
    

    def IPL_IGD(self, result, N, vmtc = 4):
        N = len(result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[vmtc])  if N is None  else N
        self.allowed_gen(result, vmtc, N)
        mtc = self.DATA(result,N,4)
        return mtc.reshape(mtc.shape[0],1)
    

    def IPL_IGDplus(self, result, N, vmtc = 5):
        N = len(result.get_elements()[0][0].get_METRIC_gen().get_arr_Metric_gen()[vmtc])  if N is None  else N
        self.allowed_gen(result, vmtc, N)
        mtc = self.DATA(result,N,5)
        return mtc.reshape(mtc.shape[0],1)
    
    
    def IPL_display(self,objectives):
        for idx, i in enumerate(objectives, start = 0):
            if i[0] > 0:
                print(f'generation {idx}  {i}')
      