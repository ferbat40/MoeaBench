class DTLZ3:  
      """
      - array with objectives in generations:

        ● default mode: experiment.benchmark = experiment.benchmarks.DTLZ3():
             
          ○ arguments:     
                  
            ● M = 3:   number of problem objectives 
            ● K = 10:  number represents the size of the vector K related to the decision variables.
            ● K = 5:   number represents the size of the vector K related to the decision variables.
            ● P = 700: number of samples to the Pareto optimum.


        ● Notes:
          
          ○ selecting 'DTLZ3' in:
            
            ● experiment.benchmark = experiment.benchmarks.DTLZ3()
              ○ You can access more information about the method.

          ○ for more information:
            
            ● [implementation](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ3/DTLZ3/) detailed implementation information.
            ● [arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/arguments/) custom and default settings problem. 
            ● [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/exceptions/) information on possible error types
            
      """

      def __repr__(self):
            return self.__class__.__doc__