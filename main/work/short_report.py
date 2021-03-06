
# -*- coding: utf-8 -*-
# @author  Bin Hong

import sys
import os
import pandas as pd


local_path = os.path.dirname(__file__)
root = os.path.join(local_path, '..', "..")
sys.path.append(root)

from main.model import ana

def work(confer, f=sys.stdout):
    test_type = 'short'
    dfo = pd.read_pickle(confer.get_pred_file())
    df = dfo[(dfo.date >=confer.model_split.test_start)]
    print(ana.roc_auc(df, confer), file=f)
    #print(ana.roc_auc_per_year(df, confer))
    #print(ana.count_level(df, confer.scores[1]))
    print(ana.accurate_level(df, confer.scores[0], type= test_type),file=f)
    res = ana.roi_level(df, confer.scores[1], type= test_type)
    print(res, file=f)
    #print(ana.roi_level(df, confer.scores[2]),file=f)
    thresholds = res['threshold'].tolist()
    print(ana.roi_level_per_year(df, confer.scores[1], thresholds[0], thresholds[1], type=test_type),file=f)
    print(ana.roi_last_months(df, confer.scores[1], thresholds[0], thresholds[1], type=test_type),file=f)
    #print(ana.roi_level_per_year(df, confer.scores[2]))