from IPython.display import  display, Markdown

class DTLZ1:  
    
      def __call__(self):
            display(Markdown(f"""
- benchmark problem for multi-objective optimization:

  - default mode: experiment.benchmark = experiment.benchmark.DTLZ1():
             
    - arguments (default setting if no arguments are provided):    

      - M = 3:   number of problem objectives 
      - K = 5:   number represents the size of the vector K related to the decision variables.
      - P = 700: number of samples to the Pareto optimum.


  - Notes:
          
    - selecting 'DTLZ1':
            
      - experiment.benchmark = experiment.benchmark.DTLZ1()
        - You can access more information about the method.

  - for more information access the links:
            
    - [general](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ1/) 
      - general information about the problem.

    - [arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/arguments/) 
      - custom and default settings problem. 
              
    - [exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/exceptions/) 
      - information on possible error types
             
      """))