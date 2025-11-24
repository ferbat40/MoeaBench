from IPython.display import  display, Markdown


class variable:  


      def __call__(self):
            
            display(Markdown(f"""
                          
- array with variables in generations:

  - default mode: var = experiment.variable():
             
    - arguments (default setting if no arguments are provided):           
      - variable = [1,2...N]: returns the first objective  
      - generations = [0,N]: It returns the goal for all generations.

                     
    - Notes:
          
      - selecting 'variable' in:
            
        - var = experiment.variable()
        - You can access more information about the method.

    - for more information:
            
      - [variable](https://moeabench-rgb.github.io/MoeaBench/analysis/variables/data/variable/) 
        - information about the method.

      - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) 
        - information on possible error types. 
   """ ))