
import os
from MoeaBench import moeabench
from MoeaBench.base_moea import BaseMoea
import sys
from  MoeaBench.CACHE_bk_user import CACHE_bk_user
#sys.modules['__main__'].my_dtlz7 = my_dtlz7




import numpy as np
import inspect

os.system("cls")  

def std(var1,var2,var3):
    return float(np.nanstd([var1,var2,var3])),'std'


def mean(var1,var2,var3):
    return float(np.nanmean([var1,var2,var3])),'mean'


def minv(var1,var2,var3):
    return float(np.min([var1,var2,var3])),'min'


def maxv(var1,var2,var3):
    return float(np.max([var1,var2,var3])),'max'



def dict_metric():
    return  {

        0: std,
        1: mean,
        2: minv,
        3: maxv
    }

std_ = True
mean_ = False
min = False
max = True
val_metric = [idx for idx, i in enumerate([std_,mean_,min,max], start = 0) if i is True]
print(val_metric)
metc = list(map(lambda key: dict_metric()[key](1,2,3),val_metric   ))
print(metc)











































































