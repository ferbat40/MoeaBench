from IPython.display import Markdown, display


class hypervolume:  
      
   

       def __call__(self):
        display(Markdown("""
- **Array containing the hypervolume metric calculation**

- **Default mode:** `hv = experiment.hypervolume()`
    
  - **Arguments (default if none provided):**
      - `objective = [1,2,...,N]`: calculates the hypervolume metric for all objectives
      - `generations = [0,N]`: calculates the hypervolume metric for all generations

- **Notes:**
    - Selecting 'hypervolume':
        - `hv = experiment.hypervolume()` → You can access more information about the method
    - For more information:
        - [hypervolume metric documentation](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/hypervolume/)
        - [Possible exceptions](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/)
"""))