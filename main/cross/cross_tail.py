#!/usr/bin/env python
# -*- coding: utf-8 -*-

#@author  Bin Hong

import sys,os
import json
import time
import numpy as np
import pandas as pd
import multiprocessing
from sklearn.externals import joblib # to dump model
import cPickle as pkl
local_path = os.path.dirname(__file__)
root = os.path.join(local_path, '..')
sys.path.append(root)
sys.path.append(local_path)

import model.modeling as  model
from utils import time_me

def accu(df, label, threshold):
    if threshold > 0:
        df2 = df.sort_values("pred", ascending = False)[:threshold]
    else:
        df2 = df
    npPred = df2["pred"].values
    npLabel = df2[label].values
    npTrueInPos = npLabel[npLabel>1.0]
    res = {"rate":df2["pred"].values[-1], "pos": npLabel.size, "trueInPos":npTrueInPos.size}
    return res

def filter_(df):
    return df

cache = {}
@time_me
def get_df(f):
    if f in cache:
        return cache[f]
    df =  pd.read_pickle(f)
    cache[f] = df
    #with open(f, "rb") as ff:
    #    df = pkl.load(ff)
    #return joblib.load(f)
    #return pd.read_csv(f)
    return df

def get_range(df, start ,end):
    return df.query('date >="%s" & date <= "%s"' % (start, end)) 

@time_me
def one_work(cls, ta_dir, label, date_range, th):
    re =  "%s\t%s\t%s\t%s\t%s\t%f\t" % (cls, ta_dir[-4:], label, date_range[0], date_range[1],th)
    merged_file = os.path.join(ta_dir, "merged.pkl")
    df = filter_(get_df(merged_file))
    df = get_range(df, date_range[0], date_range[1])
    cls = joblib.load(os.path.join(root, 'data', 'models',"model_" + cls + ".pkl"))
    feat_names = model.get_feat_names(df)
    npFeat = df.loc[:,feat_names].values
    for i, npPred in enumerate(cls.staged_predict_proba(npFeat)):
        if i == 322:
            break
    #npPred = cls.predict_proba(npFeat)
    df["pred"] = npPred[:,1]
    dacc = accu(df, label, th)
    re += "%f\t%d\t%d\t" % (dacc["rate"],dacc["trueInPos"], dacc["pos"])
    if dacc["pos"] > 0:
        re += "%f" % (dacc["trueInPos"]*1.0 / dacc["pos"])
    else :
        re += "0.0"
    print re
    return re

def main(argv):
    pool_num = int(argv[1])
    conf_file = argv[2]
    impstr = "import %s as conf" % conf_file
    exec impstr
    out_file = os.path.join(root, 'data', "crosses", conf_file+".report")
    fout = open(out_file, 'w')


    pool = multiprocessing.Pool(processes=pool_num)
    result = []
    for each in conf.l_params:
        #one_work(*each)
        result.append(pool.apply_async(one_work, each ))
    #pool.close()
    #pool.join()
    for each in result:
        print >> fout, "%s" % each.get()
        print each , "done!"
    fout.close()

if __name__ == '__main__':
    main(sys.argv)
