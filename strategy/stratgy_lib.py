import numpy as np
import pandas as pd


def pct_up_down_relate(df1, df2):
    df1['close_pct'] = df1['close'].pct_change()
    df2['close_pct'] = df2['close'].pct_change()
    df1['close_pos_neg_a'] = np.where(df1['close_pct'] < 0, -1, np.where(df1['close_pct'] == 0, 0, 1))
    df2['close_pos_neg_b'] = np.where(df2['close_pct'] < 0, -1, np.where(df2['close_pct'] == 0, 0, 1))
    df1.dropna()
    df2.dropna()
    df1_n = df1['close_pos_neg_a']
    df2_n = df2['close_pos_neg_b']
    dfa = pd.concat([df1_n, df2_n], axis=1)
    dfa[['mul']] = dfa[['close_pos_neg_a']].multiply(dfa['close_pos_neg_b'], axis="index")
    dfa.dropna()
    pos_pct = len(dfa[(dfa['mul'] == 1)]) / len(dfa)
    neg_pct = len(dfa[(dfa['mul'] == -1)]) / len(dfa)
    zero_pct = len(dfa[(dfa['mul'] == 0)]) / len(dfa)
    return [pos_pct, neg_pct, zero_pct]


def shift_relate_pct(df1, df2, shift_range):
    df1 = df1.shift(shift_range)
    relate_list = pct_up_down_relate(df1, df2)
    # for
    return shift_range, relate_list

def relate_filter(shift_range,relate_list,threshold=0.55):
    dict_rel = {}
    for i in range(len(relate_list)):
        if relate_list[i] > threshold:
            if i == 0:
                dict_rel[range] = {"pos":relate_list[i]}
                return {shift_range: {"pos":relate_list[i]}}
            elif i ==1:
                dict_rel[range] = {"neg":relate_list[i]}
    return dict_rel


