from .problems import problems


@staticmethod
def DTLZ1(M = 3, K = 5, P = 700):
        """
        - benchmark problem:
        Click on the links for more
        ...
                - DTLZ1:
                      - sinxtase:
                      experiment.problem = moeabench.benchmark.DTLZ1(args) 
                      - [DTLZ1](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/) detailed information about the problem
                      - ([args](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/#arguments)) custom and default settings problem
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/) information on possible error types
        
        """
        try:
            problem = problems(DTLZ1.__name__)
            bk = problem.get_problem(M, K, P)
            bk.P_validate(P)
            bk.set_BENCH_conf() 
            bk.POFsamples()
            return bk
        except Exception as e:
            print(e)