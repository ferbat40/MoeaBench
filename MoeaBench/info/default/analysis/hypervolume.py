from IPython.display import Markdown, display


class hypervolume:  

   

      def __call__(self):
        display(Markdown("""
      - array containing the hypervolume metric calculation:

      - default mode: hv = experiment.hypervolume()
             
        ○ arguments (default setting if no arguments are provided):     
              
          ● objective = [1,2...N]: calculates the hypervolume metric for all objectives. 
          ● generations = [0,N]: calculates the hypervolume metric for all generations.

      - Notes:
          
        ○ selecting 'hypervolume':
            
          ● hv = experiment.hypervolume()
            ○ You can access more information about the method.

        ○ for more information:
            
          ● [hypervolume](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/hypervolume/) 
            - information about the method, examples and more.
          ● [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) 
            - information on possible error types.
      """))