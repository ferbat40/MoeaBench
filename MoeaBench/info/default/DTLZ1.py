class DTLZ1:  
      """
      - array with objectives in generations:

        ● default mode: experiment.benchmark = experiment.benchmarks.DTLZ1():
             
          ○ arguments:     

            ● M = 3: number of problem objectives 
            ● K = 10: 
            ● K = 5: The number represents the size of the vector K related to the decision variables.
            ● P = 100: number of samples to the Pareto optimum.


        ● Notes:
          
          ○ selecting 'DTLZ1' in:
            
            ● experiment.benchmark = experiment.benchmarks.DTLZ1()
              ○ You can access more information about the method.

          ○ for more information:
            
            ● [implementation](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ1/DTLZ1/) detailed implementation information.
            ● ([arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/arguments/)) custom and default settings problem. 
            ● [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/exceptions/) information on possible error types
             
      """

      def __repr__(self):
            return self.__class__.__doc__