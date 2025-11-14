from .problems import problems


@staticmethod
def DTLZ1(M = 3, K = 5, P = 700):

        try:
            problem = problems(DTLZ1.__name__)
            bk = problem.get_problem(M, K, P)
            bk.P_validate(P)
            bk.set_BENCH_conf() 
            bk.POFsamples()
            return bk
        except Exception as e:
            print(e)