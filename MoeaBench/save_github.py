from github import Github

class save_github:
    
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
        file = f'{instance_moea.__class__.__name__}.py'
        with open(file,'r') as f:
            code = f.read()
        repository.create_file(file,'add file',code)