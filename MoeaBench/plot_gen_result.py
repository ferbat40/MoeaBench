import ipywidgets as widgets
from IPython.display import display
import numpy as np
import plotly.graph_objects as go
import numpy as np
from .analyse import analyse


class plot_gen_result(analyse):

    def __init__(self,gen_moea,experiments,generation,metric = ['objectives','Generations']):
        self.gen_moea=gen_moea
        self.experiments=experiments
        self.metric=metric
        self.generation=generation
        

    def configure(self):
         self.figure=go.Figure()  
         for moea, gener in zip(self.gen_moea, self.generation):
               for exp, pts in enumerate(moea , start = 0):

                    y_pts = np.mean(np.array(pts))   
                    #gen=np.array(gener)
                    
                    #y_pts=np.array(pts).flatten()
                    #gen_arr = np.full_like(y_pts,gener)
                    self.figure.add_trace(go.Scatter(
                     x = y_pts, y = gener,
                     mode='lines+markers',
                     marker=dict(size=3),
                     name=f'{self.experiments[exp]} for gen {gener}',
                     showlegend=True,
                     hovertemplate = (f"{self.experiments[exp]} for gen {gener}<br>"
                                f"{self.metric[1]}: %{{y:.0f}}<br>"
                                f"{self.metric[0]}: %{{x}}<br><extra></extra>"),
                                
                                ))
         
         self.figure.update_layout(                          
                     xaxis=dict(title=self.metric[0], showgrid=False),
                     yaxis=dict(title=self.metric[1], showgrid=False),
                     margin=dict(l=70,r=150,b=80,t=140),
                     plot_bgcolor="#FAFAFA",
                     paper_bgcolor="white",
                     width=900,
                     height=800,
                     title=dict(
                         text=f'2D Convergence Chart',
                         x=0.5,
                         xanchor='center',
                         y=0.9,
                         yanchor='top',
                         pad=dict(t = 10, b = 140),
                         font=dict(size=16)),
                         legend=dict(x=1.05,
                                     y=0.5,
                                     xanchor='left',
                                     yanchor='middle',
                                     font=dict(size=11)))
         self.PLT()
      

   

 



    

