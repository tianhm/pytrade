#!/usr/bin/env python
# -*- coding: utf-8 -*-

#@author  Bin Hong

import sys,os
import numpy as np
local_path = os.path.dirname(__file__)
root = os.path.join(local_path, '..')
sys.path.append(root)
sys.path.append(local_path)

import model.modeling as  model
import model.model_param_set as model_params

def main(argv):
    for ta in model_params.d_dir_ta:
        sym2ta = model.get_all_from(model_params.d_dir_ta[ta])
        df = model.merge(sym2ta, '1900-01-01', '2099-01-01')
        print df.shape
        df = df.replace([np.inf,-np.inf],np.nan)\
            .dropna()
        print df.shape
        df.to_csv(os.path.join(model_params.d_dir_ta[ta], "merge", "merged.csv"))
if __name__ == '__main__':
    main(sys.argv)


