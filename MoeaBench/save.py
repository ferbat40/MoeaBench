from .file import file
from joblib import dump
import numpy as np
import zipfile
from io import BytesIO, StringIO


class save(file):   
    
    @staticmethod
    def IPL_save(obj, folder):
        NonDominate = obj.result.get_elements()[0][0].get_arr_DATA()
        Dominate = obj.result.get_elements()[0][0].get_F_GEN()[-1]
      
        result =  NonDominate if NonDominate.shape[0] > 1 else Dominate
        bench = obj.result.get_elements()[0][1]
        data = obj.result.get_elements()[0][0]
        pof =  obj.pof.get_CACHE().get_elements()[0][0].get_arr_DATA()     
        path_z = save.DATA(folder)
        if path_z.exists():
            raise FileExistsError("file already exists")
        dt_MoeaBench = []
        dt_MoeaBench.append(f'{data.get_description()} Evolucionary algorithm data:\n')
        dt_MoeaBench.append(f'generations: {data.get_generations()}')
        dt_MoeaBench.append(f'population: {data.get_population()}')
        solutions =  f'non-dominated solutions of the Pareto front' if NonDominate.shape[0] > 1 else f'Only Pareto-dominated solutions were found.'   
        dt_MoeaBench.append(f'{solutions}: {result.shape[0]}')
        dt_MoeaBench.append(f'\n{bench.get_BENCH()} problem test benchmark data:\n')
        dt_MoeaBench.append(f'objectives: {bench.get_M()}')
        dt_MoeaBench.append(f'decision variabels: {bench.get_Nvar()}')
        dt_MoeaBench.append(f'size vector K: {bench.get_K()}')
        if bench.get_D() > 0:
            dt_MoeaBench.append(f'essencial objectves D: {bench.get_D()}')
        dt_MoeaBench.append(f'simulated POF solutions: {pof.shape[0]}')
        dt_MoeaBench.append(f'\nThe zip file contains the following:\n')
        dt_MoeaBench.append(f'pof.csv file contains sample simulations of Pareto-optimal front solutions')
        dt_MoeaBench.append(f'result.csv file contains results of solutions of the evolucionary algorithm related to a problem')
        dt_MoeaBench.append(f'Movebench.joblib contains the experiment object, which provides all the analysis tools, and for the other data generated as:')
        dt_MoeaBench.append(f'hypervolume data')
        dt_MoeaBench.append(f'GD data')
        dt_MoeaBench.append(f'IGD data')
        dt_MoeaBench.append(f'GD plus data')
        dt_MoeaBench.append(f'IGD plus data')
        dt_MoeaBench.append(f'the objectives during the generations')
        dt_MoeaBench.append(f'decision variables during the generations')
       
        
        with zipfile.ZipFile(path_z, 'w') as zf:
            header_result = ",".join([f'objective {i}' for i in range(1, bench.get_M()+1)])
            zf.writestr('problem.txt',"\n".join(dt_MoeaBench))
            mem_csv_pof =  StringIO()
            np.savetxt(mem_csv_pof,pof, delimiter=",", fmt="%.16f", header=header_result, comments='')
            zf.writestr('pof.csv',mem_csv_pof.getvalue())

            mem_csv_result =  StringIO()
            

            np.savetxt(mem_csv_result,result, delimiter=",", fmt="%.16f", header=header_result, comments='')
            zf.writestr('result.csv',mem_csv_result.getvalue())

            mem_obj =  BytesIO()
            dump(obj,mem_obj )
            mem_obj.seek(0)
            zf.writestr('Moeabench.joblib',mem_obj.read())
        



   

        
 
