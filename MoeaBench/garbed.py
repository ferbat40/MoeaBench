from ANALYSE_tool import ANALYSE_tool
import plotly.graph_objects as go
from IPython.display import  display, Javascript
import json


class PLOT_PF(ANALYSE_tool):         

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
       

     #3d solutions
     def ADDICT(self,b):
        try:
            if (not 0 < len(self.LIST_alread()) < 11) or (not 0 < len(self.LIST_alread())+len(self.LIST()) < 11):
                raise ValueError(f'Allowed only between one and ten matrices ({len(self.LIST_alread())} matrices found)' )
            self.ENGINE.memory().allowed_DATA(self.ALREAD.value)
            for obj1,obj2 in self.ALREAD.value:
                self.SELECT.options = list(self.SELECT.options)+[(self.ROTULE(obj1,obj2) , (obj1,obj2))]
            refactor = [item for item in self.ALREAD.options if item[1] not in self.ALREAD.value]
            self.ALREAD.options=refactor
            self.ALREAD.value=()
            BENCH = [self.ENGINE.memory().BENCH_conf_recursive(OBJ) for OBJ in self.LIST()]
            DATA =  [self.ENGINE.memory().DATA_conf_recursive(OBJ) for OBJ in self.LIST()]
            self.parameters([dt.get_arr_DATA() for dt in DATA],BENCH,DATA)   
        except Exception as e:
            msg = json.dumps(str(e))
            display(Javascript(f'alert({msg})'))

     
     #3d solutions
     def REMOVE(self,b):
        for obj1,obj2 in  self.SELECT.value:
            self.ALREAD.options = list(self.ALREAD.options)+[(self.ROTULE(obj1,obj2) , (obj1,obj2))]
        refactor = [item for item in self.SELECT.options if item[1] not in self.SELECT.value]
        self.SELECT.options=refactor
        self.SELECT.value=()
        BENCH = [self.ENGINE.memory().BENCH_conf_recursive(OBJ) for OBJ in self.LIST()]
        DATA =  [self.ENGINE.memory().DATA_conf_recursive(OBJ) for OBJ in self.LIST()]
        if DATA != []:
            self.parameters([dt.get_arr_DATA() for dt in DATA],BENCH,DATA)   
        else:
            self.reset(self.figure)



    from I_ANALYSE_tool import I_ANALYSE_tool
from ITERATE import ITERATE
import plotly.graph_objects as go
import ipywidgets as widgets
from IPython.display import display, Javascript
from  pathlib import Path
import json
import numpy as np
try:
    import google.colab
    from google.colab import output
    output.enable_custom_widget_manager()
except ImportError:
    pass


class ANALYSE_tool(I_ANALYSE_tool,ITERATE):
        
     def __init__(self,ENGINE,**kwargs): 
        self.next= widgets.Button(description = "SELECT", style = widgets.ButtonStyle(button_color='mediumspringgreen', font_weight='bold'))
        self.prev= widgets.Button(description = "DESELECT", style = widgets.ButtonStyle(button_color='lightcoral', font_weight='bold'))
        self.next.on_click(self.ADDICT)
        self.prev.on_click(self.REMOVE)
        self.btns = widgets.VBox([self.next,self.prev], layout = widgets.Layout(margin='47px 15px 0 15px', padding ='0'))
        self.ENGINE=ENGINE
        super().__init__(ENGINE=ENGINE,    
                         **kwargs)
                         
        
     def download_FILE(self):
        self.ENGINE.ENGINE_full().get_AFILE()
        files=[P_file.name for P_file in Path("analysis").iterdir()  
                if int(self.ENGINE.STR_param(f'analysis/{P_file.name}')[2]) > 0 and P_file.suffix=='.xlsx']
        for item in files:
            if item not in self.ENGINE.ENGINE_full().get_AFILE(): 
                self.ENGINE.ENGINE_full().get_AFILE().append(item)
                self.ENGINE.ENGINE_full().FILE_add(f'analysis/{item}')
       

     def allowed(self,element,data, obj = ('get_M','get_K','get_D','get_BENCH')):
        list_valid = list(map(lambda o: [o.get_M(),o.get_K(),o.get_D(),o.get_BENCH()], filter(lambda o: all(hasattr(o,m) for m in obj), element)))
        if not all(np.array_equal(data,arr) for arr in list_valid):
            raise ValueError (f'All selected parameters must be equals')   
        

     def reset(self,fig):
        BENCH = [self.ENGINE.memory().BENCH_conf_recursive(OBJ) for OBJ in self.LIST()]
        self.choice.options=[]
        self.x_axis.options=[]
        self.y_axis.options=[]
        self.z_axis.options=[]
        self.list_axis = np.array([[0,1,2] if i > 0 else [None,None,None] for i in range(0,len(BENCH)+1)])
        fig.data=[]
        fig.layout.title=None
        fig.add_trace(
        go.Scatter3d(x=[0],y=[0],z=[0],
        mode='markers',
        marker=dict(size=0),
        showlegend=False           
        )
        )
        fig.layout.scene.aspectmode='auto'
        return fig    
        

     def axis_x(self, change):
          with self.output:
                self.output.clear_output()  
                new=change['new']       
                try:
                    index = [value for key,value in self.x_axis.options].index(new)
                    select = [value for key,value in self.choice.options].index(self.choice.value)
                    if index > 0:
                        self.list_axis[select][0]=index-1
                        self.configure(0)
                except Exception as e:
                    pass


     def axis_y(self, change):
          with self.output:
             self.output.clear_output()  
             new=change['new']
             try:
                 index = [value for key,value in self.y_axis.options].index(new)
                 select = [value for key,value in self.choice.options].index(self.choice.value)
                 if index > 0:
                     self.list_axis[select][1]=index-1
                     self.configure(0)
             except Exception as e:
                 pass


     def axis_z(self, change):
          with self.output:
             self.output.clear_output()  
             new=change['new']
             try:
                 index = [value for key,value in self.z_axis.options].index(new)
                 select = [value for key,value in self.choice.options].index(self.choice.value)
                 if index > 0:
                     self.list_axis[select][2]=index-1
                     self.configure(0)
             except Exception as e:
                 pass


     def axis_configure(self, change):
         with self.output:
            self.output.clear_output()  
            new=change['new']
            try:
                index = [value for key,value in self.choice.options].index(new)
                self.x_axis.options=self.list_choice[index-1]
                self.y_axis.options=self.list_choice[index-1]
                self.z_axis.options=self.list_choice[index-1]
                self.x_axis.value= self.list_axis[index][0]
                self.y_axis.value= self.list_axis[index][1]
                self.z_axis.value= self.list_axis[index][2]
            except Exception as e:
                pass

