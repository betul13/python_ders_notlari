# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 17:53:05 2022

@author: betul
"""
#%%pandas series
import pandas as pd
s = pd.Series([87,445,23,212])
print(type(s))
print(s.index)
#%% veriye hızlı bakış
import pandas as np
import seaborn as sns
df = sns.load_dataset("titanic")
print(df.head)
#%% pandas seçim işlemleri
import pandas as np
import seaborn as sns
df = sns.load_dataset("titanic")
print(df.head)
