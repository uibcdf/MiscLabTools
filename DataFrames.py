import pandas as pd
from numpy import concatenate

def InfoList(dfs):

    list_lengths=[df.shape[0] for df in dfs]
    print(len(dfs), 'DataFrames with a total length:', sum(list_lengths))
    print([column for column in dfs[0]])
    for df in dfs:
        print(df.name, df.shape[0]) 


def LoadCSV(file_path=None):
    
    df=pd.read_csv(file_path)
    df.name=file_path
    return df

def GetColFromList(dataframe_list,column):

    return concatenate([df[column].values for df in dataframe_list])



