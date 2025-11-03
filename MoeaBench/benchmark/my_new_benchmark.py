from .problems import problems


M_register = {}


@staticmethod
def my_new_benchmark():
        try:
            problem = problems(my_new_benchmark.__name__)
            my_benchmark = get_benchmark()
            my_bk = my_benchmark(problem.get_CACHE_USER())
            F =  my_bk.POFsamples()
            my_bk.get_CACHE().DATA_store(my_bk.__class__.__name__,'IN POF',my_bk.get_M(),my_bk.get_N(),my_bk.get_n_ieq_constr(),F,my_bk.get_P(),my_bk.get_K())
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