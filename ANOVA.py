# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

datafile="/Users/rachelrigg/Google Drive/Lab/Projects/Hsp70/Flow chamber/Stats/Flow chamber data VER PIF.csv"
data = pd.read_csv(datafile)

from scipy import stats

data.boxplot('y', by='trt', figsize=(8, 6))

import statsmodels.api as sm
from statsmodels.formula.api import ols
 
mod = ols('y ~ trt',
                data=data).fit()
                
aov_table = sm.stats.anova_lm(mod, typ=2)
print aov_table

from statsmodels.stats.multicomp import MultiComparison
mc = MultiComparison(data['y'], data['trt'])
result = mc.tukeyhsd()
 
print(result)
print(mc.groupsunique)
