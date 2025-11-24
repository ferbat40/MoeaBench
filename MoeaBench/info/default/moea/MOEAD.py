from IPython.display import  display, Markdown

class MOEAD:  
     
      def __call__(self):
            display(Markdown(f"""
- evolutionary algorithm for multi-objective optimization problems:

  - default mode: experiment.moea = experiment.moea.MOEAD():
             
    - arguments (default setting if no arguments are provided):     

      - population = 150: number that represents the size of the population 
      - generations = 300: number representing the size of generations.
      - seed = 1: number that represents the random seed of the algorithm.

  - Notes:
          
    - selecting 'MOEAD':
            
      - experiment.moea = experiment.moea.MOEAD()
        - You can access more information about the method.

  - for more information access the links:
            
    - [general](https://moeabench-rgb.github.io/MoeaBench/algorithms/MOEAD/) 
      - references and more.

    - [arguments](https://moeabench-rgb.github.io/MoeaBench/algorithms/arguments/) 
      - custom and default settings problem. 

    - [configurations](https://moeabench-rgb.github.io/MoeaBench/algorithms/configuration/) 
      - algorithm configuration adopted by MoeaBench.               
      """))