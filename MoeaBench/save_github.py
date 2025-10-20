from github import Github

class save_github:

    @staticmethod
    def data(string,exlude):
        string_class = string.splitlines() 
        string_class_full=[]
        for row in string_class:
            if exlude in row:
                continue
            string_class_full.append(row)
        print(string_class_full)
        return string_class_full
    

    @staticmethod
    def save(obj):
        moea = obj.Moea.get_moea()
        instance_moea=None
        try:
            instance_moea = moea(obj.pof)
        except Exception as e:
            pass
        token = Github("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")
        repository = token.get_user().get_repo('MoeaBench')

        
        
        file_moea = f'{instance_moea.__class__.__name__}.py'
        with open(file_moea,'r') as f:
            code_moea = f.read()
        path_repository_moea =  f'user_moea/{file_moea}'        
        repository.create_file(path_repository_moea,'add file',save_github(code_moea,"Moea.register_moea()"))


        file_benchmark = f'{obj.pof.__class__.__name__}.py'
        with open(file_benchmark ,'r') as f:
            code_benchmark  = f.read()
        path_repository_benchmark =  f'user_benchmark/{file_benchmark}'        
        repository.create_file(path_repository_benchmark ,'add file',save_github(code_benchmark,"benchmark.register_benchmark()" ))