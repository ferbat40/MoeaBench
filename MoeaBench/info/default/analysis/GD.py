from IPython.display import  display, Markdown

class GD:  
         
      def __call__(self):
          display(Markdown(f"""
- **array containing the GD metric calculation:**

  - **default mode: gd = experiment.GD()**
             
    - arguments (default setting if no arguments are provided):     
              
      - objective = [1,2...N]: 
        - calculates the GD metric for all objectives. 
      - generations = [0,N]: 
        - calculates the GD metric for all generations.

  - **Notes:**
          
    - selecting 'GD':
            
      gd = experiment.GD()
      You can access more information about the method.

  - **for more information access the links:**
            
    - [GD](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/GD/) 
      - information about the method, examples and more.
            
    - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) 
      - information on possible error types.
      """))