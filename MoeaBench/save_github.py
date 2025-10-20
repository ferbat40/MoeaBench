from github import Github
from .IPL_MoeaBench import IPL_MoeaBench

class save_github(IPL_MoeaBench):

    @staticmethod
    def data(string,exlude):
        string_class = string.splitlines() 
        string_class_full=[]
        for row in string_class:
            if exlude in row:
                continue
            string_class_full.append(row)
        string_class_full = "\n".join(string_class_full)
        print(string_class_full)
        return string_class_full
    

    @staticmethod
    def save_moea(obj):
        moea = obj.Moea.get_moea()
        instance_moea=None
        try:
            instance_moea = moea(obj.pof)
        except Exception as e:
            print(e)
        file_moea = f'{instance_moea.__class__.__name__}.py'
        with open(file_moea,'r') as f:
            code_moea = f.read()
        path_repository_moea =  f'MoeaBench/user_moea/{file_moea}'  
        return  code_moea,path_repository_moea
    

    @staticmethod
    def save_benchmark(my_bk):
        file_benchmark = f'{my_bk.pof.__class__.__name__}.py'
        with open(file_benchmark ,'r') as f:
            code_benchmark  = f.read()
        path_repository_benchmark =  f'MoeaBench/user_benchmark/{file_benchmark}'   
        return code_benchmark,path_repository_benchmark
    

    @staticmethod
    def IPL_save_github(obj):
       
        token = Github("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")
        repository = token.get_user().get_repo('MoeaBench')

           
        code_moea,path_repository_moea = save_github.save_moea(obj)
        repository.create_file(path_repository_moea,'add file',save_github.data(code_moea,"Moea.register_moea()"))


        code_benchmark,path_repository_benchmark = save_github.save_benchmark(obj)  
        repository.create_file(path_repository_benchmark ,'add file',save_github.data(code_benchmark,"benchmark.register_benchmark()" ))