from IPython.display import  display, Markdown

class DPF2:  
    
      def __call__(self):
            display(Markdown(f"""
- **Benchmark problem for multi-objective optimization:**

  - **Default mode: experiment.benchmark = experiment.benchmark.DPF2():**
             
    - arguments (default setting if no arguments are provided):    

      - *M* = 3: number of problem objectives 
      - *K* = 5: number represents the size of the vector K related to the decision variables.
      - *D* = 2: number of essential objectives
      - *P* = 700: number of samples to the Pareto optimum.


  - **Notes:**
          
    - selecting 'DPF2':
            
      experiment.benchmark = experiment.benchmark.DPF2()
      - You can access more information about the method.
                             
    
    - selecting *benchmark*:
            
      experiment.benchmark
      - You can access a list of benchmark issues and their respective links for more information.

  - **For more information access the links:**
            
    - [general](https://moeabench-rgb.github.io/MoeaBench/problems/DPF/DPF2/) 
      general information about the problem.

    - [arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DPF/arguments/) 
      custom and default settings problem. 

    - [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DPF/exceptions/)
      information on possible error types
           
      """))