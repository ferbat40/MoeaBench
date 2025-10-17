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
             
         #for pts in self.gen_moea:
             for metric, gen in zip(self.generation,self.experiments):
     
                    gen=np.array(gen)
                    metric=np.array(metric)
                    self.figure.add_trace(go.Scatter(
                     x = gen, y = metric,
                     mode='lines+markers',
                     marker=dict(size=3),
                     name=f'{lbl}',
                     showlegend=True,
                     hovertemplate = (f"{lbl}<br>"
                                f"{self.metric[1]}: %{{x}}<br>"
                                f"{self.metric[0]}: %{{y}}<br><extra></extra>"),
                                
                                ))
             self.figure.update_layout(       
                     xaxis=dict(title=self.metric[1], showgrid=True, gridcolor="#C3BDBD"),
                     yaxis=dict(title=self.metric[0], showgrid=True, gridcolor="#C3BDBD"),
                     margin=dict(l=70,r=150,b=80,t=140),
                     plot_bgcolor="#FAFAFA",
                     paper_bgcolor="white",
                     width=800,
                     height=700,
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
      

   

 



    

