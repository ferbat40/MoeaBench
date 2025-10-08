from .IPL_MoeaBench import IPL_MoeaBench
from pathlib import Path

class file(IPL_MoeaBench):

    @staticmethod
    def DATA(folder):
        base = Path.cwd()
        dir_z = base  / 'analysis'
        dir_z.mkdir(parents=True, exist_ok = True)
        return dir_z / f'{folder}.zip'
   



