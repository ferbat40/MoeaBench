
M_register = {}

def register_moea(name):
    def decorator(cls):
        M_register[name] = cls
        return cls
    return decorator