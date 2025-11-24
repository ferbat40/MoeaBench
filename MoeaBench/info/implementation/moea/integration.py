from IPython.display import  display, Markdown

class integration:  
      
      def __call__(self):
          display(Markdown("""
- **integrates the user's evolutionary algorithm into MoeaBench:**
                           
    The user implementation becomes part of the framework to be used as a 
    native implementation.
                        
    
    - usage example:
      
      - on the user side:                     
                           
        The user downloads the file from their repository.
                           
        - !pip install git+https://github.com/moeabench-rgb/my_implementations.git
      
        The user imports their file into Colab.
        
        - from my_implementations.NSGA2deap import my_NSGA2dea
      
      - on the MoeaBench side:
               
        Add your import to MoeaBench wuth:
        - moeabench.add_moea(my_NSGA2deap)

    - **General rules**
             
        - Any evolutionary algorithm can be integrated, provided it conforms 
        to the integration rules.     
                           
    
    - **Supported implementations**:
    
        - Implemented in Google Colab cells to run in memory.
                           
                        
    - **User options with:**
                           
        - Native implementations of MoeaBench benchmark problems.
                           
        - user-implemented benchmark problem. 
    
    - **Example**:
      
        - NSGA-II algorithm implemented with the DEAP library.
        

    - **For more information access the links:**
            
        - [example code](https://moeabench-rgb.github.io/MoeaBench/implement_moea/example_code/example_code/) 
          - Detailed information on the implementation process of the example mentioned.
            
        - [possible execution combinations](https://moeabench-rgb.github.io/MoeaBench/experiments/combinations/combinations/) 
          - MoeaBench allows combinations for running algorithms with benchmark problems.
      """))