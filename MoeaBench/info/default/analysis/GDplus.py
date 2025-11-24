from IPython.display import  display, Markdown

class GDplus:  
      
      def __call__(self):
          display(Markdown(f"""
- **array containing the GDplus metric calculation:**

  - **default mode: gd_plus = experiment.GDplus()**
             
    - arguments (default setting if no arguments are provided):     
              
      - objective = [1,2...N]: 
        - calculates the GDplus metric for all objectives. 
      - generations = [0,N]: 
        - calculates the GDplus metric for all generations.

  - **Notes:**
          
    - selecting 'GDplus':
            
      - gd_plus = experiment.GDplus()
        - You can access more information about the method.

  - **for more information access the links:**
            
    - [GDplus](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/GDplus/) 
      - information about the method, examples and more.
            
    - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) 
      - information on possible error types.
      """))