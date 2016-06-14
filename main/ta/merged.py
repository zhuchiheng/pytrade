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
root = os.path.join(local_path, '..')
sys.path.append(root)
sys.path.append(local_path)
import model.modeling as  model
from utils import time_me

def get_all_from(path):
    sym2df = {}
    for each in model.get_file_list(path):
        symbol = model.get_stock_from_path(each)
        df = pd.read_csv(each, parse_dates=True)
        df["sym"] = symbol
        sym2df[symbol] = df 
    print len(sym2df)
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
def save(df, f):
    df.to_hdf(f, "df", format='table', complevel=9, complib='lzo')
    return
    store=pd.HDFStore(f,"w", complevel=9, complib='zlib')
    store.put("df", df, format="table", append=False)
    store.close()
    return 
    df.to_pickle(f)
    return
    if df.shape[0] < 5000000:
        version = 0
    else:
        version = 0
    with open(f, 'wb') as ff:
        pkl.dump(df, ff,version)
    #df.to_csv(f)

@time_me
def main(argv):
    taName = argv[1]
    sym2ta = get_all_from(os.path.join(root, 'data', taName))
    df = merge(sym2ta)
    df = df[df['ta_natr_14']  > 1.0]
    print df.shape
    out_file = os.path.join(root, 'data', taName, "merged_wth_na.pkl")
    save(df, out_file)

    df = df.replace([np.inf,-np.inf],np.nan)\
        .dropna()
    out_file = os.path.join(root, 'data', taName, "merged.pkl")
    save(df, out_file)

if __name__ == '__main__':
    main(sys.argv)


