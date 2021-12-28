#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:06:07 2020

@author: watchmen1
"""
import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

with open('B_vs_R_at_299V_pt2 - Sheet1.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        # x.append(float(row[1]))
        # y.append(float(row[0]))
x = np.array(x)
y = np.array(y)        
        
plt.scatter(x,y, marker='o')
m, b = np.polyfit(x, y, 1)

plt.plot(x, float(m)*x + float(b), 'g')
# x_ticks = np.arange(-0.010, 0.011, 0.002)
# plt.xticks(x_ticks)

plt.title('Magnetic Field Strength(B) vs Radius(r) at 299 Volts')

plt.xlabel('Radius(cm)')
plt.ylabel('Magnetic Field Strength (T - tesla)')

# plt.xlabel('Magnetic Field Strength (T - tesla)')
# plt.ylabel('Radius(cm)')

plt.savefig("B_vs_R_at_299V_pt2.pdf")

plt.show()