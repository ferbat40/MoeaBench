from IPython.display import  display, Markdown

class IGD:  
      
      def __call__(self):
          display(Markdown(f"""
- **Array containing the IGD metric calculation:**

  - **Default mode: igd = experiment.IGD()**
             
    - arguments (default setting if no arguments are provided):     
              
      - *objective* = [1,2...N]: calculates the IGD metric for all objectives. 
      - *generations* = [0,N]: calculates the IGD metric for all generations.

  - **Notes**:
          
    - selecting *IGD*:
            
      igd = experiment.IGD()
      - You can access more information about the method.

  - **For more information access the links:**
            
    - [IGD](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/IGD/) 
      information about the method, examples and more.
            
    - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) 
      information on possible error types.
      """))