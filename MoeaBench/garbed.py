from ANALYSE_tool import ANALYSE_tool
import numpy as np
from scipy.interpolate import griddata
import plotly.graph_objects as go
from IPython.display import  display, Javascript
import json


class PLOT_PFSURFACE(ANALYSE_tool):


    def parameters(self,BENCH,DATA):     
       try:
         if not 0 < len(self.LIST()) < 6:
              raise ValueError(f'Allowed only between one and five matrices ({len(self.LIST())} matrices found)')
         colors = ['Inferno','Turbo','Ice','Viridis','Cividis']
         self.parameter=[{"F" :value.get_arr_DATA(), "colorscale" : colors[index], "opacity" : 0.9, "showscale" : False, "showlegend" : True} for index, value in enumerate(DATA, start = 0)]
         self.BCH_title = f'3D Surface Chart'  
         self.list_choice=[[('',None)]+[(f'Objective {b+1}', b) for b in range(0,i.get_M())] for i in BENCH] 
         self.list_axis = np.array([[0,1,2] if i > 0 else [None,None,None] for i in range(0,len(BENCH)+1)])
         self.choice.options=[('', None)]+[(f'ITEM {index+1} - {bnk.get_BENCH()} (M = {bnk.get_M()}, K = {bnk.get_K()}, N = {bnk.get_Nvar()}, D = {bnk.get_D()}) for {dt.get_description()} (GEN = {dt.get_generations()} POP = {dt.get_population()})',index)  if int(dt.get_generations())+int(dt.get_population())>0 else (f'ITEM {index+1} - {bnk.get_BENCH()} (M = {bnk.get_M()}, K = {bnk.get_K()}, N = {bnk.get_Nvar()}, D = {bnk.get_D()}) ({dt.get_description()})',index) for index,(bnk,dt)  in enumerate( zip(BENCH,DATA), start = 0)]
         self.choice.value = 0
         self.configure(0)
       except Exception as e:
          self.reset(self.figure)
          msg = json.dumps(str(e))
          display(Javascript(f'alert({msg})'))


    def Z_axis(self,points,values,X,Y):
        try:
            z_linear = griddata(points=points,values=values, xi = (X,Y), method='linear')
            if not np.isnan(z_linear).any():
                return z_linear
        except Exception as e:
            pass
        try:
            z_nearest = griddata(points=points,values=values, xi = (X,Y), method='nearest')
            z_linear = griddata(points=points,values=values, xi = (X,Y), method='linear')
            return np.where(np.isnan(z_linear),z_nearest,z_linear)
        except Exception as e:
            pass
        try:
            return griddata(points=points,values=values, xi = (X,Y), method='nearest')
        except Exception as e:
            raise RuntimeError("No valid Z-axis value found") from e


    def surface(self,F=[],colorscale='Viridis',opacity=0.7,showscale=True, showlegend=True,label=[],x_axis=[],y_axis=[],z_axis=[]):
        xi = np.linspace(F[:,x_axis].min(),F[:,x_axis].max(),40)
        yi = np.linspace(F[:,y_axis].min(),F[:,y_axis].max(),40)
        X,Y = np.meshgrid(xi,yi)
        points=F[:,[x_axis,y_axis]]
        values=F[:,z_axis]
        Z = self.Z_axis(points,values,X,Y)
        return go.Surface(
            x=X,y=Y,z=Z,
            colorscale=colorscale,
            opacity=opacity,
            showscale=showscale,
            showlegend=showlegend,
            name=label,
            hovertemplate=(
                f"{str(label).split('(')[0]}<br>"
                f"{x_axis+1}: %{{x}}<br>"
                f"{y_axis+1}: %{{y}}<br>"
                f"{z_axis+1}: %{{z}}<br><extra></extra>"
                )
                )


    def configure(self,b):
      try:
        if not 0 < len(self.LIST()) < 6:
              raise ValueError(f'Allowed only between one and five matrices ({len(self.LIST())} matrices found)')
        self.figure.data=()
        with self.output:
            self.output.clear_output()  
        surfaces = [self.surface(
            F=pr['F'],
            colorscale=pr['colorscale'],
            opacity=pr['opacity'],
            showscale=pr['showscale'],
            showlegend=pr['showlegend'],
            label=f'Item {index}',
            x_axis=ax[0],
            y_axis=ax[1],
            z_axis=ax[2])
            for index,(ax, pr) in enumerate(zip(self.list_axis[1:],self.parameter), start = 1)]
        self.figure.add_traces(surfaces)
        self.figure.update_layout(
                scene = dict(
                    xaxis=dict(title=self.x_axis.value, showbackground=True, backgroundcolor="aliceblue", showgrid=True, gridcolor="#C3BDBD"),
                    yaxis=dict(title=self.y_axis.value, showbackground=True, backgroundcolor="aliceblue", showgrid=True, gridcolor="#C3BDBD"),
                    zaxis=dict(title=self.z_axis.value, showbackground=True, backgroundcolor="aliceblue", showgrid=True, gridcolor="#C3BDBD"),
                    aspectmode='manual',
                    aspectratio=dict(x=1,y=1,z=1)
                 ),
                 
                 width=900,
                 height=800,
                 margin=dict(l=0,r=0,b=0,t=0),
                 title=dict(
                     text=self.BCH_title,
                     x=0.5,
                     xanchor='center',
                     y=0.9,
                     yanchor='top',
                     pad=dict(t=0),
                     font=dict(size=16, weight='bold')
                 ),
                 legend=dict(
                     x=1,
                     y=0.5,
                     xanchor='right',
                     yanchor='middle'
               )
                )
      except Exception as e:
          self.reset(self.figure)
          msg = json.dumps(str(e))
          display(Javascript(f'alert({msg})'))