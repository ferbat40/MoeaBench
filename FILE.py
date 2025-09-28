
from FILE_reference import FILE_reference



class FILE(FILE_reference):

    def __init__(self,CACHE,**kwargs):
        self.__CACHE=CACHE
        super().__init__(**kwargs)


    
        #self.CREATE(DT_CONF,BENCH)


    