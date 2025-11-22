class variable:  
      """
      - array with variables in generations:

        ● default mode: experiment.variable():
             
          ○ arguments:             
            ● variable: returns the first objective  
            ● generations: It returns the goal for all generations.

                     
        ● Notes:
          
          ○ selecting 'variable' in:
            
            ● var = experiment.variable()
              ○ You can access more information about the method.

          ○ for more information:
            
            ● [variable](https://moeabench-rgb.github.io/MoeaBench/analysis/variables/data/variable/) information about the method.
            ● [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) information on possible error types. 
            
      """


      def __repr__(self):
            return self.__class__.__doc__