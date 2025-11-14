from .problems import problems


@staticmethod
def DPF4(M = 3, K = 5, D = 2, P = 700):
        """
        - benchmark problem:
        Click on the links for more
        ...
                - DPF4:
                      - sinxtase:
                      experiment.problem = moeabench.benchmark.DPF4(args) 
                      - [general](https://moeabench-rgb.github.io/MoeaBench/problems/DPF/DPF4/) POF sampling, results obtained in tests 
                      with genetic algorithms, references and more... 
                      - [implementation](https://moeabench-rgb.github.io/MoeaBench/problems/DPF/DPF4/DPF4/) detailed implementation information
                      - ([arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DPF/arguments/)) custom and default settings problem
                      - [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DPF/exceptions/) information on possible error types
        
        """
        try:
            problem = problems(DPF4.__name__)
            bk = problem.get_problem(M, K, P, D)
            bk.P_validate(P)
            bk.set_BENCH_conf() 
            bk.POFsamples()
            return bk
        except Exception as e:
            print(e)