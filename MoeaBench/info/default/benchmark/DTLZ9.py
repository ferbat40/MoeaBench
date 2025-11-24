from IPython.display import  display, Markdown

class DTLZ9:  
      
      def __call__(self):
            display(Markdown(f"""
- **Benchmark problem for multi-objective optimization:**

  - **Default mode: experiment.benchmark = moeabench.benchmarks.DTLZ9():**
             
    - arguments (default setting if no arguments are provided):    
                  
      - *M* = 3: number of problem objectives 
      - *N* = 10: number of decision variables.
      - *P* = 700: number of samples to the Pareto optimum.


  - **Notes:**
          
    - selecting *DTLZ9*:
            
      experiment.benchmark = moeabench.benchmarks.DTLZ9()
      - You can access more information about the method.
                             

    - selecting *benchmark*:
            
      experiment.benchmark
      - You can access a list of benchmark issues and their respective links for more information.

  - **For more information access the links:**
            
    - [general](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ9/) 
      general information about the problem.

    - [arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ8/arguments/) 
      custom and default settings problem. 

    - [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DTLZ/DTLZ8/exceptions/) 
      information on possible error types          
      """))