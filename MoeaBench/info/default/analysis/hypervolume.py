from IPython.display import Markdown, display


class hypervolume:  
      
   

      def __call__(self):
        display(Markdown("""
- **Array containing the hypervolume metric calculation**

- **Default mode:** `hv = experiment.hypervolume()`

- **Arguments (default if none provided):**
  - `objective = [1,2,...,N]`
  - `generations = [0,N]`

- **Notes:**
  - [Hypervolume docs](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/hypervolume/)
  - [Possible exceptions](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/)
"""))