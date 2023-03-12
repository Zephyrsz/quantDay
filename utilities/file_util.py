import pandas as pd

'''
data 
df = pd.read_csv(ofile,skiprows=1,delimiter=',',names=["date","open","close","high","low","volume","money"],
                 index_col='date',parse_dates=True)
'''


def dataReader(data):
    dfile = data.datauri
    col_list = data.column_list
    df = pd.read_csv(dfile, skiprows=1, delimiter=',',
                     names=col_list,
                     index_col='date', parse_dates=True)
    return df


