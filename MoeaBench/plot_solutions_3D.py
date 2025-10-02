import ipywidgets as widgets
from IPython.display import display, Javascript
import numpy as np
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
    

     def __init__(self,DATA,BENCH,vet_pt):
         self.vet_pts=vet_pt
         self.BENCH=BENCH
         self.DATA=DATA

     

    
     

     def configure(self):
         with self.output:
             self.output.clear_output()  


         for idx_gen, gen in enumerate(self.vet_pts, start = 1):
              for idx_moea, pts in enumerate(gen, start = 0):
         
        # for gen,pts in enumerate(self.vet_pts, start = 1):
                 self.figure.add_trace(go.Scatter3d(
                 x=pts[:,0], y=pts[:,1], z=pts[:,2],
                 mode='markers',
                 marker=dict(size=3),  
                 name=f'Gen {idx_gen} Moea {idx_moea}',                       
                 showlegend=True,
                 hovertemplate = (f"Item {gen}<br>"
                                  f"{1}: %{{x}}<br>"
                                  f"{1}: %{{y}}<br>"
                                  f"{1}: %{{z}}<br><extra></extra>"),
                 ))   
       
      
         self.figure.update_layout(
                scene = dict(
                    xaxis=dict(title='axis X', showbackground=True, backgroundcolor="aliceblue", showgrid=True, gridcolor="#C3BDBD"),
                    yaxis=dict(title='axis Y', showbackground=True, backgroundcolor="aliceblue", showgrid=True, gridcolor="#C3BDBD"),
                    zaxis=dict(title='axis Z', showbackground=True, backgroundcolor="aliceblue", showgrid=True, gridcolor="#C3BDBD"),
                    aspectmode='manual',
                    aspectratio=dict(x=1,y=1,z=1)
                 ),
                 
                 width=900,
                 height=800,
                 margin=dict(l=0,r=0,b=0,t=0),
                 title=dict(
                     text=f'3D Solution Distribution Chart',
                     x=0.5,
                     xanchor='center',
                     y=0.9,
                     yanchor='bottom',
                     pad=dict(t=0),
                     font=dict(size=16, weight='bold')
                 ),
                 legend=dict(
                     x=1,
                     y=0.5,
                     xanchor='left',
                     yanchor='middle'
               )
            )



     def PLT(self): 
         self.output=widgets.Output()
         self.figure=go.FigureWidget()
         self.figure.data=() 
         self.ui = widgets.VBox([widgets.HBox([self.figure], layout=widgets.Layout(justify_content='center')),
                            widgets.HBox([self.output], layout=widgets.Layout(justify_content='center'))
                            ],
                            layout=widgets.Layout(margin='0px', padding = '0px'))
         display(self.ui)

