from IPython.display import  display, Markdown

class plot_hypervolume:  
      
      def __call__(self):
          display(Markdown(f"""
- **calculate the hypervolume metric for any number of experiments and plot the graph:**

  - **default mode: moeabench.plot_hypervolume(exp1.result, exp2.result...)**
             
    - arguments (default setting if no arguments are provided):     
              
      - objective = [1,2...N]: 
        - calculates the hypervolume metric for all objectives. 
      - generations = [0,N]: 
        - calculates the hypervolume metric for all generations.

  - **Notes:**
          
    - selecting "plot_hypervolume':
            
      moeabench.plot_hypervolume(exp1.result, exp2.result...)
      - You can access more information about the method.

  - **for more information access the links:**
            
    - [plot_hypervolume](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/plot_hypervolume/)
      - information about the method, accepted variable types, examples and more.
            
    - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/plot/exceptions/) 
      - information on possible error types.
      """))