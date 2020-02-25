import pandas as pd

def pandasDataFrame(filename=None):

    fff=open(filename,'r')
    lines_header=0
    title=""
    xaxis=""
    yaxis=""
    zaxis=""
    slabels=[]
    
    for line in fff.readlines():
        
        if line[0] == '#':
            lines_header+=1
        elif line[0] == '@':
            lines_header+=1
            if 'xaxis' in line:
                xaxis=line.split('"')[1]
            elif 'yaxis' in line:
                yaxis=line.split('"')[1]
            elif 'zaxis' in line:
                zaxis=line.split('"')[1]
            elif line.startswith("@ s"):
                slabels.append(line.split('"')[1])
            elif 'title' in line:
                title=line.split('"')[1]
        else:
            break

    fff.close()

    dataframe=pd.read_table(filename,skiprows=lines_header,header=None,delim_whitespace=True)
    dataframe.dropna(axis=1, how='all', inplace=True)

    # dataframe name:
    if title:
        dataframe.name=title
    # column names:
    if len(slabels)==dataframe.columns.size:
        dataframe.columns=slabels
    elif xaxis:
        if dataframe.columns.size == 2:
            dataframe.columns=[xaxis,yaxis]
        elif dataframe.columns.size == 3:
            dataframe.columns=[xaxis,yaxis,zaxis]

    return dataframe
