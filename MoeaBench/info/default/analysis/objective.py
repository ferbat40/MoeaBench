class objective:  
      """
      - array with objectives in generations:

      - default mode: obj = experiment.objective():
             
        ○ arguments (default setting if no arguments are provided):             
          ● objective = [1,2...N]: returns the first objective  
          ● generations = [0,N]: It returns the goal for all generations.

                     
      - Notes:
          
        ○ selecting 'objective' in:
            
          ● obj = experiment.objective()
            ○ You can access more information about the method.

      - for more information:
            
        ● [objective](https://moeabench-rgb.github.io/MoeaBench/analysis/objectives/data/objective/) 
          - information about the method.

        ● [Exception](https://moeabench-rgb.github.io/MoeaBench/analysis/metrics/data/exceptions/) 
          - information on possible error types. 
            
      """


      def __repr__(self):
            return self.__class__.__doc__
      
          
     
