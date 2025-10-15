from .file import file
from joblib import load
import zipfile
from io import BytesIO
import importlib
import os
import sys


class loader(file):
     
    def IPL_loader(self, folder):
        

        dir = os.path.dirname(__file__)
        if dir not in sys.path:
            sys.path.append(dir)
 
        
        #module_name = f"user_benchmark.{'my_dtlz5'}"
        #importlib.import_module(module_name)





        path_z = loader.DATA(folder)
        if not path_z.exists():
            raise FileExistsError("folder not found")
        obj = None
        with zipfile.ZipFile(path_z, 'r') as zf:
            bytes = zf.read('Moeabench.joblib')
            obj = load(  BytesIO(bytes))

        self.__dict__.update(obj.__dict__)
 

        