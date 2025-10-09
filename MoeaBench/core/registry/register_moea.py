

M_register = {}

def register_moea(name):
    def decorator(cls):
        M_register[name] = cls

        return cls
    return decorator


def get_moea(name):
    return M_register.get(name)