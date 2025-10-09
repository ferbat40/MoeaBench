
M_register = {}

def register_moea(name):
    def decorator(cls):
        M_register[name]
        return cls
    return decorator