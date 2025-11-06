from .problems import problems


@staticmethod
def DTLZ1(M = 3, K = 5, P = 700):
        """
        - DTLZ1:
          - sinxtase:
          experiment.problem = moeabench.benchmark.DTLZ1(args) 
          - [DTLZ1](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/) detailed information about the problem
          - ([args](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/#arguments)) custom and default settings problem
          - [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/) information on possible error types
        """
        problem = problems(DTLZ1.__name__)
        bk = problem.get_problem(M, K, P)
        bk.set_BENCH_conf() 
        bk.POFsamples()
        return bk