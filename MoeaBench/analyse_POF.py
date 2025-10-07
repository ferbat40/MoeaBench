from .analyse import analyse


class analyse_POF(analyse):

        
    @staticmethod
    def IPL_pareto(experiment, objectives):
        print(objectives)
        for b in experiment:
            for i in b[1].get_elements():
                print(i[1].get_M(),"  ",i[0].get_description(),"  ",i[0].get_arr_DATA())
    
