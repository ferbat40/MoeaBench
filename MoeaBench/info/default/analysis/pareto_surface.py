from IPython.display import  display, Markdown

class pareto_surface:  
  
      def __call__(self):
          display(Markdown(f"""
- **Plot a graph related to the Pareto optimal front surface for any number of experiments.**
  - **accepting two types of acceptable variables.:**
        
    - experiment.pof: 
      - referring to samples of the Pareto optimal front of the problem.

    - experiment.result: 
      - referring to solutions found by an evolutionary algorithm on the Pareto optimal front.

  - **default mode: moeabench.pareto_surface(exp1.result, exp2.pof, exp2.result...)**
             
    - arguments (default setting if no arguments are provided):     
              
    - objective = [1,2,3]: 
      - plot the graph considering the first three objectives.

  - **Notes:**
          
    - selecting "pareto_surface':
            
      moeabench.pareto_surface(exp1.result, exp2.pof, exp2.result...)
      You can access more information about the method.

  - **for more information access the links:**
            
    - [pareto_surface](https://moeabench-rgb.github.io/MoeaBench/analysis/objectives/plot/pareto_surface/)
      - information about the method, accepted variable types, examples and more.
            
    - [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/objectives/plot/exceptions/) 
      - information on possible error types.
      """))