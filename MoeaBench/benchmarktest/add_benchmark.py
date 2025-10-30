from MoeaBench.CACHE_bk_user import CACHE_bk_user


def add_benchmark(name, m = 3 ,p = 600 ,k = 5):
        my_benchmark = name(CACHE_bk_user(), m, p, k)
        F = my_benchmark.POFsamples()
        my_benchmark.get_CACHE().DATA_store(my_benchmark.__class__.__name__,'IN POF',my_benchmark.M,my_benchmark.N,my_benchmark.n_ieq_constr,F,my_benchmark.P,my_benchmark.K)
        return my_benchmark