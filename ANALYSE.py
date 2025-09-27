from METRIC import METRIC
from E_METRIC import E_METRIC
from plot_3D_solutions import plot_3D_solutions
from plot_2D_HV import plot_2D_HV
from plot_2D_GD import plot_2D_GD
from plot_2D_GDplus import plot_2D_GDplus
from plot_2D_IGD import plot_2D_IGD
from plot_2D_IGDplus import plot_2D_IGDplus


from plot_3D_surface import plot_3D_surface
from I_ANALYSE import I_ANALYSE
from ENGINE import ENGINE



class ANALYSE(I_ANALYSE):
    """  
    - Instância:    
      analyse = ANALYSE(engine)  
    - ANALYSE esta dividida em 5 partes:
      - Parte 2: Plotagem 3D para pontos.
              - analyse.PLOT()
      - Parte 3: Plotagem 3D para superfície.
              - analyse.PLOT_SURFACE()
      - Parte 4: Plotagem 2D para métricas durante gerações.
              - analyse.PLOT_GEN()
      - Parte 5: Relatório de métricas finais.
              - analyse.PLOT_GEN()
    """   
    
    def __init__(self):    
        engine=ENGINE()    
        self.__METRIC=METRIC(ENGINE=engine,metodhs=list(E_METRIC))
        self.__plot_3D_solutions=plot_3D_solutions(ENGINE=engine)
        self.__plot_2D_HV=plot_2D_HV(ENGINE=ENGINE())
        self.__plot_2D_GD=plot_2D_GD(ENGINE=ENGINE())
        self.__plot_2D_GDplus=plot_2D_GDplus(ENGINE=ENGINE())
        self.__plot_2D_IGD=plot_2D_IGD(ENGINE=ENGINE())
        self.__plot_2D_IGDplus=plot_2D_IGDplus(ENGINE=ENGINE())
        self.__plot_3D_surface=plot_3D_surface(ENGINE=engine)
    

    def METRIC(self):
        return self.__METRIC.PLT()
    

    def plot_3D_solutions(self):
        return self.__plot_3D_solutions.PLT()
    

    def plot_2D_HV(self):
        return self.__plot_2D_HV.HV()
    

    def plot_2D_GD(self):
        return self.__plot_2D_GD.GD()
    

    def plot_2D_GDplus(self):
        return self.__plot_2D_GDplus.GDplus()
    

    def plot_2D_IGD(self):
        return self.__plot_2D_IGD.IGD()


    def plot_2D_IGDplus(self):
        return self.__plot_2D_IGDplus.IGDplus()


    def plot_3D_surface(self):
        return self.__plot_3D_surface.PLT()
    

    


    



    
    

    


    