from .factory import moeabench


from typing import TYPE_CHECKING

if TYPE_CHECKING: from .MOEA import NSGA_III, RVEA, SPEA_II, MOEAD, U_NSGA_III
if TYPE_CHECKING: from .benchmark import DTLZ1,DTLZ2,DTLZ3,DTLZ4,DTLZ5,DTLZ6,DTLZ7,DTLZ8,DTLZ9,DPF1,DPF2,DPF3,DPF4,DPF5,E_problems,problems,I_problems
if TYPE_CHECKING: from .benchmark.problem_benchmark import P_DTLZ1,P_DTLZ2,P_DTLZ3,P_DTLZ4,P_DTLZ5,P_DTLZ6,P_DTLZ7,P_DTLZ8,P_DTLZ9,P_DPF1,P_DPF2,P_DPF3,P_DPF4,P_DPF5
if TYPE_CHECKING: from .benchmark.problem_benchmark.kernel_benchmark import  K_DTLZ1,K_DTLZ2,K_DTLZ3,K_DTLZ4,K_DTLZ5,K_DTLZ6,K_DTLZ7,K_DTLZ8,K_DTLZ9,K_DPF1,K_DPF2,K_DPF3,K_DPF4,K_DPF5
if TYPE_CHECKING: from .H_DPF import H_DPF
if TYPE_CHECKING: from .H_DTLZ import H_DTLZ
if TYPE_CHECKING: from .CACHE import CACHE
if TYPE_CHECKING: from .CACHE_bk_user import CACHE_bk_user