#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:05:14 2020

@author: watchmen1
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(r'Hall Effect Data Reformat.xlsx')

###
hall_voltage_pdoped1 = np.array(df.iloc[0:11, 1])
sample_voltage_pdoped1 = np.array(df.iloc[0:11, 2])
sample_current_pdoped = np.array(df.iloc[0:11, 0])

hall_voltage_pdoped2 = np.array(df.iloc[0:15, 5])
sample_voltage_pdoped2 = np.array(df.iloc[0:15, 6])
temp_pdoped = np.array(df.iloc[0:15, 4])

hall_voltage_pdoped3 = np.array(df.iloc[0:7, 9])
sample_voltage_pdoped3 = np.array(df.iloc[0:7, 10])
bfield_pdoped = np.array(df.iloc[0:7, 8])

###
hall_voltage_ndoped1 = np.array(df.iloc[17:28, 1])
sample_voltage_ndoped1 = np.array(df.iloc[17:28, 2])
sample_current_ndoped = np.array(df.iloc[17:28, 0])

hall_voltage_ndoped2 = np.array(df.iloc[17:33, 5])
sample_voltage_ndoped2 = np.array(df.iloc[17:33, 6])
temp_ndoped = np.array(df.iloc[17:33, 4])

hall_voltage_ndoped3 = np.array(df.iloc[17:25, 9])
sample_voltage_ndoped3 = np.array(df.iloc[17:25, 10])
bfield_ndoped = np.array(df.iloc[17:25, 8])

###
hall_voltage_undoped1 = np.array(df.iloc[35:42, 1])
sample_voltage_undoped1 = np.array(df.iloc[35:42, 2])
sample_current_undoped = np.array(df.iloc[35:42, 0])

hall_voltage_undoped2 = np.array(df.iloc[35:51, 5])
sample_voltage_undoped2 = np.array(df.iloc[35:51, 6])
temp_undoped = np.array(df.iloc[35:51, 4])

print(hall_voltage_undoped2)
print(sample_voltage_undoped2)
print(temp_undoped)

### Hall voltage vs sample current p-doped and n-doped
plt.figure(1)
plt.plot(sample_current_pdoped, hall_voltage_pdoped1, color="red", label="p-doped")
plt.plot(sample_current_ndoped, hall_voltage_ndoped1, color="blue", label="n-doped")
plt.title('Hall voltage vs Sample current')
plt.xlabel('Sample Current(mA)')
plt.ylabel('Hall voltage (mV)')
plt.legend()
plt.savefig("Hall_Voltage_vs_Sample_Current_PandN.pdf")

### Hall voltage vs sample current undoped
plt.figure(2)
plt.plot(sample_current_undoped, hall_voltage_undoped1, color="green", label="undoped")
plt.title('Hall voltage vs Sample current')
plt.xlabel('Sample Current(mA)')
plt.ylabel('Hall voltage (mV)')
plt.legend()
plt.savefig("Hall_Voltage_vs_Sample_Current_undoped.pdf")

### Sample voltage vs sample current p-doped and n-doped
plt.figure(3)
plt.plot(sample_current_pdoped, sample_voltage_pdoped1, color="red", label="p-doped")
plt.plot(sample_current_ndoped, sample_voltage_ndoped1, color="blue", label="n-doped")
plt.title('Sample voltage vs Sample current')
plt.xlabel('Sample Current(mA)')
plt.ylabel('Sample voltage (V)')
plt.legend()
plt.savefig("Sample_Voltage_vs_Sample_Current_PandN.pdf")

### Sample voltage vs sample current undoped
plt.figure(4)
plt.plot(sample_current_undoped, sample_voltage_undoped1, color="green", label="undoped")
plt.title('Sample voltage vs Sample current')
plt.xlabel('Sample Current(mA)')
plt.ylabel('Sample voltage (V)')
plt.legend()
plt.savefig("Sample_Voltage_vs_Sample_Current_undoped.pdf")

### Hall voltage vs temperature p-doped and n-doped
plt.figure(5)
plt.plot(temp_pdoped, hall_voltage_pdoped2, color="red", label="p-doped")
plt.plot(temp_ndoped, hall_voltage_ndoped2, color="blue", label="n-doped")
plt.title('Hall voltage vs Temperature')
plt.xlabel('Temperature(K)')
plt.ylabel('Hall voltage (mV)')
plt.legend()
plt.savefig("Hall_Voltage_vs_Temp_PandN.pdf")

### Hall voltage vs temperature undoped
plt.figure(6)
plt.plot(temp_undoped, hall_voltage_undoped2, color="green", label="undoped")
plt.title('Hall voltage vs Temperature')
plt.xlabel('Temperature(K)')
plt.ylabel('Hall voltage (mV)')
plt.legend()
plt.savefig("Hall_Voltage_vs_Temp_undoped.pdf")

### Sample voltage vs temperature p-doped and n-doped
plt.figure(7)
plt.plot(temp_pdoped, sample_voltage_pdoped2, color="red", label="p-doped")
plt.plot(temp_ndoped, sample_voltage_ndoped2, color="blue", label="n-doped")
plt.title('Sample voltage vs Temperature')
plt.xlabel('Temperature(K)')
plt.ylabel('Sample voltage (V)')
plt.legend()
plt.savefig("Sample_Voltage_vs_Temp_PandN.pdf")

### Sample voltage vs temperature undoped
plt.figure(8)
plt.plot(temp_undoped, sample_voltage_undoped2, color="green", label="undoped")
plt.title('Sample voltage vs Temperature')
plt.xlabel('Temperature(K)')
plt.ylabel('Sample voltage (V)')
plt.legend()
plt.savefig("Sample_Voltage_vs_Temp_undoped.pdf")

### Hall voltage vs magnetic field p-doped and n-doped
plt.figure(9)
plt.plot(bfield_pdoped, hall_voltage_pdoped3, color="red", label="p-doped")
plt.plot(bfield_ndoped, hall_voltage_ndoped3, color="blue", label="n-doped")
plt.title('Hall voltage vs Magnetic Field')
plt.xlabel('Magnetic Field(mT)')
plt.ylabel('Hall voltage (mV)')
plt.legend()
plt.savefig("Hall_Voltage_vs_MagField_PandN.pdf")

### Sample voltage vs magnetic field p-doped and n-doped
plt.figure(10)
plt.plot(bfield_pdoped, sample_voltage_pdoped3, color="red", label="p-doped")
plt.plot(bfield_ndoped, sample_voltage_ndoped3, color="blue", label="n-doped")
plt.title('Sample Voltage vs Magnetic Field')
plt.xlabel('Magnetic Field(mT)')
plt.ylabel('Sample voltage (V)')
plt.legend()
plt.savefig("Sample_Voltage_vs_MagField_PandN.pdf")



