class stat:
    
    def __init__(self, imports):
        print(imports.statistics," chegoy")

    @property
    def kstest(self):
        return self._kstest
    

    @kstest.setter
    def kstest(self,value):
        self._kstest=value()


    @property
    def indice(self):
        return self._indice
    

    @indice.setter
    def indice(self,value):
        self._indice=value()