import numpy as np
import inspect


class ALLOWED:    
        
    def allowed_call(self,classes):
         call=inspect.stack()
         clr = call[2]
         if clr.function == '<module>' or clr.function == '<cell line: 0>':
             raise RuntimeError (f"Invalid call to class {classes} through {clr.filename}, line {clr.lineno}")


    def allowed_bench(self,BENCH,D,K,N):

        if not isinstance(BENCH,str):
            raise ValueError('The Name of the Benchmark must be a string')#
 
        if not self.allowed_str(BENCH):
            raise ValueError('Is not allowed special characters for name of the Benchmark or strings less than 3')#
        
        #if not self.allowed_int(M):
           # raise ValueError('Only integer types for M are allowed')#
        
        #if not self.allowed_int(D):
            #raise ValueError('Only integer types for D are allowed')#
        
       # if not self.allowed_int(K):
            #raise ValueError('Only integer types for K are allowed')#
        
        #if not self.allowed_int(N):
           # raise ValueError('Only integer types for N are allowed')#   

        #M = int(M)
        N = int(N)

        #if not M>0:
           # raise ValueError('The value of M must be greather than 0')#

        
        if not N>0:
            raise ValueError('The value of N must be greather than 0')#
       

    def allowed_result(self,description,arr_DATA,generations,population):

        if not isinstance(description,str):
            raise TypeError("'The Name of the MOEA must be a string'")#

        if not self.allowed_str(description):
            raise ValueError('Is not allowed special characters for name of the MOEA or strings less than 3')#
        
        #if not self.allowed_int(generations):
            #raise ValueError('Only integer types for generations are allowed')#
        
        #if not self.allowed_int(population):
           # raise ValueError('Only integer types for population are allowed')#
        
        generations=int(generations)
        population=int(population)
        
        if not generations > 0:
            raise ValueError('The value of generations must be greather than 0')#
        
        if not population > 0:
            raise ValueError('The value of population must be greather than 0')#
            
        if not isinstance(arr_DATA, (list, np.ndarray, tuple)):
            raise TypeError('Only arrays, lists or tuples are allowed for arrays' )#

        if not len(arr_DATA) > 0:
            raise ValueError('Is not allowed empty arrays')#

        if not np.array(arr_DATA).ndim == 2:
            raise ValueError('Only arrays with two dimension is allowed')#
        return np.array(arr_DATA)
    
    
    def allowed_int(self,STR):
         if STR.strip() == "":
             return False
         for DG in STR.strip():
             if not DG.isdigit():
                 return False
         return True


    def allowed_str(self,STR):
        if len(STR.strip()) < 3:
            return False
        for DG in STR:
            if  not DG.isalpha() and not DG.isdigit():
                return False
        return True
    

    def K_validate(self,K_N):
        if not K_N > 0:
            raise ValueError("this value of 'k' is not valid, it must be greater than 0")#
        return True
    

    def M_validate(self,M):
        if not  M > 2:
            raise ValueError("this value of 'M' is not valid, it must be greater or equal than 2" )#
        return True
    

    def N_validate(self,N):
        if not N >= 5:
            raise ValueError("this value of 'N' is not valid, it must be greater or equal than 5" )#
        return True
    
    
    def MN_validate(self,K_N,M,D):
        if not M <= D+K_N-1:
            raise ValueError("this value of 'M' is not valid, it must be lass or equal than N")#
        return True
    
    
    def MN1_validate(self,M,D):
        if not M > D > 1:
            raise ValueError("The value of 'D' must be greater than 1 and less than 'M'")#
        return True
    

    

    
    

    
    
    
    


       


   
    

