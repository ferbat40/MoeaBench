from IPython.display import Markdown, display


class IGD:  
      """
      - array containing the IGD metric calculation:

      - default mode: igd = experiment.IGD()
             
        ○ arguments (default setting if no arguments are provided):     
              
          ● objective = [1,2...N]: calculates the IGD metric for all objectives. 
          ● generations = [0,N]: calculates the IGD metric for all generations.

      - Notes:
          
        ○ selecting 'IGD':
            
          ● igd = experiment.IGD()
            ○ You can access more information about the method.

        ○ for more information:
            
          ● [IGD](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/IGD/) 
            - information about the method, examples and more.
            
          ● [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) 
            - information on possible error types.
      """
   

      def __repr__(self):
          return self.__class__.__doc__