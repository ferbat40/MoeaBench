from .problems import problems



def DTLZ8(M = 3, N = 10, P = 700):
        """
        - benchmark problem:
        Click on the links for more
        ...
                - DTLZ8:
                      - sinxtase:
                      experiment.problem = moeabench.benchmark.DTLZ8(args) 
                      - [general](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ8/) POF sampling, results obtained in tests 
                      with genetic algorithms, references and more... 
                      - [implementation](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ8/DTLZ8/) detailed implementation information
                      - ([arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ8/arguments/)) custom and default settings problem
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ8/exceptions/) information on possible error types
        
        """
        try:
            problem = problems(DTLZ8.__name__)
            bk = problem.get_problem(M , N , P)
            bk.P_validate(P)
            bk.set_BENCH_conf() 
            bk.POFsamples()
            return bk
        except Exception as e:
            print(e)