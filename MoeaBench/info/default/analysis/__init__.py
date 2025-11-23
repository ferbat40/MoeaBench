from .objective import objective
from .variable import variable
from .hypervolume import hypervolume
from .GD import GD
from .GDplus import GDplus
from .IGD import IGD
from .IGDplus import IGDplus
from .plot_hypervolume import plot_hypervolume
from .plot_GD import plot_GD
from .plot_GDplus import plot_GDplus
from .plot_IGD import  plot_IGD
from .plot_IGDplus import plot_IGDplus
from .pareto import pareto
from .pareto_surface import pareto_surface


objective = objective()
variable = variable()
hypervolume = hypervolume()
GD = GD()
GDplus = GDplus()
IGD = IGD()
IGDplus = IGDplus()
plot_hypervolume = plot_hypervolume()
plot_GD = plot_GD()
plot_GDplus = plot_GDplus()
plot_IGD = plot_IGD()
plot_IGDplus = plot_IGDplus()
pareto = pareto()
pareto_surface = pareto_surface()


