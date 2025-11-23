from IPython.display import Markdown, display


class hypervolume:  
   
      def __call__(self):
        display(Markdown("""
- **Array containing the hypervolume metric calculation**

- **Default mode:** 
    - hv = experiment.hypervolume()

- **arguments (default setting if no arguments are provided):**
  - objective = [1,2...N]: calculates the hypervolume metric for all objectives.                      
  - generations = [0,N]: calculates the hypervolume metric for all generations.                    


- **Notes:**
                         
  - selecting 'hypervolume':
    - hv = experiment.hypervolume()
      - You can access more information about the method.
  
  - for more information:
                         
    - [Hypervolume docs](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/hypervolume/)
      - information about the method, examples and more.  
    - [Possible exceptions](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/)
      - information on possible error types. 
"""))