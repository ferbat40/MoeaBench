from .IPL_MoeaBench import IPL_MoeaBench
import ipywidgets as widgets
from IPython.display import  display


class analyse(IPL_MoeaBench):
    
    def PLT(self):  
         out = widgets.Output()
         with out:
             display(self.figure)
         self.ui = widgets.VBox([widgets.HBox([out], layout=widgets.Layout(justify_content='center')),
                             ])
         display(self.ui)
