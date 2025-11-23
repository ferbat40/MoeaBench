class DTLZ7:  
      """
      - benchmark problem for multi-objective optimization:

        ● default mode: experiment.benchmark = experiment.benchmarks.DTLZ7():
             
          ○ arguments:     
                  
            ● M = 3:   number of problem objectives 
            ● K = 5:   number represents the size of the vector K related to the decision variables.
            ● P = 700: number of samples to the Pareto optimum.


        ● Notes:
          
          ○ selecting 'DTLZ7' in:
            
            ● experiment.benchmark = experiment.benchmarks.DTLZ7()
              ○ You can access more information about the method.

          ○ for more information:
            
            ● [general](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ7/) general information about the problem.
            ● [arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/arguments/) custom and default settings problem. 
            ● [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/exceptions/) information on possible error types
            
      """

      def __repr__(self):
            return self.__class__.__doc__