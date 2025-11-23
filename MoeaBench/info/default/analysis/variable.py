
class variable:  
      """
      - array with variables in generations:

        ● default mode: var = experiment.variable():
             
          ○ arguments:             
            ● variable: returns the first objective  
            ● generations: It returns the goal for all generations.

                     
        ● Notes:
          
          ○ selecting 'variable' in:
            
            ● var = experiment.variable()
              ○ You can access more information about the method.

          ○ for more information:
            
            ● [variable](https://moeabench-rgb.github.io/MoeaBench/analysis/variables/data/variable/) information about the method.
            ● [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types. 
            
      """


     def __call__(self):
        display(Markdown("""
- **array with objectives in generations:**

- **default mode:**
    - obj = experiment.objective():
             
- **arguments (default setting if no arguments are provided):**             
    - objective: returns the first objective  
    - generations: It returns the goal for all generations.

                     
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