self.parameters([dt.get_arr_DATA() for dt in DATA],BENCH,DATA) 
     def parameters(self,vet_pt,BENCH,DATA):
         self.BENCH=BENCH
         self.DATA=DATA
         self.vet_pts=[ (i - np.min(i,axis = 0)) / (np.max(i,axis = 0)-np.min(i,axis = 0))   for i in vet_pt]  
         self.list_choice=[[('',None)]+[(f'Objective {b+1}', b) for b in range(0,i.get_M())] for i in BENCH] 
         self.list_axis = np.array([[0,1,2] if i > 0 else [None,None,None] for i in range(0,len(BENCH)+1)])
         self.choice.options=[('', None)]+[(f'ITEM {index+1} - {bnk.get_BENCH()} (M = {bnk.get_M()}, K = {bnk.get_K()}, N = {bnk.get_Nvar()}, D = {bnk.get_D()}) for {dt.get_description()} (GEN = {dt.get_generations()} POP = {dt.get_population()})',index)  if int(dt.get_generations())+int(dt.get_population())>0 else (f'ITEM {index+1} - {bnk.get_BENCH()} (M = {bnk.get_M()}, K = {bnk.get_K()}, N = {bnk.get_Nvar()}, D = {bnk.get_D()}) ({dt.get_description()})',index) for index,(bnk,dt)  in enumerate( zip(BENCH,DATA), start = 0)]
         self.choice.value = 0
         self.configure(0)


     #3D surface
     def ADDICT(self,b):
        try:
            if not 0 < len(self.LIST_alread()) < 6:
              raise ValueError(f'Allowed only between one and five matrices ({len(self.LIST_alread())} matrices found)')
            self.ENGINE.memory().allowed_DATA(self.ALREAD.value)
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

     
     #3D surface
     def REMOVE(self,b):
        for obj1,obj2 in  self.SELECT.value:
            self.ALREAD.options = list(self.ALREAD.options)+[(self.ROTULE(obj1,obj2) , (obj1,obj2))]
        refactor = [item for item in self.SELECT.options if item[1] not in self.SELECT.value]
        self.SELECT.options=refactor
        self.SELECT.value=()
        BENCH = [self.ENGINE.memory().BENCH_conf_recursive(OBJ) for OBJ in self.LIST()]
        DATA =  [self.ENGINE.memory().DATA_conf_recursive(OBJ) for OBJ in self.LIST()]
        if DATA != []:
            self.parameters(BENCH,DATA)   
        else:
            self.reset(self.figure)


     def PLT(self):  
         iterate=self.CHOICE()
         self.x_axis = widgets.Dropdown(layout = widgets.Layout(width='120px' ,margin='0px 25px 0 10px', padding ='0'))
         label_x = widgets.HTML("<span style='font-size:14px; color:blue; font-weight:bold;'>X</span>")
         self.y_axis = widgets.Dropdown(layout = widgets.Layout(width='120px' ,margin='0px 25px 0 10px', padding ='0'))
         label_y = widgets.HTML("<span style='font-size:14px; color:blue; font-weight:bold;'>Y</span>")  
         self.z_axis = widgets.Dropdown(layout = widgets.Layout(width='120px' ,margin='0px 25px 0 10px', padding ='0'))
         label_z = widgets.HTML("<span style='font-size:14px; color:blue; font-weight:bold;'>Z</span>")     
         self.choice = widgets.Dropdown(options=[],layout = widgets.Layout(width='500px' ,margin='0px 25px 0 10px', padding ='0')) 
         label_choice = widgets.HTML("<span style='font-size:14px; color:blue; font-weight:bold;'>CONFIGURE</span>")
         self.choice.observe(self.axis_configure, names = 'value')
         self.x_axis.observe(self.axis_x, names = 'value')  
         self.y_axis.observe(self.axis_y, names = 'value')
         self.z_axis.observe(self.axis_z, names = 'value')  
         self.output=widgets.Output()
         self.figure=go.FigureWidget()
         self.figure.data=()
         self.ui = widgets.VBox([widgets.HBox([iterate], layout=widgets.Layout(justify_content='center')),
                            widgets.HBox([self.figure], layout=widgets.Layout(justify_content='center')),
                            widgets.HBox([label_choice,self.choice,label_x,self.x_axis,label_y,self.y_axis,label_z,self.z_axis],layout=widgets.Layout(justify_content='center')),
                            widgets.HBox([self.output], layout=widgets.Layout(justify_content='center'))
                            ],
                            layout=widgets.Layout(margin='0px', paddin = '0px'))
         display(self.ui)