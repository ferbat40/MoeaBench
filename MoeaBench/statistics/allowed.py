import numpy as np


class allowed:

    def allowed_array(self,args):
        results = [True if (isinstance(i,list)) and (isinstance(i[-1],np.ndarray)) else False for i in args ]
        if False in results:
            raise ValueError("Only arrays are allowed for the metric calculation.")
        return results