from IPython.display import  display, Markdown

class code:  
      
      def __call__(self):
          display(Markdown("""
- **User implementation for their own benchmark problem:**
                           
    Custom implementations can also be used with MoeaBench.

    - **General rules**
             
        - Any benchmark problem can be implemented as long as it adheres to 
        implementation rules.     
    
    - **Supported implementations**:
    
        - Implemented in Google Colab cells to run in memory.
                           
        - Implemented in a file and coupled to MoeaBench via the user's 
        repository on GitHub.
                        
    - **User options with:**
                           
        - native implementations of MoeaBench algorithms.
                           
        - user-implemented algorithm. 
    
    - **Example**:
      
        - Deb's DTLZ5 benchmark problem.
        

    - **For more information access the links:**
            
        - [example code](https://moeabench-rgb.github.io/MoeaBench/implement_benchmark/example_code/example_code/) 
          - Detailed information on the implementation process of the example mentioned.
            
        - [possible execution combinations](https://moeabench-rgb.github.io/MoeaBench/experiments/combinations/combinations/) 
          - MoeaBench allows combinations for running algorithms with benchmark problems.
      """))