from IPython.display import  display, Markdown

class IGDplus:  
      
      def __call__(self):
          display(Markdown("""
- **Array containing the IGDplus metric calculation:**

  - **Default mode: igd_plus = experiment.IGDplus()**
             
    - arguments (default setting if no arguments are provided):     
              
      - *objective* = [1,2...N]: calculates the IGDplus metric for all objectives. 
      - *generations* = [0,N]: calculates the IGDplus metric for all generations.

  - **Notes:**
          
    - selecting *IGDplus*:
            
      igd_plus = experiment.IGDplus()
      - You can access more information about the method.

  - **For more information access the links:**
            
    - [IGDplus](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/IGDplus/) 
      information about the method, examples and more.
            
    - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) 
      information on possible error types.
      """))