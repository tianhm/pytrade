#!/usr/bin/env python
# -*- coding: utf-8 -*-

#@author  Bin Hong

import sys,os
import time
import numpy as np
import pandas as pd
from sklearn.externals import joblib # to dump model
import cPickle as pkl
local_path = os.path.dirname(__file__)
root = os.path.join(local_path, '..', '..')
sys.path.append(root)

import main.model.modeling as  model
import main.base as base
from utils import time_me

def get_all_from(path):
    sym2df = {}
    for each in base.get_file_list(path,ext=".pkl"):
        symbol = model.get_stock_from_path(each)
        df = pd.read_pickle(each)
        df["sym"] = symbol
        sym2df[symbol] = df 
    return sym2df


def merge(sym2feats):
    dfMerged = None
    toAppends = []
    for sym in sym2feats.keys():
        df = sym2feats[sym]
        if dfMerged is None:
            dfMerged = df
        else:
            toAppends.append(df)
    # batch merge speeds up!
    dfMerged =  dfMerged.append(toAppends)
    return dfMerged

@time_me
def get_merged_with_na(ta):
    sym2ta = get_all_from(os.path.join(root, 'data', 'ta', ta))
    df = merge(sym2ta)
    df = df[df['ta_NATR_14']>1.0]
    return df

@time_me
def get_merged(ta):
    df = get_merged(ta)
    df = df.replace([np.inf,-np.inf],np.nan)\
        .dropna()
    return df


