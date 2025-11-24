from IPython.display import  display, Markdown

class DTLZ2:  
      
      def __call__(self):
            display(Markdown(f"""
- **Benchmark problem for multi-objective optimization:**

  - **Default mode: experiment.benchmark = moeabench.benchmarks.DTLZ2():**
             
    - arguments (default setting if no arguments are provided):     
                  
      - *M* = 3: number of problem objectives 
      - *K* = 5: number represents the size of the vector K related to the decision variables.
      - *P* = 700: number of samples to the Pareto optimum.


  - **Notes:**
          
    - selecting *DTLZ2*:
            
      experiment.benchmark = moeabench.benchmarks.DTLZ2()
      - You can access more information about the method.
                             
    - selecting *benchmark*:
            
      experiment.benchmark
      - You can access a list of benchmark issues and their respective links for more information.

  - **For more information access the links:**
            
    - [general](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ2/) 
      general information about the problem.

    - [arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/arguments/) 
      custom and default settings problem. 

    - [exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/exceptions/) 
      information on possible error types            
      """))