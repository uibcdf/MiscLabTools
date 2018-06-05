from numpy import ndarray as ndarray
from pandas.core.frame import DataFrame as dataframe

scalars=[int,float,bool]

def Check(obj=None,as_str=True):

    type1=type(obj)
    type2=None
    type3=None
    supratype=type1.__name__

    if type1 in [list,tuple]:
        type2=type(obj[0])
        if type2 in [list,tuple,ndarray,dataframe]:
            supratype+=' of '+type2.__name__

    if type2 in [list,tuple]:
        type3=type(obj[0][0])
        if type3 in [list,tuple,ndarray,dataframe]:
            supratype+=' of '+type3.__name__

    if as_str:
        return supratype
    else:
        return type1, type2, type3
