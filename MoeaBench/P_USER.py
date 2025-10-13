from .P_DTLZ1 import P_DTLZ1

class P_USER(P_DTLZ1):

    def __init__(self, M, N, P, CACHE):
        self.CACHE=CACHE
        self.N=N
        self.M = M
        self.P = P