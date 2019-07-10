"""
Author: Meng
Date: 2019/6/22
"""
from math import log

def calc_shannon_ent(dataset):
    numentries = len(dataset)
    labelcounts = {}
    for featvec in dataset:
        currentlabel = featvec[-1]
        if currentlabel not in labelcounts.keys():
            labelcounts[currentlabel] = 0
            