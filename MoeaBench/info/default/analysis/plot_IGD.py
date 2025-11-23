class plot_IGD:  
      """
      - calculate the IGD metric for any number of experiments and plot the graph:

      - default mode: moeabench.plot_IGD(exp1.result, exp2.result...)
             
        ○ arguments (default setting if no arguments are provided):     
              
          ● objective = [1,2...N]: calculates the IGD metric for all objectives. 
          ● generations = [0,N]: calculates the IGD metric for all generations.

      - Notes:
          
        ○ selecting "plot_IGD':
            
          ● moeabench.plot_IGD(exp1.result, exp2.result...)
            ○ You can access more information about the method.

        ○ for more information:
            
          ● [IGD](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/plot_IGD/)
            - information about the method, accepted variable types, examples and more.
            
          ● [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/exceptions/) 
            - information on possible error types.
      """
   

      def __repr__(self):
          return self.__class__.__doc__