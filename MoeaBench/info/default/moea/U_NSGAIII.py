from IPython.display import  display, Markdown

class U_NSGAIII:  
        
      def __call__(self):
            display(Markdown(f"""
- **Evolutionary algorithm for multi-objective optimization problems:**

  - **Default mode: experiment.moea = moeabench.moea.U_NSGAIII():**
             
    - arguments (default setting if no arguments are provided):     

      - *population* = 150: number that represents the size of the population. 
      - *generations* = 300: number representing the size of generations.
      - *seed* = 1: number that represents the random seed of the algorithm.

  - **Notes:**
          
    - selecting *U_NSGAIII*:
            
      experiment.moea = moeabench.moea.U_NSGAIII()
      - You can access more information about the method.
                             
    - selecting *moea*:
            
      moeabench.moea
      - You can access a list of evolutionary algorithm problems and their respective links to obtain more information.


  - **For more information access the links:**
            
    - [general](https://moeabench-rgb.github.io/MoeaBench/algorithms/UNSGA3/) 
      references and more.

    - [arguments](https://moeabench-rgb.github.io/MoeaBench/algorithms/arguments/) 
      custom and default settings problem. 
              
    - [configurations](https://moeabench-rgb.github.io/MoeaBench/algorithms/configuration/) 
      algorithm configuration adopted by MoeaBench.               
      
      """))