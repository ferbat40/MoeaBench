from IPython.display import  display, Markdown

class hypervolume:  
    
      def __call__(self):
          display(Markdown(f"""
- **Array containing the hypervolume metric calculation:**

  - **Default mode: hv = experiment.hypervolume()**
             
    - arguments (default setting if no arguments are provided):     
              
      - *objective* = [1,2...N]: calculates the hypervolume metric for all objectives. 
      - *generations* = [0,N]: calculates the hypervolume metric for all generations.

  - **Notes:**
          
    - selecting *hypervolume*:
            
      hv = experiment.hypervolume()
      - ou can access more information about the method.

  - **For more information access the links:**
            
    - [hypervolume](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/hypervolume/) 
      information about the method, examples and more.
            
    - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) 
      information on possible error types.
      """))
