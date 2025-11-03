from .MoeaBench import MoeaBench

class _MoeaBenchWrapper:
    """
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
        return MoeaBench(*args,  **kwargs)

moeabench = _MoeaBenchWrapper()