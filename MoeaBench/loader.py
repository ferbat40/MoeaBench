from .file import file
from joblib import load
import zipfile
from io import BytesIO

class loader(file):
     
    def IPL_loader(self, folder):
        path_z = loader.DATA(folder)
        if not path_z.exists():
            raise FileExistsError("folder not found")
        obj = None
        with zipfile.ZipFile(path_z, 'r') as zf:
            bytes = zf.read('Moeabench.joblib')
            obj = load(  BytesIO(bytes))

        self.__dict__.update(obj.__dict__)
 

        