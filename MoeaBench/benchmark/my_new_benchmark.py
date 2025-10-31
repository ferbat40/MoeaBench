from MoeaBench.CACHE_bk_user import CACHE_bk_user

M_register = {}


@staticmethod
def my_new_benchmark():
        try:
            my_benchmark = get_benchmark()
            my_bk = my_benchmark(CACHE_bk_user())
            F =  my_bk.POFsamples()
            my_bk.get_CACHE().DATA_store(my_bk.__class__.__name__,'IN POF',my_bk.M,my_bk.N,my_bk.n_ieq_constr,F,my_bk.P,my_bk.K)
            return my_bk
        except Exception as e:
            print(e)
        

@staticmethod   
def register_benchmark():
        def decorator(cls):
            try:
                name = cls.__name__
                if len(M_register) > 0:
                     raise MemoryError("There is already an implementation of the user's Benchmark registered")
                M_register[name] = cls
            except Exception as e:
                 print(e)
            return cls
        return decorator


@staticmethod
def get_benchmark():
        return next(iter(M_register.values())) if len(M_register.values()) > 0 else None