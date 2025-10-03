import ipywidgets as widgets
from IPython.display import display, Javascript
import plotly.graph_objects as go
import numpy as np
import json
try:
    import google.colab
    from google.colab import output
    output.enable_custom_widget_manager()
except ImportError:
    pass


class plot_solutions_3D:
    

     def __init__(self,DATA,BENCH,vet_pt,generations,experiments):
         self.vet_pts=vet_pt
         self.BENCH=BENCH
         self.DATA=DATA
         self.generations=generations
         self.experiments=experiments
         
     def sdf(self):
         
        for idx_gen, gen in enumerate(self.vet_pts, start = self.generations[0]):
              for idx_moea, pts in enumerate(gen, start = 0):
                  print(idx_gen,pts,self.experiments[idx_moea], "sdf")


     def configure(self):


         #self.figure=go.Figure()
         for idx_gen, gen in enumerate(self.vet_pts, start = self.generations[0]):
              for idx_moea, pts in enumerate(gen, start = 0):
                  print(idx_gen,pts,self.experiments[idx_moea]," configure")

                 


    

