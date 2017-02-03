#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @author  Bin Hong

"""
"""

import sys
import os
import platform
import socket
import pandas as pd

import matplotlib
matplotlib.use('Agg')

local_path = os.path.dirname(__file__)
root = os.path.join(local_path, '..')
sys.path.append(root)

from main.base.score2 import ScoreLabel
from main.work import model
from main.work import build
#from main.work import pred
from main import base
from main.work.conf import MltradeConf
from main.ta import ta_set
from main.model.spliter import BinarySpliter
from main.classifier.tree import MyRandomForestClassifier
from main.classifier.tree import RFCv1n2000md6msl100
from main.classifier.tree import RFCv1n2000md6msl10000
from main.classifier.tree import MyGradientBoostingClassifier
from main.classifier.tree import MyLogisticRegressClassifier
from main.backtest import backtest


def getConf(week,
        index="sp100_snapshot_20091129",
        model_split=BinarySpliter("2010-01-01", "2017-01-01", "1700-01-01", "2010-01-01")
):
    #classifier = MyGradientBoostingClassifier(n_estimators = 100)
    classifier = RFCv1n2000md6msl100()
    index = index
    #classifier = MyLogisticRegressClassifier(C=1e3)
    ta = ta_set.TaSetBase1Ext4El()
    index = index
    week = week
    if base.is_test_flag():
        classifier = MyRandomForestClassifier(n_estimators=10, min_samples_leaf=10)
        index = "test"

    confer = MltradeConf(
                         model_split=model_split,
                         classifier=classifier,
                         score1=ScoreLabel(5, 1.0),
                         score2 = ScoreLabel(5, 1.0),
                         ta = ta, n_pool=30, index=index, week = week)

    return confer

def get_confs():
    for week in [1,2,3,4,5]:
        yield getConf(week, index = "sp100_snapshot_20091129", model_split=BinarySpliter("2010-01-01", "2013-01-01", "1980-01-01", "2010-01-01"))
        yield getConf(1, index = "sp100_snapshot_20120316", model_split=BinarySpliter("2013-01-01", "2015-01-01", "1983-01-01", "2013-01-01"))
        yield getConf(1, index = "sp100_snapshot_20140321", model_split=BinarySpliter("2015-01-01", "2017-01-01", "1985-01-01", "2015-01-01"))

#if __name__ == '__main__':
#    tobe = []
#    for confer in get_confs():
#        build.work(confer)
#        model.work(confer)
#        df1 = pd.read_pickle(confer.get_pred_file())
#        df1 = df1[(df1.date >=confer.model_split.test_start) & (df1.date<=confer.model_split.test_end)]
#        tobe.append(df1)
#    df = pd.concat(tobe)
#
#    df.to_pickle(os.path.join(root, 'output', "result.pkl"))
#    # backtest.run(os.path.join(root, "data", "cross", "pred%s.pkl" % base.last_trade_date()))

