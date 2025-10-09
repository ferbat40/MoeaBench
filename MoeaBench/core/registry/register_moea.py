
from MoeaBench.core.utils.save_moea import save_moea

M_register = {}

def register_moea(name):
    def decorator(cls):
        M_register[name] = cls
        save_moea(cls)
        return cls
    return decorator