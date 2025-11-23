class DTLZ1:  
      """
      - benchmark problem for multi-objective optimization:

      - default mode: experiment.benchmark = experiment.benchmarks.DTLZ1():
             
          ○ arguments (default setting if no arguments are provided):    

            ● M = 3:   number of problem objectives 
            ● K = 5:   number represents the size of the vector K related to the decision variables.
            ● P = 700: number of samples to the Pareto optimum.


      - Notes:
          
          ○ selecting 'DTLZ1' in:
            
            ● experiment.benchmark = experiment.benchmarks.DTLZ1()
              ○ You can access more information about the method.

       - for more information:
            
            ● [general](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ1/) 
              - general information about the problem.

            ● [arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/arguments/) 
              - custom and default settings problem. 
              
            ● [exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/exceptions/) 
              - information on possible error types
             
      """

      def __repr__(self):
            return self.__class__.__doc__