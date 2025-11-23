class DTLZ8:  
      """
      - benchmark problem for multi-objective optimization:

      - default mode: experiment.benchmark = experiment.benchmarks.DTLZ8():
             
          ○ arguments (default setting if no arguments are provided):     
                  
            ● M = 3:   number of problem objectives 
            ● N = 10:  number of decision variables.
            ● P = 700: number of samples to the Pareto optimum.


      - Notes:
          
          ○ selecting 'DTLZ8' in:
            
            ● experiment.benchmark = experiment.benchmarks.DTLZ8()
              ○ You can access more information about the method.

      - for more information:
            
            ● [general](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ8/) 
              - general information about the problem.

            ● [arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ8/arguments/) 
              - custom and default settings problem. 

            ● [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ8/exceptions/) 
              - information on possible error types
            
      """

      def __repr__(self):
            return self.__class__.__doc__