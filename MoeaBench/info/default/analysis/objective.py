from IPython.display import Markdown, display

class objective:  
    
    
    def __call__(self):
        display(Markdown("""
- **array with objectives in generations:**

- **default mode:**
    - obj = experiment.objective():
             
- **arguments (default setting if no arguments are provided):**             
    - objective = [1]: returns the first objective  
    - generations = [0,N]: It returns the goal for all generations.

                     
- **Notes:**
          
    - selecting 'objective':        
      - obj = experiment.objective()
        - You can access more information about the method.

    - for more information:
            
      - [Ibjective docs](https://moeabench-rgb.github.io/MoeaBench/analysis/objectives/data/objective/) 
        - information about the method.
      - [Possible exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) 
        - information on possible error types. 
            
"""))
      
          
     
