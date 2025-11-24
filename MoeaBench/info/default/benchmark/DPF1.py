from IPython.display import  display, Markdown

class DPF1:  
    
      def __call__(self):
            display(Markdown(f"""
- **benchmark problem for multi-objective optimization:**

  - **default mode: experiment.benchmark = experiment.benchmark.DPF1():**
             
    - arguments (default setting if no arguments are provided):      

      - M = 3:   
        - number of problem objectives 
      - K = 5:   
        - number represents the size of the vector K related to the decision variables.
      - D = 2:   
        - number of essential objectives
      - P = 700: 
        - number of samples to the Pareto optimum.


  - **Notes:**
          
    - selecting 'DPF1':
            
      experiment.benchmark = experiment.benchmark.DPF1()
      You can access more information about the method.

  - **for more information access the links:**
            
    - [general](https://moeabench-rgb.github.io/MoeaBench/problems/DPF/DPF1/) 
      - general information about the problem.

    - [arguments](https://moeabench-rgb.github.io/MoeaBench/problems/DPF/arguments/) 
      - custom and default settings problem. 
              
    - [Exception](https://moeabench-rgb.github.io/MoeaBench/problems/DPF/exceptions/) 
      - information on possible error types
                
      """))