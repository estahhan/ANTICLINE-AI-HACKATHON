import numpy as np          #
import pandas as pd         #
import matplotlib.pyplot as plt
import seaborn as sns       #
from scipy import stats
from scipy import linalg

df_pre = pd.read_csv('wellbore_data_preproduction_well.csv')
df_pro = pd.read_csv('wellbore_data_producer_wells.csv')
df=df_pre.append(df_pro, ignore_index=True)

df.columns = ['Well_ID','X','Y','Depth','Porosity','Perm','AI','Facies','Density','Comp_vel','E','Vs','G']
df.describe().transpose()