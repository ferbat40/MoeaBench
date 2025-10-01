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
         self.vet_pt=vet_pt
         self.BENCH=BENCH
         self.DATA=DATA
         self.output=widgets.Output()
         self.figure=go.FigureWidget()
         self.figure.data=()
     

     def parameters(self):
         self.vet_pts=[ (i - np.min(i,axis = 0)) / (np.max(i,axis = 0)-np.min(i,axis = 0))   for i in self.vet_pt]  
         self.list_axis = np.array([[0,1,2] if i > 0 else [None,None,None] for i in range(0,len(self.BENCH)+1)])
         self.configure(0)
     

     def configure(self,b):
         with self.output:
             self.output.clear_output()  
         colors = ['red', 'blue', 'green','orange','purple','black','brown','yellow','cyan','gray']
         self.figure.data=()
         for index,(ax,pts, color) in enumerate(zip(self.list_axis[1:],self.vet_pts, colors), start=1):
             self.figure.add_trace(go.Scatter3d(
                 x=pts[:, ax[0]], y=pts[:, ax[1]], z=pts[:, ax[2]],
                 mode='markers',
                 marker=dict(size=3, color=color),  
                 name=f'Item {index}',                       
                 showlegend=True,
                 hovertemplate = (f"Item {index}<br>"
                                  f"{ax[0]+1}: %{{x}}<br>"
                                  f"{ax[1]+1}: %{{y}}<br>"
                                  f"{ax[2]+1}: %{{z}}<br><extra></extra>"),
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
         self.ui = widgets.VBox([widgets.HBox([self.figure], layout=widgets.Layout(justify_content='center')),
                            widgets.HBox([self.output], layout=widgets.Layout(justify_content='center'))
                            ],
                            layout=widgets.Layout(margin='0px', paddin = '0px'))
         display(self.ui)

