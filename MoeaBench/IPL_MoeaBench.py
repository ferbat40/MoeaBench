from .I_MoeaBench import I_MoeaBench
import inspect

class IPL_MoeaBench(I_MoeaBench):

    def IPL_variables(self):
        raise NotImplementedError("Not implemented")
    

    def normalize_gen(self):
        raise NotImplementedError("Not implemented")


    def DATA(self):
        raise NotImplementedError("Not implemented")


    def change_axis(self):
        raise NotImplementedError("Not implemented")

   
    def IPL_objectives(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_plot_3D(self):
        raise NotImplementedError("Not implemented")
    
    
    def PLT(self):
        raise NotImplementedError("Not implemented")  
    
    
    def allowed_obj(self):
        raise NotImplementedError("Not implemented")
    
    
    def configure(self):
        raise NotImplementedError("Not implemented")
    

    def  IPL_GD(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_GDplus(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_IGD(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_IGDplus(self):
        raise NotImplementedError("Not implemented")
      
    
    def IPL_hypervolume(self):
        raise NotImplementedError("Not implemented")
    

    def IPL_display(self):
        raise NotImplementedError("Not implemented")
    

    def allowed_gen(self):
        raise NotImplementedError("Not implemented")
    

    def IPL_plot_GD(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_plot_GDplus(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_plot_IGD(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_plot_IGDplus(self):
        raise NotImplementedError("Not implemented")
    
    
    def IPL_plot_hypervolume(self):
        raise NotImplementedError("Not implemented")
    
    
    @staticmethod
    def extract_pareto_result(args,caller):
        experiment = [] 
        data = []
        benk = []
        arr = []
        for i in args:
            for key, val in caller:
                try:
                    if i == val.result:
                        experiment.append(f'{key}.result')
                        arr.append(i.get_elements()[0][0].get_arr_DATA())
                        data.append(i.get_elements()[0][0])
                        benk.append(i.get_elements()[0][1])
                    elif i == val.pof:
                        experiment.append(f'{key}.pof')
                        arr.append(i.get_CACHE().get_elements()[0][0].get_arr_DATA())
                        data.append(i.get_CACHE().get_elements()[0][0])
                        benk.append(i.get_CACHE().get_elements()[0][1])
                except Exception as e:
                    pass
        return experiment, data, benk, arr





