from .file import file
from .save_github import save_github
import inspect


class save_class(file):

    @staticmethod
    def save_benchmark(my_bk):
        string_class = inspect.getsource(my_bk.__class__)
        string_class_temp = 'from MoeaBench.base_benchmark import BaseBenchmark\n\n\n\n'+string_class
        string_class_temp = string_class_temp.splitlines() 
        string_class_full=[]
        for row in string_class_temp:
            if 'benchmark.register_benchmark()' in row:
                continue
            string_class_full.append(row)
        string_class_full = "\n".join(string_class_full)
        file_name = f'{my_bk.__class__.__name__}'
        file_name = file.DATA(file_name,'MoeaBench/user_benchmark','py')
        with open(file_name, 'w') as f:
            f.write(string_class_full)


    @staticmethod
    def save_moea(my_moea):
        string_class = inspect.getsource(my_moea.__class__)
        string_class_temp = 'from MoeaBench.base_moea import BaseMoea\n\n\n\n'+string_class
        string_class_temp = string_class_temp.splitlines() 
        string_class_full=[]
        for row in string_class_temp:
            if 'Moea.register_moea()' in row:
                continue
            string_class_full.append(row)
        string_class_full = "\n".join(string_class_full)
        file_name = f'{my_moea.__class__.__name__}'
        file_name = file.DATA(file_name,'MoeaBench/user_moea','py')
        with open(file_name, 'w') as f:
            f.write(string_class_full)


    @staticmethod
    def IPL_save_class(obj):
        save_github.save(obj)
        #moea = obj.Moea.get_moea()
        #moeabench_benchmark = save_class.DATA(f'{obj.pof.__class__.__name__}','MoeaBench/','py') 
        #user_benchmark = save_class.DATA(f'{obj.pof.__class__.__name__}','MoeaBench/user_benchmark','py')    
    
        #instance_moea=None
        #try:
            #instance_moea = moea(obj.pof)
        #except Exception as e:
            #pass
            
       # moeabench_user = save_class.DATA(instance_moea.__class__.__name__,'MoeaBench/user_moea','py') if instance_moea is not None else None
        
        #if (moeabench_benchmark.exists() or user_benchmark.exists()) and (moeabench_user is not None and moeabench_user.exists()):
           # raise MemoryError("classes already exists")
        
        #if not moeabench_benchmark.exists() and not user_benchmark.exists():
            #save_class.save_benchmark(obj.pof)

       # if moeabench_user is not None and not moeabench_user.exists():
           # save_class.save_moea(instance_moea)
                