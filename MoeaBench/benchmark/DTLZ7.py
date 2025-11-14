from .problems import problems


def DTLZ7(M = 3, K = 5, P = 700):
        """
        - benchmark problem:
        Click on the links for more
        ...
                - DTLZ7:
                      - sinxtase:
                      experiment.problem = moeabench.benchmark.DTLZ7(args) 
                      - [general](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ7/) POF sampling, results obtained in tests 
                      with genetic algorithms, references and more... 
                      - [implementation](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ7/DTLZ7/) detailed implementation information
                      - ([arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/arguments/)) custom and default settings problem
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/exceptions/) information on possible error types
        
        """
        try:
            problem = problems(DTLZ7.__name__)
            bk = problem.get_problem(M, K, P)
            bk.P_validate(P)
            bk.set_BENCH_conf() 
            bk.POFsamples()
            return bk
        except Exception as e:
            print(e)