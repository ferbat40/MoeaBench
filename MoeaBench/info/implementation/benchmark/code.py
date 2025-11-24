from IPython.display import  display, Markdown

class code:  
      
      def __call__(self):
          display(Markdown("""
- **User implementation for their own benchmark problem:**

  - **features**
             
    - Any benchmark problem can be implemented as long as it adheres to 
    implementation rules:     
    
    - possibilities of use:
    
      - Implemented in Google Colab cells to run in memory.
                           
      - Implemented in a file and coupled to MoeaBench via the user's 
      repository on GitHub.
    
    - proposed example:
      
      - Deb's DTLZ5 benchmark problem.
    
              
    - A user-implemented problem can be used by: 
                           
      - native implementations of MoeaBench algorithms.
                           
      - user-implemented algorithm.
       

  - **for more information access the links:**
            
    - [example code](https://moeabench-rgb.github.io/MoeaBench/implement_benchmark/example_code/example_code/) 
      - Detailed information on the implementation process of the example mentioned.
            
    - [Exception](https://moeabench-rgb.github.io/MoeaBench/experiments/combinations/combinations/) 
      - MoeaBench allows combinations for running algorithms with benchmark problems.
      """))