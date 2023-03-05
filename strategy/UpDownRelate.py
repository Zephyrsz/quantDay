import pandas as pd
import numpy as np


d_baseDir = "/Users/roger.wei/app/qdata/jqdata/history_dir"


ofile = d_baseDir+ "/history_000001.XSHE.csv"
ofile1 = d_baseDir+ "/history_000006.XSHE.csv"

df = pd.read_csv(ofile,skiprows=1,delimiter=',',names=["date","open","close","high","low","volume","money"],
                 index_col='date',parse_dates=True)
df1 = pd.read_csv(ofile1,skiprows=1,delimiter=',',names=["date","open","close","high","low","volume","money"],
                 index_col='date',parse_dates=True)

df['close_pct'] = df['close'].pct_change()
df['close_pos_neg_a'] = np.where(df['close_pct']<0,-1,np.where(df['close_pct']==0,0,1))
# df.to_csv("001.csv")

df.dropna()
print("001################")
print(df[(df['close_pos_neg_a']==0)])
print("001s################")
df_n = df['close_pos_neg_a']


df1['close_pct'] = df1['close'].pct_change()
df1['close_pos_neg_b'] = np.where(df1['close_pct']<0,-1,np.where(df1['close_pct']==0,0,1))
# df1.to_csv("006.csv")
print("006################")
print(df1[(df1['close_pos_neg_b']==0)])
print("006################")

df1_n = df1['close_pos_neg_b']


dfa = pd.concat([df_n,df1_n],axis=1)

# print(dfa)

dfa[['mul']] = dfa[['close_pos_neg_a']].multiply(dfa['close_pos_neg_b'],axis="index")

dfa.dropna()

# print(dfa)
# print(dfa[['mul','close_pos_neg_a']])
pos_pct = len(dfa[(dfa['mul']==1)])/ len(dfa)
neg_pct = len(dfa[(dfa['mul']==-1)])/ len(dfa)
zero_pct = len(dfa[(dfa['mul']==0)])/ len(dfa)
# print(dfa['mul'].unique())
# print(dfa[(dfa['mul']==0)])
# print(pos_pct,neg_pct,zero_pct)
