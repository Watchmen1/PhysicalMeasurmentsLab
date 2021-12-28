#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:32:12 2020

@author: watchmen1
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(r'electron.xlsx')
# print(df)
# print(df.info())

anode_voltage = np.array(df.iloc[2:7, 2])
inner_diam_B = np.array(df.iloc[2:7, 3])
outer_diam_B = np.array(df.iloc[2:7, 4])
inner_diam_G = np.array(df.iloc[2:7, 5])
outer_diam_G = np.array(df.iloc[2:7, 6])
print(anode_voltage)
print(outer_diam_B)

# inv_anode_voltage = 1 / (np.sqrt(anode_voltage))
# inv_anode_voltage = inv_anode_voltage.astype(float)

### Graph of anode voltage vs inner diam B
inner_diam_B = inner_diam_B.astype(float)

m, b = np.polyfit(anode_voltage, inner_diam_B, 1)
print(m, b)
plt.figure(1)
plt.scatter(anode_voltage, inner_diam_B)
plt.plot(anode_voltage, m * anode_voltage + b, label='slope = 1677.7 * x - 3.983')
plt.title('Inverse Square Root of Voltage vs Inner Radius of B')
plt.xlabel('Inverse Square Root of Voltage (V^-1/2)')
plt.ylabel('Inner Radius (mm)')
plt.legend()
plt.savefig("Voltage_vs_Inner_Radius_of_B.pdf")

### Graph of anode voltage vs outer diam B
outer_diam_B = outer_diam_B.astype(float)

m, b = np.polyfit(anode_voltage, outer_diam_B, 1)
print(m, b)
plt.figure(2)
plt.scatter(anode_voltage, outer_diam_B)
plt.plot(anode_voltage, m * anode_voltage + b, label='slope = 3312.8 * x - 12.514')
plt.title('Inverse Square Root of Voltage vs Outer Radius of B')
plt.xlabel('Inverse Square Root of Voltage (V^-1/2)')
plt.ylabel('Outer Radius (mm)')
plt.legend()
plt.savefig("Voltage_vs_Outer_Radius_of_B.pdf")

### Graph of anode voltage vs inner diam G
inner_diam_G = inner_diam_G.astype(float)

m, b = np.polyfit(anode_voltage, inner_diam_G, 1)
print(m, b)
plt.figure(3)
plt.scatter(anode_voltage, inner_diam_G)
plt.plot(anode_voltage, m * anode_voltage + b, label='slope = 1262.1 * x +4.531')
plt.title('Inverse Square Root of Voltage vs Inner Radius of G')
plt.xlabel('Inverse Square Root of Voltage (V^-1/2)')
plt.ylabel('Inner Radius (mm)')
plt.legend()
plt.savefig("Voltage_vs_Inner_Radius_of_G.pdf")

### Graph of anode voltage vs outer diam G
outer_diam_G = outer_diam_G.astype(float)

m, b = np.polyfit(anode_voltage, outer_diam_G, 1)
print(m, b)
plt.figure(4)
plt.scatter(anode_voltage, outer_diam_G)
plt.plot(anode_voltage, m * anode_voltage + b, label='slope = 3483.7 * x - 14.957')
plt.title('Inverse Square Root of Voltage vs Outer Radius of G')
plt.xlabel('Inverse Square Root of Voltage (V^-1/2)')
plt.ylabel('Outer Radius (mm)')
plt.legend()
plt.savefig("Voltage_vs_Outer_Radius_of_G.pdf")