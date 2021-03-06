#!/usr/bin/env python
# -*- coding: utf-8 -*-

#@author  Bin Hong

import sys,os
local_path = os.path.dirname(__file__)
root = os.path.join(local_path, '..')
sys.path.append(root)

import model.model_param_set as param_set

"""
## 研究目的
    研究模型在时间上的稳定性
## 结论
"""
ta =  param_set.d_dir_ta


l_params = [
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2010-01-01", '2010-12-31'),  0.0),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2010-01-01", '2010-12-31'),  0.5),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2010-01-01", '2010-12-31'),  0.6),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2010-01-01", '2010-12-31'),  0.65),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2010-01-01", '2010-12-31'),  0.7),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2010-01-01", '2010-12-31'),  0.75),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2010-01-01", '2010-12-31'),  0.8),

        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2011-01-01", '2011-12-31'),  0.0),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2011-01-01", '2011-12-31'),  0.5),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2011-01-01", '2011-12-31'),  0.6),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2011-01-01", '2011-12-31'),  0.65),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2011-01-01", '2011-12-31'),  0.7),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2011-01-01", '2011-12-31'),  0.75),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2011-01-01", '2011-12-31'),  0.8),

        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2012-01-01", '2012-12-31'),  0.0),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2012-01-01", '2012-12-31'),  0.5),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2012-01-01", '2012-12-31'),  0.6),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2012-01-01", '2012-12-31'),  0.65),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2012-01-01", '2012-12-31'),  0.7),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2012-01-01", '2012-12-31'),  0.75),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2012-01-01", '2012-12-31'),  0.8),

        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2013-01-01", '2013-12-31'),  0.0),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2013-01-01", '2013-12-31'),  0.5),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2013-01-01", '2013-12-31'),  0.6),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2013-01-01", '2013-12-31'),  0.65),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2013-01-01", '2013-12-31'),  0.7),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2013-01-01", '2013-12-31'),  0.75),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2013-01-01", '2013-12-31'),  0.8),

        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2014-01-01", '2014-12-31'),  0.0),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2014-01-01", '2014-12-31'),  0.5),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2014-01-01", '2014-12-31'),  0.6),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2014-01-01", '2014-12-31'),  0.65),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2014-01-01", '2014-12-31'),  0.7),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2014-01-01", '2014-12-31'),  0.75),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2014-01-01", '2014-12-31'),  0.8),

        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2015-01-01", '2015-12-31'),  0.0),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2015-01-01", '2015-12-31'),  0.5),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2015-01-01", '2015-12-31'),  0.6),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2015-01-01", '2015-12-31'),  0.65),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2015-01-01", '2015-12-31'),  0.7),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2015-01-01", '2015-12-31'),  0.75),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2015-01-01", '2015-12-31'),  0.8),

        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2016-01-01", '2016-12-31'),  0.0),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2016-01-01", '2016-12-31'),  0.5),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2016-01-01", '2016-12-31'),  0.6),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2016-01-01", '2016-12-31'),  0.65),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2016-01-01", '2016-12-31'),  0.7),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2016-01-01", '2016-12-31'),  0.75),
        ("taselect_GBCv1n1000md3lr001_l5_s2000e2009" , ta["taselect"], "label5", ("2016-01-01", '2016-12-31'),  0.8),

        ]

