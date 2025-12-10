from .plot_3D import plot_3D
import numpy as np


class analyse_obj(plot_3D):
        
        
    def allowed_DATA(i):
        if hasattr(i,'result') and hasattr(i.result,'get_elements'):
            return True
        elif isinstance(i,np.ndarray) and i.ndim == 2:
            return True
        else:
            return False
    

    @staticmethod
    def DATA(i):
        return [z.get_F_GEN()[-1] for b in i.result.get_elements() for z in b if hasattr(z,'get_F_GEN')][0]  if hasattr(i,'result') and hasattr(i.result,'get_elements') else None
   

    @staticmethod
    def extract_pareto_result(args):
        idx = [i for i in range(1,len(args)+1)]
        val = np.array(list(map(lambda key: analyse_obj.allowed_DATA(key),[i for i in args])))
        data = []
        benk = []
       
        if len(np.where(val == False)[0]) >= 0:
            raise TypeError(f'incorrect data format: {[args[i] for i in range(0,len(val)) if val[i] == False] [0]  }')
        
        it_exp = iter(idx)
        it_arr = iter(idx)
        for i in args:
            arr = analyse_obj.DATA(i)
            name =  f'{i.__class__.__name__}{next(it_exp)}' if arr is not None else f'{i.__class__.__name__}{next(it_arr)}'
            arr =  arr if arr is not None else i
            data.append(arr)
            benk.append(name)
        return benk, data

      
    @staticmethod
    def IPL_plot_3D(args, objectives, generations = []):
        benk, data = analyse_obj.extract_pareto_result(args)
        #print(data, "    ",benk)
      
        
            
    
            #analyse_obj.allowed_obj(bench,bench[0],experiments,objectives)
            #axis =  [i for i in range(0,3)]    if len(objectives) == 0 else [i-1 if i > 0 else 0 for i in objectives] 
            
            #if not len([i for i in arra_gen if len(i) == 0]) == 0:   
                #raise ValueError (f'No results found for plot')
            #plot_3D_obj =  analyse_obj(bench,arra_gen,experiments,axis, generations)
            #$plot_3D_obj.configure()
      
    
