class repository:
        
        def add_MOEA(self,algorithm):
          moea =  algorithm.get_CACHE()
          moea.get_DATA_conf().set_DATA_MOEA(algorithm,algorithm.get_problem()) 
          return (moea,algorithm.__class__,algorithm.__class__.__name__)