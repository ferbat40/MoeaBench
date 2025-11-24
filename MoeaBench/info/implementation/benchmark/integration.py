from IPython.display import  display, Markdown

class integration:  
      
      def __call__(self):
          display(Markdown("""
- **Integrates the user's benchmark problem into MoeaBench:**
                           
    The user implementation becomes part of the framework to be used as a 
    native implementation.
                        
    
    - **usage example**:
      
      - on the user side:                     
                           
        The user downloads the file from their repository.
                           
        - !pip install git+https://github.com/moeabench-rgb/my_implementations.git
      
        The user imports their file into Colab.
        
        - from my_implementations.my_dtlz5 import my_dtlz5
      
      - on the MoeaBench side:
               
        Add your import to MoeaBench with:
        - moeabench.add_benchmark(my_dtlz5)

    - **General rules**
                                        
        - Any benchmark issue can be integrated, provided it complies with 
        the integration rules.
                           
    
    - **Supported implementations**:
    
        - Implemented in Google Colab cells to run in memory.
                           
                        
    - **User options:**
                           
        - Native implementations of MoeaBench benchmark problems.
                           
        - user-implemented benchmark problem. 
    
    - **Example**:
      
        - Deb's DTLZ5 benchmark problem.
                           
    - selecting 'add_benchmark':
            
      moeabench.add_benchmark()
      - You can access more information about the method.       

    - **For more information access the link:**
            
        - [integration](https://moeabench-rgb.github.io/MoeaBench/implement_benchmark/integration/integration/) 
          - Detailed information about the integration process of the example mentioned.
            
        """))