class DPF1:  
      """
      - benchmark problem for multi-objective optimization:

        ● default mode: experiment.benchmark = experiment.benchmarks.DPF1():
             
          ○ arguments:     

            ● M = 3:   number of problem objectives 
            ● K = 5:   number represents the size of the vector K related to the decision variables.
            ● D = 2:   number of essential objectives
            ● P = 700: number of samples to the Pareto optimum.


        ● Notes:
          
          ○ selecting 'DPF1' in:
            
            ● experiment.benchmark = experiment.benchmarks.DPF1()
              ○ You can access more information about the method.

          ○ for more information:
            
            ● [general](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DPF1/) general information about the problem.
            ● [arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DPF/arguments/) custom and default settings problem. 
            ● [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DPF/exceptions/) information on possible error types
                
      """

      def __repr__(self):
            return self.__class__.__doc__