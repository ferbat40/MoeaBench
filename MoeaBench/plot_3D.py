import ipywidgets as widgets
from IPython.display import display
import plotly.graph_objects as go
import numpy as np
from .analyse import analyse
try:
    import google.colab
    from google.colab import output
    output.enable_custom_widget_manager()
except ImportError:
    pass


class plot_3D(analyse):
    
     def __init__(self,BENCH,vet_pt,experiments,axis, type = 'pareto-optimal front'):
         self.vet_pts=vet_pt
         self.BENCH=BENCH
         self.experiments=experiments
         self.axis = axis
         self.type=type
         

     def configure(self):
         self.figure=go.Figure()
         for exp,pts in zip (self.experiments,self.vet_pts):

                ax = pts[:,self.axis[0]]
                ay = pts[:,self.axis[1]]
                az = pts[:,self.axis[2]]
                msk = ~(np.isnan(ax) | np.isnan(ay) | np.isnan(az))
                if np.any(msk):
                 self.figure.add_trace(go.Scatter3d(
                 x=ax, y=ay, z=az,
                 mode='markers',
                 marker=dict(size=3),  
                 name=f'{exp}',                       
                 showlegend=True,
                 hovertemplate = (f"{exp}<br>"
                                  f"{self.axis[0]+1}: %{{x}}<br>"
                                  f"{self.axis[1]+1}: %{{y}}<br>"
                                  f"{self.axis[2]+1}: %{{z}}<br><extra></extra>"),
                 ))   
       
      
         self.figure.update_layout(
                scene = dict(
                    xaxis=dict(title=self.axis[0]+1, showbackground=True, backgroundcolor="aliceblue", showgrid=True, gridcolor="#C3BDBD"),
                    yaxis=dict(title=self.axis[1]+1, showbackground=True, backgroundcolor="aliceblue", showgrid=True, gridcolor="#C3BDBD"),
                    zaxis=dict(title=self.axis[2]+1, showbackground=True, backgroundcolor="aliceblue", showgrid=True, gridcolor="#C3BDBD"),
                    aspectmode='manual',
                    aspectratio=dict(x=1,y=1,z=1)
                 ),
                 
                 width=900,
                 height=800,
                 margin=dict(l=0,r=0,b=0,t=0),
                 title=dict(
                     text=f'3D Chart for {self.type}',
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