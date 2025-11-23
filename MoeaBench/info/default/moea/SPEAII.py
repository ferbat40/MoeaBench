class SPEAII:  
      """
      - evolutionary algorithm for multi-objective optimization problems:

        ● default mode: experiment.moea = experiment.moeas.SPEAII():
             
          ○ arguments:     

            ● population = 150: number that represents the size of the population 
            ● generations = 300: number representing the size of generations.
            ● seed = 1: number that represents the random seed of the algorithm.

        ● Notes:
          
          ○ selecting 'SPEAII' in:
            
            ● experiment.moea = experiment.moeas.SPEAII()
              ○ You can access more information about the method.

          ○ for more information:
            
            ● [general](https://moeabench-rgb.github.io/MoeaBench/algorithms/SPEAII/) references and more...
            ● [arguments](https://moeabench-rgb.github.io/MoeaBench/algorithms/arguments/) custom and default settings problem. 
            ● [configurations](https://moeabench-rgb.github.io/MoeaBench/algorithms/configuration/) algorithm configuration adopted by MoeaBench.               
      """
   
      def __repr__(self):
            return self.__class__.__doc__