from .MoeaBench import MoeaBench

class _MoeaBenchWrapper:
    
    def __init__(self):
        self.__doc__ =   """
        - Description:   
            MoeaBench is a framework for experimentation, analysis, and 
            development of benchmark problems for validating the performance     
            of genetic algorithms.
             
        - Example :
            experiment = moeabench()
           
        - NOTES:
            - For more information about the framework, please visit the link:
              https://moeabench-rgb.github.io/MoeaBench/
    """
    

    def __getattr__(self, name):
        inst = MoeaBench()
        return getattr(inst, name)


    def __call__(self, *args, **kwargs):
        obj = MoeaBench(*args,  **kwargs)
        obj.__doc__ = self.__doc__
        return obj

moeabench = _MoeaBenchWrapper()
