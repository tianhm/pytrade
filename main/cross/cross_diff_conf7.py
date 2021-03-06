#!/usr/bin/env python
# -*- coding: utf-8 -*-

#@author  Bin Hong

import sys,os
local_path = os.path.dirname(__file__)
root = os.path.join(local_path, '..')
sys.path.append(root)

import model.model_param_set as param_set


ta =  param_set.d_dir_ta

l_params = [
        ("ta1_GBCv1n1000md3_l5_s2000e2009" , ta["ta3"], "label5", ("2010-01-01", '2015-12-31'),  0.0),
        ("ta1_GBCv1n1000md3_l5_s2000e2009" , ta["ta3"], "label5", ("2010-01-01", '2015-12-31'),  0.6),
        ("ta1_GBCv1n1000md3_l5_s2000e2009" , ta["ta3"], "label5", ("2010-01-01", '2015-12-31'),  0.7),
        ("ta1_GBCv1n1000md3_l5_s2000e2009" , ta["ta3"], "label5", ("2010-01-01", '2015-12-31'),  0.8),

        ("ta3_GBCv1n1000md3_l5_s2000e2009" , ta["ta3"], "label5", ("2010-01-01", '2015-12-31'),  0.0),
        ("ta3_GBCv1n1000md3_l5_s2000e2009" , ta["ta3"], "label5", ("2010-01-01", '2015-12-31'),  0.7),
        ("ta3_GBCv1n1000md3_l5_s2000e2009" , ta["ta3"], "label5", ("2010-01-01", '2015-12-31'),  0.8),
        ("ta3_GBCv1n1000md3_l5_s2000e2009" , ta["ta3"], "label5", ("2010-01-01", '2015-12-31'),  0.9),
        ("ta3_GBCv1n1000md3_l5_s2000e2009" , ta["ta3"], "label5", ("2010-01-01", '2015-12-31'),  0.95),

        ]

