import numpy as np

def Float2Str(lista,decimals=6):
    olista=[]
    for ii in lista:
        if type(ii) in [float,np.float64]:
            olista.append(np.str(np.around(ii,decimals)))
        else:
            olista.append(ii)
    return olista

