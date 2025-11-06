from .problems import problems


@staticmethod
def DTLZ1(M = 3, K = 5, P = 700):
        """
        - Example:
          - The benchmark problem should be used with an experiment, with the following syntax.
          experiment.problem = moeabench.benchmark.[DTLZ1](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/)(ARGS)
        
        - Notes:
          - [DTLZ1](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/) for detailed information about the problem
          - ( [ARGS](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/#arguments) ) for detailed information on the parameters that can be passed for custom 
          - configuration of the benchmark problem, see the parameters that can be passed. 
          [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ1/DTLZ1/) for information on possible error types
    
        """
        problem = problems(DTLZ1.__name__)
        bk = problem.get_problem(M, K, P)
        bk.set_BENCH_conf() 
        bk.POFsamples()
        return bk