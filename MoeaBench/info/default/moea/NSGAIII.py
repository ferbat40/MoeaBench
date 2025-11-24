from IPython.display import  display, Markdown

class NSGAIII:  
      
      def __call__(self):
            display(Markdown(f"""
- **Evolutionary algorithm for multi-objective optimization problems:**

  - **Default mode: experiment.moea = experiment.moea.NSGAIII():**
             
    - arguments (default setting if no arguments are provided):    

      - *population* = 150: number that represents the size of the population 
      - *generations* = 300: number representing the size of generations.
      - *seed* = 1: number that represents the random seed of the algorithm.

  - **Notes:**
          
    - selecting *NSGAIII*:
            
      experiment.moea = experiment.moea.NSGAIII()
      - You can access more information about the method.

  - **For more information access the links:**
            
    - [general](https://moeabench-rgb.github.io/MoeaBench/algorithms/NSGA3/) 
      references and more.

    - [arguments](https://moeabench-rgb.github.io/MoeaBench/algorithms/arguments/) 
      custom and default settings problem. 

    - [configurations](https://moeabench-rgb.github.io/MoeaBench/algorithms/configuration/) 
      algorithm configuration adopted by MoeaBench.               
      
      """))