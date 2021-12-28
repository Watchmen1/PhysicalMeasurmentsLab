#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:19:40 2020

@author: watchmen1
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(r'Temp vs ln(sigma).xlsx')

###put data into individual arrays
temp_pdoped = np.array(df.iloc[0:15, 0])
sigma_pdoped = np.array(df.iloc[0:15, 1])

temp_ndoped = np.array(df.iloc[0:16, 3])
sigma_ndoped = np.array(df.iloc[0:16, 4])

temp_undoped = np.array(df.iloc[0:16, 6])
sigma_undoped = np.array(df.iloc[0:16, 7])

print(temp_undoped)
print(sigma_undoped)

###graph of temp vs ln(sigma)
plt.plot(temp_pdoped, sigma_pdoped, color="red", label="p-doped")
plt.plot(temp_ndoped, sigma_ndoped, color="blue", label="n-doped")
plt.plot(temp_undoped, sigma_undoped, color="green", label="undoped")
plt.title(r'ln($\sigma$) vs Temperature')
plt.xlabel('Temperature (K)')
plt.ylabel(r'ln($\sigma$)')
plt.legend()
plt.savefig("ln_sigma_vs_Temp.pdf")