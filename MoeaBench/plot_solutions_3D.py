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
    

     def __init__(self,DATA,BENCH,vet_pt,generations,experiments,axis):
         self.vet_pts=vet_pt
         self.BENCH=BENCH
         self.DATA=DATA
         self.generations=generations
         self.experiments=experiments
         self.axis = axis


     def configure(self):
         self.figure=go.Figure()
         for idx_gen, gen in enumerate(self.vet_pts, start = self.generations[0]):
              for idx_moea, pts in enumerate(gen, start = 0):
                ax = pts[:,self.axis[0]]
                ay = pts[:,self.axis[1]]
                az = pts[:,self.axis[2]]
                msk = ~(np.isnan(ax) | np.isnan(ay) | np.isnan(az))
                if np.any(msk):
                 self.figure.add_trace(go.Scatter3d(
                 x=ax, y=ay, z=az,
                 mode='markers',
                 marker=dict(size=3),  
                 name=f'{self.experiments[idx_moea]} for generation {idx_gen}',                       
                 showlegend=True,
                 hovertemplate = (f"{self.experiments[idx_moea]} - gen {idx_gen}<br>"
                                  f"X: %{{x}}<br>"
                                  f"Y: %{{y}}<br>"
                                  f"Z: %{{z}}<br><extra></extra>"),
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
                     font=dict(size=16)
                 ),
                 legend=dict(
                     x=1,
                     y=0.5,
                     xanchor='left',
                     yanchor='middle'
               )
            )
         self.PLT()


     def PLT(self):  
         out = widgets.Output()
         with out:
             display(self.figure)
         self.ui = widgets.VBox([widgets.HBox([out], layout=widgets.Layout(justify_content='center')),
                             ])
         display(self.ui)



    

