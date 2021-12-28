#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:51:05 2020

@author: watchmen1
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df_20 = pd.read_csv(r'/Users/watchmen1/Python_Projects/Physcial_Measurements_Lab_2/exp2_lif_20kv.txt', sep='\t')
df_30 = pd.read_csv(r'/Users/watchmen1/Python_Projects/Physcial_Measurements_Lab_2/exp2_lif_30kv.txt', sep='\t')

###load data into individual arrays
lif20kv_angle = np.array(df_20.iloc[:,0])
lif20kv_Crate = np.array(df_20.iloc[:,1])

lif30kv_angle = np.array(df_30.iloc[:,0])
lif30kv_Crate = np.array(df_30.iloc[:,1])

###load subset of data into arrays for creating linear fit lines###
lif20kv_angle_sub = np.array(df_20.iloc[148:201,0])
lif20kv_Crate_sub = np.array(df_20.iloc[148:201,1])

lif30kv_angle_sub = np.array(df_30.iloc[125:201,0])
lif30kv_Crate_sub = np.array(df_30.iloc[125:201,1])

### graph of lif at 20kv with linear fit line###
m, b = np.polyfit(lif20kv_angle_sub, lif20kv_Crate_sub, 1)
print(m, b)

xvals1 = np.linspace(26, 36, 400)

plt.figure(1)
plt.scatter(lif20kv_angle, lif20kv_Crate)
#plt.plot(lif20kv_angle, m * lif20kv_angle + b, color='red')
plt.plot(xvals1, m * xvals1 + b, color='red',label='linear fit: 0.414 x angle +(-10.337)')
plt.xlabel('Angle(degrees)')
plt.ylabel('Counting Rate(CPS)')
plt.title('First Peak LIF 20kV')
plt.legend()
plt.savefig('firstpeak_lif20kv.pdf')
plt.show()

### graog if lif at 30kv with linear fit line###
m2, b2 = np.polyfit(lif30kv_angle_sub, lif30kv_Crate_sub, 1)
print(m2, b2)

xvals2 = np.linspace(20, 36, 400)

plt.figure(2)
plt.scatter(lif30kv_angle, lif30kv_Crate)
plt.plot(xvals2, m2 * xvals2 + b2, color='red', label='linear fit: 0.629 x angle +(-12.433)')
plt.xlabel('Angle(degrees)')
plt.ylabel('Counting Rate(CPS)')
plt.title('First Peak LIF 30kV')
plt.legend()
plt.savefig('firstpeak_lif30kv.pdf')
plt.show()




