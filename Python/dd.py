#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'drawdowncalc' function below.
#
# The function is expected to return a FLOAT.
# The function accepts following parameters:
#  1. FLOAT_ARRAY rets
#  2. INTEGER N
#
import bisect
from copy import deepcopy
import numpy as np



def drawdowncalc_from_nav(prices):
    pre_p = 1
    cur_max=1
    cur_min=1
    dds = []
    predd = 0
    for idx,p in enumerate(prices):
        if p >= cur_max:
            cur_max = p
            predd = 0
        elif p < cur_max:
            cur_min = p
        
        print(f"current max {cur_max}")
        print(f"current min {cur_min}")
        if p>=cur_min and p<cur_max:
            dd = (1-cur_min / cur_max)
            if dd > predd:
                dds.append(dd)
            else:
                dds.append(0)
            predd = dd
        else:
            dds.append(0)
        pre_p = p
    return dds

def find_idx(dds):
    cur = -1
    next = -1
    idx = []
    for i in range(len(dds)-1):
        cur = dds[i]
        next = dds[i+1]
        if next ==0 and cur!=0:
            idx.append(cur)
    if dds[-1]!=0:
        idx.append(dds[-1])
    return idx
    

def drawdowncalc(rets, N):
    # Write your code here
    # this is to record the dd in order
    prets = np.insert(rets,0,0)
    navs = np.cumprod(prets + 1)
    res = drawdowncalc_from_nav(navs)
    print(res)
    idx = find_idx(res)
    idx = sorted(idx)[::-1]
    #print(len(idx))
    print(rets,N)
    print(idx)
    
    if N > len(idx):
        return len(idx)
    else:
        dd = -idx[N-1]
        

        return float("{:.4f}".format(dd))
    
    
    
    # convert in to returns
    

    
    
    # convert in to returns

    
rets = [-0.01, 0.01, -0.02, 0.02, -0.03, 0.03, -0.04, 0.04, -0.05, 0.05] 
n = 2

drawdowncalc(rets, n)