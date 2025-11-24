from IPython.display import  display, Markdown

class code:  
      
      def __call__(self):
          display(Markdown("""
- **User implementation for their own evolutionary algorithm:**
                           
    Custom implementations can also be used with MoeaBench.

    - **General rules**
             
        - Any evolutionary algorithm can be implemented, as long as it conforms
        to the implementation rules.     
                           
    
    - **Supported implementations**:
    
        - Implemented in Google Colab cells to run in memory.
                           
        - Implemented in a file and coupled to MoeaBench via the user's 
        repository on GitHub.
                        
    - **User options:**
                           
        - Native implementations of MoeaBench benchmark problems.
                           
        - user-implemented benchmark problem. 
    
    - **Example**:
      
        - NSGA-II algorithm implemented with the DEAP library..
        

    - **For more information access the links:**
            
        - [example code](https://moeabench-rgb.github.io/MoeaBench/implement_moea/example_code/example_code/) 
          Detailed information on the implementation process of the example mentioned.
            
        - [possible execution combinations](https://moeabench-rgb.github.io/MoeaBench/experiments/combinations/combinations/) 
          MoeaBench allows combinations for running algorithms with benchmark problems.
      """))