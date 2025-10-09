import inspect

def save_moea(moea_class):
    isp = inspect.getsource(moea_class)
    with open (f'{moea_class.__name__}.py','w') as f:
        f.write(isp)