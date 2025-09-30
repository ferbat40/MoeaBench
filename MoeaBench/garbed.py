from PLOT_PFGEN import PLOT_PFGEN
import numpy as np
import ipywidgets as widgets
from  pathlib import Path


class PLOT_GEN(PLOT_PFGEN):
     
     def __init__(self,ENGINE,metric): 
       self.ENGINE=ENGINE
       self.metric=metric
       self.next= widgets.Button(description = '\u23E9', layout = widgets.Layout(width='40px',margin='0', padding ='0'))
       self.prev= widgets.Button(description = '\u23EA', layout = widgets.Layout(width='40px',margin='0', padding ='0'))
       self.next.on_click(self.ADDICT)
       self.prev.on_click(self.REMOVE)
       self.btns = widgets.VBox([self.next,self.prev], layout = widgets.Layout(margin='90px 0 0 0', padding ='0'))    
       super().__init__(ENGINE=ENGINE,metric=metric)
       

     def download_FILE(self):
        self.ENGINE.ENGINE_lite().get_AFILE()
        files=[P_file.name for P_file in Path("analysis").iterdir()  
                if int(self.ENGINE.STR_param(f'analysis/{P_file.name}')[2]) > 0 and P_file.suffix=='.xlsx']
        for item in files:
            if item not in self.ENGINE.ENGINE_lite().get_AFILE(): 
                self.ENGINE.ENGINE_lite().get_AFILE().append(item)
                self.ENGINE.ENGINE_lite().FILE_add(f'analysis/{item}',self.metric[0])
       

     def DATA(self,BENCH,DATA):
        axis_DATA=[]
        pop = [np.array(i.get_METRIC_gen().get_arr_Metric_gen()[1]).flatten() for i in DATA]
        metric = [np.array(i.get_METRIC_gen().get_arr_Metric_gen()[0]).flatten() for i in DATA]
        label = [f'{dt.get_description()}     (GEN={dt.get_generations()},POP={dt.get_population()})     (M={bk.get_M()},K={bk.get_K()},N={bk.get_Nvar()},D={bk.get_D()})' if int(dt.get_generations())+int(dt.get_population())>0 
                 else f'{dt.get_description()}' for dt,bk in zip(DATA,BENCH)]
        title=f'for {BENCH[0].get_BENCH()}'
        for x,y in zip(pop,metric):
           axis_DATA.append([x,y])
        return [pop,metric],label,title
     




     from IPython.display import display, Javascript
from ANALYSE_tool import ANALYSE_tool
import ipywidgets as widgets
import plotly.graph_objects as go
import numpy as np
import json
try:
    import google.colab
    from google.colab import output
    output.enable_custom_widget_manager()
except ImportError:
    pass

class PLOT_PFGEN(ANALYSE_tool):
     
     def __init__(self,ENGINE,metric):
        self.metric=metric
        super().__init__(ENGINE=ENGINE)
        

     def parameters(self,BENCH,DATA):
         mtc = [i for i in self.metric if i != 'Evaluations']
         mtc.append('Evaluations')
         self.metric=mtc
         self.markers,self.label,self.title=self.DATA(BENCH,DATA)
         self.colors = ['red', 'blue', 'green','orange','purple','black','brown','yellow','cyan','gray']
         self.change_axis({'new' : mtc[0]})
         self.axis_change.value = mtc[0]
         self.configure(0)
             

     def reset(self,fig):
        fig.data=[]
        fig.layout.title=None
        self.markers=[]
        self.axis_DATA=[]
        fig.add_trace(
        go.Scatter(x=[0],y=[0],
        mode='lines+markers',
        marker=dict(size=0),
        showlegend=False           
        )
        )
        return fig
     

     def change_axis(self, b):
       try:
         if not 0 < len(self.LIST()) < 11:
              raise ValueError(f'Allowed only between one and five matrices ({len(self.LIST())} matrices found)')       
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
        msg = json.dumps(str(e))
        display(Javascript(f'alert({msg})')) 
     
     
     #3d gen
     def ADDICT(self,b):
        try:
            if not 0 < len(self.LIST_alread()) < 11:
                raise ValueError(f'Allowed only between one and ten matrices ({len(self.LIST_alread())} matrices found)')
            for obj1,obj2 in self.ALREAD.value:
                self.SELECT.options = list(self.SELECT.options)+[(self.ROTULE(obj1,obj2) , (obj1,obj2))]
            refactor = [item for item in self.ALREAD.options if item[1] not in self.ALREAD.value]
            self.ALREAD.options=refactor
            self.ALREAD.value=()
            BENCH = [self.ENGINE.memory().BENCH_conf_recursive(OBJ) for OBJ in self.LIST()]
            DATA =  [self.ENGINE.memory().DATA_conf_recursive(OBJ) for OBJ in self.LIST()]
            self.parameters(BENCH,DATA)   
        except Exception as e:
            msg = json.dumps(str(e))
            display(Javascript(f'alert({msg})'))
       

     def configure(self,b):
       try:
        if not 0 < len(self.LIST()) < 11:
              raise ValueError(f'Allowed only between one and five matrices ({len(self.LIST())} matrices found)')   
        with self.output:
             self.output.clear_output()  
             vet_pts=[i for i in self.axis_DATA]
             self.figure.data=()
             colors = ['red', 'blue', 'green','orange','purple','black','brown','yellow','cyan','gray']
             for pts, cl, lbl in zip( vet_pts, colors, self.label ):
                 pts=np.array(pts)
                 self.figure.add_trace(go.Scatter(
                     x = pts[0], y = pts[1],
                     mode='lines+markers',
                     marker=dict(size=3, color=cl),
                     name=f'{lbl.split("     ")[0]}<br>{lbl.split("     ")[1]}<br>{lbl.split("     ")[2]}<br>',
                     showlegend=True,
                     hovertemplate = (f"{str(lbl).split('(')[0]}<br>"
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
        self.reset(self.figure)
        msg = json.dumps(str(e))
        display(Javascript(f'alert({msg})'))
  
        
     def PLT(self):  
        iterate=self.CHOICE()
        self.axis_change = widgets.Dropdown(options=[('',None),(self.metric[1],self.metric[1]),(self.metric[0],self.metric[0])] , description="<span style='font-size:14px; color:blue; font-weight:bold;'>AXIS X</span>")
        self.output=widgets.Output()
        self.figure=go.FigureWidget()
        self.figure.data=()
        self.button = widgets.Button(description="PLOT", style = widgets.ButtonStyle(button_color='deepskyblue', font_weight='bold'))
        self.axis_change.observe(self.change_axis, names = 'value')
        self.button.on_click(self.configure) 
        ui = widgets.VBox([widgets.HBox([iterate], layout=widgets.Layout(justify_content='center')),
                           widgets.HBox([self.figure], layout=widgets.Layout(justify_content='center')),
                           widgets.HBox([self.axis_change,self.button],layout=widgets.Layout(justify_content='center')),
                           widgets.HBox([self.output], layout=widgets.Layout(justify_content='center'))],
                           layout=widgets.Layout(margin='0px', paddin = '0px', justify_content='center', align_items ='center'))
        display(ui)