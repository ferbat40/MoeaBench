import ipywidgets as widgets
from IPython.display import display
import numpy as np
import plotly.graph_objects as go
import numpy as np
from .analyse import analyse


class plot_gen(analyse):

    def __init__(self,markers,label,title,metric):
        self.markers=markers
        self.label=label
        self.title=title
        self.metric=metric
        self.axis_DATA=[]
       

    def axis(self, b):
       try:
         self.axis_DATA=[]
         value = b['new']
         mtc=self.metric
         first = mtc.index(value)
         end = 1-first
         if self.metric != [mtc[end],mtc[first]]:
            self.metric = [mtc[end],mtc[first]]
            self.markers=self.markers[::-1]
         for x,y in zip(self.markers[0],self.markers[1]):
           self.axis_DATA.append([x,y])  
       except Exception as e:
          print(e)
       
    
    def configure(self,b):
       try:
          with self.output:
             self.output.clear_output()  
             vet_pts=[i for i in self.axis_DATA]
             #print("markers[0]   " , self.markers[0], "markers[1]   " , self.markers[1])
             self.figure.data=()
             for gen, metric,  lbl in zip( self.markers[0],  self.markers[1], self.label ):
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
                         font=dict(size=16, 
                         weight='bold')),
                         legend=dict(x=1.05,
                                     y=0.5,
                                     xanchor='left',
                                     yanchor='middle',
                                     font=dict(size=11, weight='bold')))
       except Exception as e:
          print(e)
      

    def PLT(self):  
        self.axis_change = widgets.Dropdown(options=[('',None),(self.metric[1],self.metric[1]),(self.metric[0],self.metric[0])] , description="<span style='font-size:14px; color:blue; font-weight:bold;'>AXIS X</span>")
        self.output=widgets.Output()
        self.figure=go.FigureWidget()
        self.figure.data=()
        self.button = widgets.Button(description="PLOT", style = widgets.ButtonStyle(button_color='deepskyblue', font_weight='bold'))
        self.axis_change.observe(self.axis, names = 'value')
        self.button.on_click(self.configure) 
        ui = widgets.VBox([widgets.HBox([self.figure], layout=widgets.Layout(justify_content='center')),
                           widgets.HBox([self.axis_change,self.button],layout=widgets.Layout(justify_content='center')),
                           widgets.HBox([self.output], layout=widgets.Layout(justify_content='center'))],
                           layout=widgets.Layout(margin='0px', paddin = '0px', justify_content='center', align_items ='center'))
        display(ui)
                
                
        

                