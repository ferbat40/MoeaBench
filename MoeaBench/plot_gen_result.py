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
         
         #all_y=[]  
         for moea, gener in zip(self.gen_moea, self.generation):
               for exp, pts in enumerate(moea , start = 0):
                   
                    
                    gen=np.array(gener)
                    y_pts=np.round(pts,1)
                    #all_y.append(pts)
                    self.figure.add_trace(go.Scatter(
                     x = gen, y = y_pts,
                     mode='markers',
                     marker=dict(size=3),
                     name=f'{self.experiments[exp]} for gen {gen}',
                     showlegend=True,
                     hovertemplate = (f"{self.experiments[exp]} for gen {gen}<br>"
                                f"{self.metric[0]}: %{{y}}<br>"
                                f"{self.metric[1]}: %{{y}}<br><extra></extra>"),
                                
                                ))
         #all_y=np.concatenate(all_y)
         #y_min, y_max = np.nanmin(all_y), np.nanmax(all_y)
         
         self.figure.update_layout(       
                     xaxis=dict(title=self.metric[1],  gridcolor="#C3BDBD"),
                     yaxis=dict(title=self.metric[0],  gridcolor="#C3BDBD"),
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
      

   

 



    

